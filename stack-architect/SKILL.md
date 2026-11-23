# stack-architect: Diagramas de arquitectura con logos oficiales

Skill propia de wekyt (MIT). Genera diagramas de arquitectura de software
profesionales (HTML autocontenido, modo claro/oscuro) con logos vectoriales
oficiales en caché. El render ortogonal y la cascada de fuentes de logos
incorporan ideas de caru-ini/stack-diagram (MIT), con atribución en el README.

## Los 3 modos de entrada

1. **Proyecto**: `"Analiza este repo y sácame el diagrama"`:
   `python3 scripts/parse_context.py --repo /ruta/al/repo -o architecture.json`
   Lee `package.json`, `docker-compose.yml`, `pyproject.toml`, `requirements.txt`,
   `*.tf`, `.env.example` y deduce el stack (framework, BD, colas, pagos, IA…).
2. **Frase**: `"Dibuja: Next.js en Vercel, Supabase y Claude"`:
   `python3 scripts/parse_context.py --text "Next.js en Vercel, Supabase y Claude" -o architecture.json`
3. **PRD/documento**: pega el texto y pide el diagrama TO-BE:
   `python3 scripts/parse_context.py --text-file prd.txt -o architecture.json`
   (extrae componentes y flujos por palabras clave; el agente refina el JSON a mano
   si el documento es ambiguo: **siempre revisa `architecture.json` antes de renderizar**).

## Pipeline

```bash
cd stack-architect
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python3 scripts/parse_context.py --repo /ruta/al/repo -o /tmp/arch.json
# (opcional) edita /tmp/arch.json: ajusta layers, groups, edges
python3 scripts/fetch_logos.py /tmp/arch.json   # descarga SVGs oficiales a assets/cache/logos/
python3 scripts/render_html.py /tmp/arch.json -o /tmp/diagrama.html
```

### Buscar un logo por nombre

```bash
python3 scripts/buscar_logos.py "Next.js"              # lista candidatos validados
python3 scripts/buscar_logos.py "Next.js" --descargar  # guarda el mejor en caché
python3 scripts/validar_svg.py assets/cache/logos/*.svg  # audita la caché
```

Todo SVG descargado pasa por `validar_svg.py` **antes** de cachearse:
rechaza `<script>`, handlers `on*`, `<foreignObject>`, `javascript:`,
referencias externas http(s), `@import` externos y entidades XXE.
Ante la duda se descarta y se prueba la siguiente fuente. Los logos
oficiales nunca se alteran.

`render_html.py` valida el esquema, calcula el layout (columnas por `layer`,
flechas bezier sin cruzar etiquetas) y emite **un solo .html** con todo inlinado.
Ábrelo en el navegador o adjúntalo como artefacto.

## Esquema `architecture.json`

```json
{
  "title": "Mi App: Arquitectura",
  "direction": "LR",
  "groups": [{"id": "cloud", "label": "Vercel"}],
  "nodes": [
    {"id": "web", "label": "Next.js 14", "sublabel": "App Router",
     "brand": "nextdotjs", "layer": 1, "group": "cloud"}
  ],
  "edges": [{"from": "user", "to": "web", "label": "HTTPS"}]
}
```

- `layer`: columna 0–5 (0 = cliente/entrada, 5 = servicios externos profundos).
- `brand`: slug de Simple Icons (`nextdotjs`, `vercel`, `supabase`, `anthropic`,
  `postgresql`, `stripe`, `docker`…) o `lucide:<nombre>` para genéricos
  (`lucide:database`, `lucide:server`, `lucide:globe`, `lucide:cpu`, `lucide:webhook`).
  Ver `scripts/fetch_logos.py:BRAND_ALIASES` para alias comunes (`nextjs` → `nextdotjs`).
- `group`: id de `groups`: dibuja el contenedor punteado alrededor de sus nodos.

## Reglas

1. **Logos intocables**: nunca recolorear ni alterar los SVG oficiales.
2. **Offline-first**: si el SVG está en `assets/cache/logos/`, no se descarga nada.
3. **Seguridad**: `validar_svg.py` corre sobre cada descarga; lo que no pasa,
   no se cachea. Sin excepciones.
4. **Diseño (unslop)**: blueprint técnico: etiquetas de grupo en minúscula
   normal (nada de UPPERCASE con tracking), píldoras de protocolo en mono,
   todo en grilla de 4px, cromo neutro; el color lo ponen los logos.
5. **Verificación**: tras renderizar, abre el HTML y confirma: sin nodos
   encimados, sin etiquetas de flecha tachadas, logos visibles en claro Y oscuro.
4. **Marcas**: los logos son marcas de sus dueños; úsalos solo en diagramas
   descriptivos de arquitectura (práctica estándar), no como aval.
5. Si un `brand` no se encuentra en ninguna fuente, usa `lucide:<nombre>`
   y avisa cuál fue el fallback.

## Fuentes de logos (cascada)

1. **svgl** (`api.svgl.app`, marcas oficiales actuales: solo match exacto de título)
2. Simple Icons CDN (`cdn.simpleicons.org`, CC0)
3. Devicon (`raw.githubusercontent.com/devicons/devicon`)
4. gilbarbara/logos (`cdn.jsdelivr.net/gh/gilbarbara/logos`)
5. Lucide (`unpkg.com/lucide-static`) como fallback genérico (solo `lucide:<nombre>`)

El `brand` también acepta URL explícita: `"logo=https://sitio.com/logo.svg"`
para marcas que no están en ninguna fuente. Todo lo descargado se valida
con `validar_svg.py` y se registra en `assets/cache/logos/manifest.json`
(con la fuente y alerta de `white_fill`).

## Renderizado (dibujo de ingeniería)

El `render_html.py` genera nodos 132×100 (tile 60×60 + nombre + rol) y
**aristas ortogonales** (solo horizontal/vertical, codos a 90°):

- **Misma fila** → lado del tile al lado del tile (`y = topY+30`).
- **Misma columna** → base de la caja (`topY+100`) al tope del tile.
  Nunca desde el fondo del tile: cruzaría el texto.
- **Capas adyacentes** → codo por el corredor entre columnas
  (libre por construcción): horizontal corta → vertical en corredor →
  horizontal corta al destino.
- **Salto de >1 capa** → curva por debajo (caso raro).

**Etiquetas SOBRE la línea** con halo (`paint-order: stroke`), no píldoras
flotantes: horizontal → centrada sobre la línea; vertical → a la derecha.

**Jerarquía por `kind`**: `primary` = acento sólido (flujo principal),
`data` = neutral sólido, `trigger` = neutral punteado. La flecha usa
`context-stroke`: hereda el color de la línea en ambos temas.

Grupos: caja sutil con la etiqueta dentro de la esquina superior
izquierda (+ icono 14px opcional vía `"icon": "<brand>"`).

**La skill exige mirar el PNG antes de entregar** (`render_png.py`,
claro + oscuro). Si no tienes chromium a mano, la verificación visual se
hace con el navegador del sistema sobre el HTML.
