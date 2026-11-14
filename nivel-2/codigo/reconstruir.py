"""
Nivel 2 - Ubicaciones entre 22:40:00 y 22:55:00 (hora de Atenas, 15/08/2026).

ENTRADAS
- nivel-1/accesos.csv: cruces de puertas. Corrección: el reloj del controlador Sur
  atrasa 7 min 13 s (el mismo corte de luz figura 21:06:52 en Sur y 21:14:05 en
  Norte/Cella; la vuelta 21:07:32 vs 21:14:45). A todo evento Sur se le suman 433 s.
  Lo confirma el SMS de Yannis 23:08 "Volvió Theo" = Sur IN 23:00:47 + 7:13 = 23:08:00.
- nivel-2/celulares/*: WhatsApp (txt), Telegram (result.json, se usa date_unixtime),
  SMS (sms.xml, se usa el epoch en ms). Todo convertido a UTC+3.
- nivel-2/fotos/*: EXIF. Las fotos de relleno (CREDITOS.md) no tienen metadatos.
  Se usa GPSDateStamp+GPSTimeStamp (UTC) +3 h, porque el reloj de algunos equipos
  está mal (IMG_4661 de Leon dice 2025-01-01 pero su GPS marca 19:46 UTC = 22:46).
  La cámara Nikon de Ariadna está en UTC+2 (los fuegos 22:00-22:05 salen a las 21:01).
  Las coordenadas se asignan al sector más cercano del plano del informe.

SALIDA
- nivel-2/ubicaciones.json: para cada persona, tramos [desde, hasta) contiguos que
  cubren 22:40:00-22:55:00, armados a partir de los "anclajes" de evidencia de abajo.
"""
import csv, json, math, sys, datetime as D
from pathlib import Path

ROOT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
SUR_OFFSET = D.timedelta(seconds=433)

SECTORES = {  # plano operativo del informe inicial
    "cella": (37.97564, 23.72148), "templo": (37.97591, 23.72151),
    "terraza": (37.97582, 23.72179), "jardín": (37.97540, 23.72195),
    "cocina": (37.97532, 23.72146), "puerta-norte": (37.97630, 23.72162),
    "puerta-sur": (37.97515, 23.72135), "estacionamiento": (37.97656, 23.72215),
    "afuera": (37.97491, 23.72125),
}


def sector(lat, lon):
    return min(SECTORES, key=lambda s: math.dist((lat, lon), SECTORES[s]))


def foto_gps(path):
    """Devuelve (hora Atenas HH:MM:SS, sector) usando el GPS de la foto."""
    from PIL import Image, ExifTags  # solo para leer EXIF
    ex = Image.open(path).getexif()
    g = {ExifTags.GPSTAGS.get(k, k): v for k, v in ex.get_ifd(0x8825).items()}
    # Solo cuentan fotos del 15/08 (las de relleno son de otros días y a 400-700 m)
    if not g or g.get("GPSDateStamp") != "2026:08:15":
        return None
    dms = lambda v: float(v[0]) + float(v[1]) / 60 + float(v[2]) / 3600
    h, m, s = (int(x) for x in g["GPSTimeStamp"])
    hora = (D.datetime(2026, 8, 15, h, m, s) + D.timedelta(hours=3)).strftime("%H:%M:%S")
    return hora, sector(dms(g["GPSLatitude"]), dms(g["GPSLongitude"]))


def accesos(path):
    """Cruces OK con hora corregida (Sur +7:13)."""
    out = []
    for r in csv.DictReader(open(path, encoding="utf-8")):
        if r["resultado"] != "OK" or not r["credencial"]:
            continue
        t = D.datetime.fromisoformat(r["timestamp"])
        if r["puerta"] == "Sur":
            t += SUR_OFFSET
        out.append((t.strftime("%H:%M:%S"), r["credencial"], r["puerta"], r["tipo"]))
    return sorted(out)


# Anclajes: (hora en que empieza a valer, lugar, evidencia)
ANCLAJES = {
    "dafne": [
        ("22:38:00", "cella", "Cella IN 22:38; foto IMG_6152 22:45 GPS cella"),
        ("22:46:00", "templo", "Cella OUT 22:46; WA 22:46 'salí, voy por el pasillo'"),
        ("22:47:00", "terraza", "WA Kyra 22:47 'te veo. acá junto a la baranda'; selfie IMG_7305 22:50 terraza; WA 22:52 'estoy con Kyra todavía'"),
    ],
    "nikos": [
        ("22:39:00", "cella", "Cella IN 22:39; WA 22:40 'ya corté la alarma'"),
        ("22:43:00", "templo", "Cella OUT 22:43, camino a Norte"),
        ("22:44:00", "puerta-norte", "WA 22:45 'estoy con Eleni y tu sobrino' (ambos en Norte)"),
        ("22:52:00", "templo", "WA 22:52 'ya dejo Norte. vuelvo por adentro'; 22:54 'te vi recién en el pasillo'"),
        ("22:54:00", "cella", "Cella IN 22:54; WA 22:55 'alarma conectada'"),
    ],
    "theo": [
        ("22:40:00", "templo", "WA 22:40 'estoy en el pasillo del templo'"),
        ("22:41:00", "cella", "Cella IN 22:41; foto IMG_5739 22:42 GPS cella"),
        ("22:53:00", "templo", "Cella OUT 22:53; WA 22:53 'afuera de la sala'; Nikos 22:54 'te vi en el pasillo'. Sur OUT real 23:01"),
    ],
    "petros": [
        ("22:40:00", "templo", "TG 22:41 'estoy en el templo hablando con uno del museo'"),
        ("22:43:00", "puerta-norte", "TG 22:43 'ya estoy en Norte'"),
        ("22:44:00", "estacionamiento", "Norte OUT 22:44; foto IMG_5128 22:51 GPS estacionamiento; Norte IN 22:58. (Cella IN AG-004 22:48:31 no puede ser él)"),
    ],
    "marina": [
        ("22:40:00", "terraza", "TG 22:41 'yo tampoco bajé todavía' (arriba = terraza)"),
        ("22:42:00", "templo", "TG 22:41 'en un minuto': baja hacia Norte"),
        ("22:44:00", "puerta-norte", "TG 22:44 'llegando a la puerta, me frenaron'"),
        ("22:45:00", "estacionamiento", "Norte OUT 22:45; TG 22:50 'está abierto' (baúl); Norte IN 22:57"),
    ],
    "kyra": [("22:38:00", "terraza", "WA 22:38 'sigo arriba'; 22:44 'estoy en la terraza'; IMG_9140 22:48 y IMG_7305 22:50 terraza")],
    "ariadna": [("22:38:00", "jardín", "WA 22:38 'me planto en el jardín hasta q termine la banda'")],
    "eleni": [("22:40:00", "puerta-norte", "SMS 22:40 'No me muevo de acá'; Nikos 22:45; foto Leon IMG_4661 22:46 en Norte")],
    "yannis": [("22:40:00", "puerta-sur", "SMS 22:40 'Sigo en Sur hasta relevo de las 23:30'")],
    "stavros": [
        ("22:39:00", "cocina", "WA 22:39 'acá en cocina... me quedo con lo caliente'"),
        ("22:48:00", "puerta-sur", "WA 22:48 'estoy en Sur, vuelvo con hielo'"),
        ("22:49:00", "afuera", "Sur OUT 22:41:47+7:13 = 22:49:00; Sur IN real 22:57:00"),
    ],
    "ioanna": [("22:39:00", "terraza", "WA 22:39 'hago terraza hasta las once'; 22:48 'sigo en terraza'; IMG_9140 22:48 GPS terraza")],
    "leon": [("22:40:00", "puerta-norte", "SMS Eleni 22:40 'Leon sigue en Norte'; foto IMG_4661 GPS 22:46 Norte; WA 22:46 'no me están dejando pasar'")],
}

INI, FIN = "22:40:00", "22:55:00"


def tramos(anclajes):
    res = []
    for i, (t, lugar, _) in enumerate(anclajes):
        desde = max(t, INI)
        hasta = anclajes[i + 1][0] if i + 1 < len(anclajes) else FIN
        hasta = min(hasta, FIN)
        if desde < hasta:
            if res and res[-1]["lugar"] == lugar:
                res[-1]["hasta"] = hasta
            else:
                res.append({"desde": desde, "hasta": hasta, "lugar": lugar})
    assert res[0]["desde"] == INI and res[-1]["hasta"] == FIN
    assert all(a["hasta"] == b["desde"] for a, b in zip(res, res[1:]))
    return res


if __name__ == "__main__":
    # Verificación de evidencia (si están los archivos disponibles)
    fotos = ROOT / "nivel-2" / "fotos"
    if fotos.exists():
        for f in sorted(fotos.glob("*.[jJ][pP][gG]")):
            try:
                r = foto_gps(f)
            except Exception:
                r = None
            if r:
                print("foto", f.name, *r, file=sys.stderr)
    acc = ROOT / "nivel-1" / "accesos.csv"
    if acc.exists():
        for e in accesos(acc):
            if "22:35:00" <= e[0] <= "23:10:00":
                print("acceso", *e, file=sys.stderr)

    salida = {p: tramos(a) for p, a in ANCLAJES.items()}
    destino = ROOT / "nivel-2" / "ubicaciones.json"
    destino.parent.mkdir(parents=True, exist_ok=True)
    destino.write_text(json.dumps(salida, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(salida, ensure_ascii=False))
