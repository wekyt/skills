# taste-skill

**En prueba**

Skill de frontend anti-slop. Construye webs de empresa profesionales al nivel
de figma.com y x.ai: copy claro con voz propia, un solo sistema, una sección
por pantalla, bordes iguales, fotografías reales y UI real del producto, una
entrada de hero y uno o dos momentos repartidos en cada página, efectos shader
y escenas solo en páginas de tecnología, videojuegos y software,
micro-interacciones discretas, y un verificador y una puerta de acabado que lo
imponen en un navegador real.

## Demo

GIF pendiente. Falta un antes/después real: la skill se revisó el 21-nov
(veredicto: vale para trabajo web) pero no se instaló y no ha corrido sobre
ninguna página real todavía. La primera corrida real, candidata, es el pulido
de parluu.com (ver `PARLUU.md`): cuando exista esa página antes y después,
con su línea `GATE: PASS`, el GIF se genera desde esas dos capturas. No se
fabrica una demo con mockups.

## Verlo en video

Short en producción. Todavía no hay un Short de Píldora Tech donde se haya
usado esta skill.

## Antes / después

Sin corrida real todavía, sin números. Lo que se espera de la primera corrida
(parluu.com):

Entrada: la página actual de parluu.com, sin pulir con la skill. Salida: la
misma página con el sistema de la skill (una sección por pantalla, bordes
iguales, UI real del resultado como `app-frame`, colores de marca crema,
naranja y carbón por `start.mjs brand`, copy en español revisado a mano) y la
línea `GATE: PASS` o `GATE: OPEN` del verificador. Hasta que esa corrida
exista, esta sección queda en blanco y no se inventan cifras.

## Qué añade la adaptación wekyt

- `GUIA.md`: guía de uso en español (las nueve reglas de la casa, la corrida
  en siete pasos, el checklist, qué no hacer nunca).
- `ADAPTACION-NEXTJS.md`: cómo se usa la skill dentro de un proyecto Next.js
  (el kit en `public/assets`, exportación estática, la puerta contra la
  página construida o el servidor de desarrollo).
- `PARLUU.md`: notas de pulido para parluu.com (tipo software, colores de
  marca crema, naranja y carbón, la UI real es la página de resultado).

## Origen

tasteskill 2.5.1, de Leonxlnx (https://github.com/Leonxlnx/taste-skill),
licencia MIT. El cuerpo de la skill (`SKILL.md`) se mantiene en su inglés
original, porque sus verificadores, sus identificadores de comprobación y sus
comandos usan esos términos exactos. La descripción del frontmatter está en
español para que la skill se active con pedidos en español.

Versión de esta adaptación: `2.5.1-wekyt.1` (ver `VERSION`). La versión
original es `2.5.1`.

## Instalación

Copia esta carpeta a `~/.claude/skills/design-taste-frontend` o al directorio
de skills de tu proyecto. La skill necesita Node 22 o superior y Chrome, Edge
o Chromium. El comando `wekyt skill add` llegará después; por ahora la
instalación es copiando la carpeta.

Los assets viven en el repo original; tráelos antes de usar la skill. No se
empaquetan aquí por peso (37 MB, 1.594 archivos). Origen exacto:
https://github.com/Leonxlnx/taste-skill, ruta `skills/taste-skill/assets`,
licencia MIT. Comandos verificados 22-nov-2026 (traen solo esa ruta):

```bash
git clone --depth 1 --filter=blob:none --sparse https://github.com/Leonxlnx/taste-skill.git /tmp/taste-skill-original
cd /tmp/taste-skill-original && git sparse-checkout set skills/taste-skill/assets
cp -r skills/taste-skill/assets ~/.claude/skills/design-taste-frontend/assets
```

Sin esa carpeta, las rutas `assets/...` de la skill no resuelven.

## Estructura

- `SKILL.md`: la skill completa (inglés original + nota de adaptación).
- `GUIA.md`, `ADAPTACION-NEXTJS.md`, `PARLUU.md`: adaptación wekyt en
  español.
- `assets/`: el kit de componentes. No se incluye por peso (37 MB, 1.594
  archivos): se trae del repo original, ver Instalación y la sección Assets
  abajo.
- `library/`: paletas y tipografías (`palettes.json`, `type.json`).
- `references/`: las referencias que usa cada familia de recursos.
- `scripts/`: los verificadores (`gate.mjs`, `consistency.mjs`,
  `copy-lint.mjs`, `perf.mjs`, `photos.mjs`, `icons.mjs`, `shoot.mjs`,
  `start.mjs`, `moments.mjs`, `effects.mjs`).

## Assets

Qué contiene el kit, de dónde viene y cómo traerlo. Todo lo que la skill
necesita está documentado aquí; nada queda solo como una ruta suelta.

Origen: https://github.com/Leonxlnx/taste-skill, ruta
`skills/taste-skill/assets`, licencia MIT. Peso total: 37 MB, 1.594 archivos.
Comandos para traerlo (verificados 22-nov-2026): ver Instalación arriba.

Inventario:

| Parte | Archivos | Peso | Qué hace |
| --- | --- | --- | --- |
| `starter.html` | 1 | 35 KB | Página de partida de cada construcción |
| `system.css` | 1 | 103 KB | El sistema único de la página: paleta, fuentes, radios y bordes |
| `system.js` | 1 | 36 KB | El comportamiento que comparten las páginas: navegación, pestañas, menús |
| `backgrounds/` | 7 | 160 KB | Fondos CSS |
| `components/` | 87 | 772 KB | Piezas creativas `fx-*`, se montan como HTML, CSS y JS planos |
| `diagrams/` | 6 | 176 KB | Tarjetas de diagrama: hub, carriles, pulsos |
| `effects/` | 56 | 692 KB | Fondos con shader |
| `icons/` | 932 | 5,9 MB | Iconos reales a todo color, de marcas y de interfaz |
| `layout/` | 41 | 5,1 MB | Layouts de hero y secciones, con `deal.mjs` y `check.mjs` |
| `moments/` | 90 | 2,5 MB | Momentos de sitio premiado, de foto y de tipo |
| `motion/` | 5 | 96 KB | Capa de movimiento: entradas, hover, bucles de tarjeta |
| `objects/` | 122 | 6,3 MB | Objetos y renders de producto |
| `photos/` | 67 | 12 MB | Fotografías reales |
| `scenes/` | 61 | 3,1 MB | Escenas grandes |
| `ui/` | 117 | 732 KB | Fragmentos de UI y tarjetas |

Cada referencia `assets/...` de `SKILL.md`, `GUIA.md`,
`ADAPTACION-NEXTJS.md` y `references/` apunta a una parte de esta tabla.
Las referencias de `references/` y `scripts/` a rutas `assets/...` son las
mismas rutas del kit: se resuelven en cuanto la carpeta está en su sitio.

Fuera del kit, y por eso no están en la tabla: `assets/client/` es material
del cliente que pide el brief (tráiler, key-art), `assets/img/` es donde
`photos.mjs fetch` escribe las fotos del proyecto, y `dist/assets/index-*.js`
es la salida del bundler de un framework. Ninguno de los tres viene en el kit
ni hay que traerlo del repo original.

## Licencia

MIT (ver `LICENSE`). Copyright (c) 2026 Leonxlnx. La adaptación wekyt no
cambia la licencia ni la autoría.

---

# taste-skill

**In testing**

Anti-slop frontend skill. Builds professional company websites at the level of
figma.com and x.ai: plain copy in a voice of its own, one system, one section
per screen, equal edges, real photographs and real product UI, a hero entrance
and one or two dealt moments on every page, shader effects and scenes only on
tech, gaming and software pages, quiet micro-interactions, and a checker and
finish gate that enforce it in a real browser.

Demo GIF pending: the skill was reviewed on Nov 21 (verdict: worth it for web
work) but never installed and never run on a real page yet. The first real run,
candidate parluu.com (see `PARLUU.md`), will produce the before/after the GIF
needs. No Short exists yet.

Original: tasteskill 2.5.1 by Leonxlnx (https://github.com/Leonxlnx/taste-skill),
MIT license. This wekyt adaptation (version `2.5.1-wekyt.1`) keeps the skill
body in its original English and adds a Spanish guide (`GUIA.md`), a Next.js
adaptation (`ADAPTACION-NEXTJS.md`) and polish notes for parluu.com
(`PARLUU.md`).

Install: copy this folder to `~/.claude/skills/design-taste-frontend` or your
project's skills directory. Requires Node 22+ and Chrome, Edge or Chromium.
Assets are not bundled (37 MB, 1,594 files): fetch them from the original
repo first, see the Assets section in this README.
