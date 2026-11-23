---
name: desarma-video
description: Desarma un video de referencia (viral, Short, largo o clip generado por IA) para hacer uno original en el mismo formato: mide cortes, ritmo y audio con ffmpeg, extrae cuadros y línea de tiempo por plano, transcribe la voz con faster-whisper local y produce lista de planos, texto en pantalla, guion, plan de remake y los prompts para recrearlo. Se usa cuando el usuario pide "desarma este video", "cómo se hizo este video", "haz un video como este", "saca el guion y los planos de este video", comparte un viral para crear con IA o pega un enlace y pregunta qué lo hace funcionar o cómo hacer su propia versión. No es para publicar ni para descargar un video y volver a subirlo.
license: MIT
version: 1.0.0
---

# Desarma video

Convierte un video de referencia en todo lo necesario para hacer un video
original en el mismo formato: estructura, lista de planos, línea de texto,
guion, ritmo, recursos, ruta de producción por plano y prompts para recrearlo.

Los scripts miden. Tu miras los cuadros y describes. Nadie adivina: lo que no
se observó queda como "no confirmado". Esa regla es lo que hace el resultado
confiable para producir desde él.

Necesita `ffmpeg` y `ffprobe` en el PATH. YouTube se descarga con
`python3 -m yt_dlp`; los archivos locales no necesitan nada más. Para
transcribir, faster-whisper en local (modelo `small`).

## Límites

- El objetivo es un video nuevo en el mismo formato. El video descargado, sus
  cuadros y su audio son solo referencia. No se vuelven a subir, no se reutiliza
  su audio ni se pegan sus cuadros en el video nuevo. Si el usuario pide
  descargar un video y republicarlo, rechaza esa parte y ofrece el desarme más
  un remake original.
- Las descargas quedan en la carpeta de salida, en una carpeta nueva por video.
  Nada se envía a servicios de terceros.
- Solo lectura hacia la plataforma: una consulta del medio y la descarga. Ante
  bloqueo, 403 o 429, detente y reporta el mensaje. No reintentes ni lo rodees.
- Un video por corrida.

## El prompt original, cuando es público

Muchos virales traen su prompt publicado: en el comentario fijado, en la
descripción o en un documento compartido. Cuando exista:

- Captúralo VERBATIM, con su fuente (enlace y dónde aparece). Nunca lo resumas
  como si fuera el texto real.
- El prompt del remake DERIVA de ese prompt, no se inventa otro: se cambia
  solo lo necesario (sujeto o forma), un cambio por vez (cambio mínimo).
- La física se pide describiendo el RESULTADO VISUAL exacto con negativos
  explícitos (la tapa nunca se sale sola; el vidrio se hace añicos, no se parte
  en dos; el contenido CAE desde la rotura y nunca sube por encima del envase).
  Las palabras no simulan física.
- Si el momento clave está mal en el clip generado, es NO APTO aunque el resto
  funcione. Si el usuario ve un defecto en un clip de IA, el clip es NO APTO y
  no se discute ni se justifica.

## Flujo

### 1. Revisa las herramientas

```bash
ffmpeg -version && ffprobe -version
```

Si falta ffmpeg, da el comando de instalación y detente. Sin transcriptor, el
guion queda como no confirmado.

### 2. Consigue el video

Descarga el video público o trabaja sobre un archivo local. Usa una carpeta
nueva por video.

### 3. Analiza

```bash
# Duración, resolución, fps y audio
ffprobe -v error -show_entries format=duration,size -show_entries stream=width,height,r_frame_rate,codec_name,codec_type -of default=noprint_wrappers=1 <video>

# Detección de cortes por cambio de escena
ffmpeg -i <video> -vf "select='gt(scene,0.4)',showinfo" -f null - 2>&1 | grep showinfo

# Un cuadro por segundo para la tira de tiempo
mkdir -p <carpeta>/tira && ffmpeg -i <video> -vf fps=1 <carpeta>/tira/cuadro_%04d.jpg

# Hoja de contacto (un cuadro cada 2 s en rejilla)
ffmpeg -i <video> -vf "fps=1/2,scale=320:-1,tile=4x4" -frames:v 1 <carpeta>/contacto.jpg

# Audio: presencia de voz y música, sonoridad
ffprobe -v error -show_entries stream=codec_type -of csv <video>
ffmpeg -i <video> -vn -af loudnorm=print_format=json -f null - 2>&1 | grep -A12 Parsed_loudnorm
```

Abre la hoja de contacto primero. Si la cantidad de planos parece mal contra
ella (las transiciones animadas y los fundidos se pierden fácil; la acción
rápida agrega cortes falsos), corrige a mano y anota el cambio.

**REFERENTE: MIRAR LOS CUADROS, NO EL RESUMEN.** Cuando el usuario apunta a un
referente, lo que se ve realmente se verifica en los CUADROS del video, no en
un resumen propio. Un resumen no es fuente de verdad sobre lo visual.

### 4. Transcribe (cuando el video tiene voz)

Decodifica el audio a PCM de 16 kHz mono con ffmpeg y pásale el array a
faster-whisper (modelo `small`, en local). Sin transcripción, el guion se
reporta como no confirmado. No escribas líneas habladas desde lo que los
subtítulos parecen decir.

### 5. Revisa los cuadros

Mira las imágenes de cada plano (primero, último, hoja de contacto, tira) y
anota por plano:

- `tipo`: plano fijo, cámara en mano, captura de pantalla, animación, foto con
  zoom, entrevista, b-roll.
- `descripcion`, `camara`, `transicion de entrada`.
- `texto en pantalla`: cada texto con su rol, posición y tiempos leídos de la
  tira. Un ítem por cada estado distinto del texto.
- `capas`: pegatinas, picture-in-picture, capturas, logos. Todo lo compuesto
  sobre la imagen base que no sea texto.

Para todo el video: `hook` (qué muestran los primeros segundos y qué
prometen), `estructura` (secciones con tiempos), `estilo visual`, `recursos`
(cada uno marcado como `el usuario lo aporta`, `se puede generar` o `solo
referencia`), `sonidos`.

Cómo mirar:

- Los candidatos de cambio de texto marcan momentos donde una banda del cuadro
  cambió mientras el resto quedaba quieto. Revisa cada uno. Un plano sin
  candidatos igual puede tener texto cambiando (el texto sobre video en
  movimiento nunca dispara), así que escanea cada tira.
- Cuando la tira sea muy gruesa para leer o medir algo, extrae cuadros a más
  fps en ese rango.
- `poco movimiento` significa que la imagen casi no cambia: probablemente un
  fijo o una pausa. Si igual lo describes como video en movimiento, di que se
  mueve.
- Si un plano detectado contiene dos planos distintos, divídelo y vuelve a
  analizar.

Audio: no puedes oírlo. `voz presente` y `musica presente` quedan como `"no
confirmado"` salvo que haya evidencia: una transcripción con voz (solo voz),
un archivo sin pista de audio o el usuario diciendo lo que oyó (`fuente:
usuario` con sus palabras en `nota`). Cuando importe para el remake, pide al
usuario que escuche y diga si hay música, voz y efectos de sonido en los
cortes o en los textos. Registra los efectos en `sonidos`.

### 6. Prompts de vídeo generado por IA para el remake

Cuando el remake usa clips generados por IA (por ejemplo, Google Flow con
Omni 1.2: clips de 3 a 15 s; consulta el coste actual en la herramienta antes
de prometer nada):

- Un prompt por clip, con beats exactos cada 2 segundos (qué pasa en cada
  beat) y encadenamiento por último frame.
- Cada prompt lleva el resultado visual exacto y negativos explícitos de
  física (ver arriba).
- Si existe prompt original público, el prompt del remake es ese prompt con el
  cambio mínimo (sujeto o forma), no uno nuevo.
- Brazos bajos y sujeto visible; nunca poses de brazos arriba o estirados (la
  IA elabora manos con dedos).

En nuestra práctica, un Short lleva como mucho 2 clips generados; el resto es
motion graphics y material real. Esa es una regla de oficio, no un límite de
la herramienta.

### 7. Reporte y plan de remake

Sigue esta plantilla. Muestra la hoja de contacto, lidera con el hook y la
estructura, luego la tabla de planos, luego lo no confirmado, luego el plan de
producción. Adapta el formato, no el contenido: guion nuevo, material nuevo,
el tema del usuario.

```
DESARME · <título o enlace> · <duración> · <resolución>
Hook: ...
Estructura: ...
Prompt original: <verbatim + fuente, o "no publicado">
PLANOS
1. 0,0-2,4 s | tipo | descripción | texto en pantalla | sonido
...
NO CONFIRMADO
- ...
PLAN DE REMAKE
1. plano 1 -> ruta (grabar / render por código / grabar pantalla / ffmpeg / clip generado por IA) + recursos que faltan
...
PROMPTS DE VÍDEO GENERADO
1. clip 1 (0-8 s): <prompt completo>
...
```

## Archivos

| Archivo | Propósito |
|---|---|
| `breakdown.json` | Todo lo medido y revisado |
| `tira/` | Cuadros a 1 fps con tiempo |
| `contacto.jpg` | Hoja de contacto del video |
| `transcripcion.json` | Transcripción normalizada, cuando existe |
| `prompt-original.txt` | Prompt original verbatim + fuente, cuando es público |
| `remake.md` | El plan de producción + prompts de vídeo generado |
