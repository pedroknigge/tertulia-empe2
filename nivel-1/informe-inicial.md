# Informe inicial · Gala de las Panateneas

El sábado 15 de agosto de 2026 se celebró una gala privada en el Templo de Atenea, en el Ágora de Atenas. Se emitieron 48 credenciales nominativas. Los invitados ingresaron desde las 19:30; el personal de preparación pudo ingresar desde las 08:00. El registro entregado abarca la jornada completa, desde el recinto vacío antes del montaje hasta las 23:59. Quien no tiene una salida registrada puede seguir dentro al final del registro.

En la cella, sala interior del templo, se exhibía una corona de olivo de oro. Por trabajos de iluminación se acordó desconectar la alarma de la vitrina entre las 22:40 y las 22:55 y cubrirla con una tela negra. La ceremonia estaba prevista para las 23:15. A las 23:10, al retirar la tela, la curadora Dafne Kostas advirtió que la corona no estaba en su soporte.

Entre las 22:00 y las 22:05 se realizó el espectáculo de fuegos artificiales. Toda referencia horaria de este informe corresponde a Atenas, UTC+3, del 15/08/2026.

## Instalaciones y control de acceso

Norte conecta el exterior con el acceso de invitados. Sur conecta el exterior con el acceso de servicio. Cella es una puerta interior: cruzarla no equivale a entrar o salir del recinto. El templo, el jardín, la terraza, la cocina y el lado interior de los puestos de guardia están dentro del recinto. El estacionamiento de invitados y la zona de vehículos de servicio están fuera.

Cada lector registra el identificador de evento, su fecha y hora, la puerta, la credencial, el nombre, el tipo y el resultado. `IN` y `OUT` indican el sentido del cruce respecto del espacio controlado por esa puerta. `POWER_FAIL` y `POWER_RESTORE` corresponden al suministro eléctrico y no llevan credencial. Los números de evento pertenecen a cada controlador. `OK` indica autorización y `DENEGADO` indica un intento sin cruce; puede ocurrir por falta de permiso o por una lectura incompleta. Las credenciales son personales.

## Lugares para las respuestas

Usen exactamente estos valores: `cella`, `templo`, `terraza`, `jardín`, `cocina`, `puerta-norte`, `puerta-sur`, `estacionamiento`, `afuera`. `Templo` incluye los pasillos y la escalinata interior, sin incluir la cella ni la terraza. `Afuera` incluye la zona de camiones del acceso de servicio. El estacionamiento de invitados usa su valor específico.

El plano operativo de la gala utiliza los siguientes puntos de referencia; las coordenadas están expresadas en grados decimales WGS84. Son centros aproximados de sectores, no límites catastrales.

| Sector | Latitud | Longitud |
|---|---:|---:|
| cella | 37.97564 | 23.72148 |
| templo | 37.97591 | 23.72151 |
| terraza | 37.97582 | 23.72179 |
| jardín | 37.97540 | 23.72195 |
| cocina | 37.97532 | 23.72146 |
| puerta-norte | 37.97630 | 23.72162 |
| puerta-sur | 37.97515 | 23.72135 |
| estacionamiento | 37.97656 | 23.72215 |
| afuera, sector de servicio | 37.97491 | 23.72125 |

## Credenciales emitidas y permisos

| Credencial | Nombre | Función | Puertas habilitadas |
|---|---|---|---|
| AG-001 | Dafne Kostas | Curadora del templo | Norte, Sur, Cella |
| AG-002 | Nikos Andreou | Jefe de seguridad | Norte, Sur, Cella |
| AG-003 | Theo Kallis | Técnico de iluminación | Norte, Sur, Cella |
| AG-004 | Petros Galanis | Coleccionista invitado | Norte |
| AG-005 | Marina Sotiriou | Mecenas de la gala | Norte |
| AG-006 | Kyra Alexiou | Periodista | Norte |
| AG-007 | Ariadna Lykou | Fotógrafa oficial | Norte, Sur |
| AG-008 | Eleni Markou | Guardia Puerta Norte | Norte, Sur |
| AG-009 | Yannis Petridis | Guardia Puerta Sur | Norte, Sur |
| AG-010 | Stavros Demou | Encargado del catering | Sur |
| AG-011 | Ioanna Vasileiou | Moza del catering | Sur |
| AG-012 | Leon Kostas | Voluntario | Norte |
| AG-013 | Andreas Pappas | Personal de montaje | Sur |
| AG-014 | Sofia Rallis | Personal de montaje | Sur |
| AG-015 | Dimitris Vrettos | Personal de montaje | Sur |
| AG-016 | Chloe Mavrou | Personal de montaje | Sur |
| AG-017 | Ilias Drakos | Invitado | Norte |
| AG-018 | Melina Rizou | Personal de montaje | Sur |
| AG-019 | Kostas Bellos | Invitado | Norte |
| AG-020 | Nefeli Pagonis | Invitado | Norte |
| AG-021 | Panos Dimas | Personal de montaje | Sur |
| AG-022 | Rena Kalogianni | Invitado | Norte |
| AG-023 | Alexis Sarris | Invitado | Norte |
| AG-024 | Myrto Xanthou | Personal de montaje | Sur |
| AG-025 | Giorgos Spanos | Invitado | Norte |
| AG-026 | Eva Karali | Invitado | Norte |
| AG-027 | Christos Zervas | Personal de montaje | Sur |
| AG-028 | Lydia Vardas | Invitado | Norte |
| AG-029 | Marios Fotiou | Invitado | Norte |
| AG-030 | Anna Gika | Personal de montaje | Sur |
| AG-031 | Orestis Lazos | Invitado | Norte |
| AG-032 | Zoe Lappa | Invitado | Norte |
| AG-033 | Vasilis Raptis | Personal de montaje | Sur |
| AG-034 | Dora Malamou | Invitado | Norte |
| AG-035 | Pavlos Mantas | Invitado | Norte |
| AG-036 | Mina Tzavela | Personal de montaje | Sur |
| AG-037 | Stefanos Vellis | Invitado | Norte |
| AG-038 | Lena Arvaniti | Invitado | Norte |
| AG-039 | Haris Deli | Personal de montaje | Sur |
| AG-040 | Olga Kanelou | Invitado | Norte |
| AG-041 | Michalis Kontos | Invitado | Norte |
| AG-042 | Iris Maniati | Personal de montaje | Sur |
| AG-043 | Filippos Balis | Invitado | Norte |
| AG-044 | Nadia Lambrou | Invitado | Norte |
| AG-045 | Sotiris Lekkas | Personal de montaje | Sur |
| AG-046 | Efi Koroni | Invitado | Norte |
| AG-047 | Aris Politis | Invitado | Norte |
| AG-048 | Vera Nasi | Personal de montaje | Sur |
