# Análisis de YouTube Studio

Skill propia de wekyt (MIT). Playbook para convertir cada video publicado en
una lección que mejora el siguiente. Nació para el canal Píldora Tech, donde
corre a diario desde el 24-oct-2026; las rutas de abajo usan
`<tu-workspace>` como marcador de tu carpeta de trabajo.
Se aplica en la tarea diaria de análisis y alimenta el reporte semanal.

## Fuente de datos
YouTube Studio de tu canal, vía navegador con la sesión ya iniciada. Si la
sesión venció, el dueño del canal re-ingresa una vez; nunca se pide una
contraseña por chat.

## Qué se toma por video (Short y largo, por separado)
- Impresiones, CTR (clics / impresiones), vistas, duración media vista, retención
  (especialmente el % que sigue a los 30 s en Shorts y la curva de los primeros 30 s
  en largos), "me gusta", comentarios, suscriptores ganados por ese video.
- Fuente de tráfico principal (feed de Shorts, búsqueda, sugeridos, externo).
- Edad del video al medir: un video de 2 horas NO se compara con uno de 3 días.
  Marcar siempre "señal temprana" vs "dato maduro" (a partir de 48–72 h).

## Cómo se atribuye "qué funcionó"
Comparar solo dentro de la misma familia (Short vs Short, largo vs largo) y, dentro
de ella, por subformato (noticia, tutorial, Product Hunt, dato-tarjeta). Para cada
video, registrar en una línea: tema, subformato, gancho de los primeros 3 s, título,
miniatura, hora de publicación, y las métricas clave. Luego buscar patrones:
- Gancho: ¿qué aperturas retienen más a los 30 s? Repetir la estructura ganadora.
- Título/miniatura: CTR alto con vistas bajas = buen empaque, mal alcance;
  CTR bajo = probar otro titular/miniatura en el siguiente video del mismo tema.
- Tema: el tema que rinde se repite con variación (nuevo ángulo, no copia).
- Hora: comparar 11:00 vs 19:00 con al menos 2 semanas de datos antes de mover horarios.
- Suscriptores: el video que más suscriptores convierte marca el tipo de contenido
  que construye canal, no solo vistas.

## Base de datos y tablero (desde 2026-10-24)
Toda medición queda registrada en SQLite, no solo en el documento:
- Base: `<tu-workspace>/studio.db`
  - `videos`: youtube_id, titulo, tipo (short/largo), subformato, tema, gancho,
    titulo_texto, fecha_publicacion, hora_publicacion, radar_puntaje, estado.
  - `metricas`: video_id, fecha_medicion, madurez (temprana/madura), vistas,
    impresiones, ctr, duracion_media_seg, retencion_30s, likes, comentarios,
    subs_ganados, fuente_principal. Una fila por video y día (UNIQUE).
- Cada corrida: inserta la fila del video si no existe y añade la medición del día
  (o la actualiza si ya existe para esa fecha). Nunca borra mediciones anteriores:
  la historia es lo que permite comparar.
- Después de escribir, corre `python3 <tu-workspace>/export_dashboard.py`
  para regenerar `dashboard/datos.json`.
- Repo del tablero: cuando exista tu repo del tablero, sincronizar ahí
  `dashboard/` (index.html + datos.json) con el flujo de equipo (una sola
  subida por corrida). El tablero es una página estática sin backend: lee
  datos.json y muestra totales + tabla por video.
  El equipo de desarrollo puede construir encima (gráficas, filtros, comparativas)
  sin tocar la recolección.

## Decisiones que salen de cada análisis
Cada corrida escribe en `<tu-workspace>/analisis-studio.md`:
1. Tabla del día (una fila por video medido).
2. "Qué funcionó" (máx. 3 hallazgos con el dato que los respalda).
3. "Qué ajustar" (máx. 3 decisiones concretas para los próximos videos: gancho,
   tema, título, formato u hora). Estas decisiones las deben leer los crons de
   producción AM/PM antes de elegir tema.
4. Si un video supera claramente al resto (2x o más en vistas o suscriptores),
   avisar al dueño del canal en el chat con el dato y la hipótesis de por qué.

## Reglas
- Los datos mandan; sin dato, es opinión y se marca como tal.
- Nunca prometer cifras futuras ("millones") como hecho: son la meta, no el pronóstico.
- No tocar nada en Studio (no borrar, no cambiar títulos, no republicar).
- El reporte semanal (lunes) consolida los datos maduros de la semana; el análisis
  diario solo registra señales y decisiones.
