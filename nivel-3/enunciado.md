Reciben ocho grabaciones en `interrogatorios/`: Dafne, Nikos, Theo, Petros, Marina, Kyra, Yannis y Leon. Pueden contrastarlas con los archivos recibidos anteriormente.

Estas grabaciones están bajo secreto de sumario dentro de la simulación: transcriban y separen hablantes con herramientas locales. No envíen los audios a servicios externos. La organización está autorizada a evaluar los textos entregados con su juez. No suban los MP3 al repositorio de respuestas.

Suban ocho archivos UTF-8 en `nivel-3/transcripciones/`, llamados `dafne.txt`, `nikos.txt`, `theo.txt`, `petros.txt`, `marina.txt`, `kyra.txt`, `yannis.txt` y `leon.txt`. Escriban un turno por línea, con `Interrogador: texto` o `Nombre: texto`; usen el nombre de pila con inicial mayúscula. Marquen `[inaudible]` o `[solapamiento]` cuando corresponda, sin completar palabras que no puedan reconocer.

Suban también `nivel-3/contradicciones.json`: una lista de objetos con los campos `persona` (identificador en minúsculas usado en la entrega anterior), `afirmacion` (texto), `evidencias` (lista de referencias) y `explicacion` (texto). Registren las discrepancias y los límites de las declaraciones frente al expediente, sin repetir el mismo hallazgo con otras palabras.

Cada referencia es una ruta relativa al material recibido, por ejemplo `nivel-3/interrogatorios/nombre.mp3`. Pueden agregar `#t=120` para un segundo de audio, `#L25` para una línea de texto, `#N-0001` para un evento de CSV, `#mensaje-12` para un SMS o `#chat-10000:mensaje-12` para Telegram. En una foto pueden agregar `#EXIF` o `#imagen`. Usen sólo referencias existentes. No agreguen explicaciones fuera del JSON.
