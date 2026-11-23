# Guía de taste-skill (español)

tasteskill 2.5.1, la skill de frontend anti-slop. Construye webs de empresa
profesionales al nivel de figma.com y x.ai: copy claro con voz propia, un solo
sistema, una sección por pantalla, bordes iguales, fotografías reales y UI real
del producto, una entrada de hero y uno o dos momentos repartidos en cada
página, efectos shader y escenas solo en páginas de tecnología, videojuegos y
software, micro-interacciones discretas, y un verificador y una puerta de
acabado que lo imponen en un navegador real.

Original de Leonxlnx (https://github.com/Leonxlnx/taste-skill), licencia MIT.
El cuerpo de la skill (`SKILL.md`) se mantiene en su inglés original, porque
sus verificadores, sus identificadores de comprobación y sus comandos usan esos
términos exactos. Esta guía es la puerta de entrada en español.

## Cuándo se usa

Cuando se construye, diseña, rediseña, cambia el estilo, pule o revisa una
landing, una web de empresa, producto, tienda, cafetería, hotel, estudio,
SaaS, IA, herramienta de desarrollo o videojuego, como HTML/CSS estático o
dentro de un proyecto existente de React, Next.js, Vue, Svelte, Astro o
Tailwind, o cuando el usuario dice que una página se ve genérica, de plantilla
o "hecha por IA".

## Requisitos

Node 22 o superior y Chrome, Edge o Chromium. ffmpeg es opcional. Los
verificadores de la skill abren un Chrome headless con WebGL por CPU, uno a la
vez, en primer plano, con un tiempo límite de 10 minutos. Nunca en segundo
plano, nunca en un navegador con ventana, nunca con una herramienta de
navegador.

## Assets: qué son y cómo traerlos

Los assets viven en el repo original; tráelos antes de usar la skill. No se
empaquetan aquí por peso: 37 MB, 1.594 archivos.

Origen exacto: https://github.com/Leonxlnx/taste-skill, ruta
`skills/taste-skill/assets`, licencia MIT. Para traerlos (comandos verificados
22-nov-2026, traen solo esa ruta, no el repo entero):

```bash
git clone --depth 1 --filter=blob:none --sparse https://github.com/Leonxlnx/taste-skill.git /tmp/taste-skill-original
cd /tmp/taste-skill-original && git sparse-checkout set skills/taste-skill/assets
cp -r skills/taste-skill/assets ~/.claude/skills/design-taste-frontend/assets
```

Si prefieres el clon completo, es `git clone --depth 1
https://github.com/Leonxlnx/taste-skill.git` y la carpeta a copiar es la
misma: `skills/taste-skill/assets`.

Sin esa carpeta, las rutas `assets/...` de esta guía y de `SKILL.md` no
resuelven, y el paso 0 de la corrida no tiene kit que copiar. El inventario
completo, con lo que hace cada parte, está en `README.md`, sección Assets.

## Las nueve reglas de la casa

Estas nueve mandan sobre todo lo demás en la skill.

1. **Nada de pie de foto ni descripción debajo de ninguna imagen, render o
   visual.** Los créditos de licencia van en una sola línea del pie de página.
2. **Cada visual se dibuja, nunca queda un hueco vacío,** a 1440, 1024, 768 y
   390 píxeles de ancho.
3. **Una sección por pantalla:** el hero solo en la primera pantalla, cada
   sección exactamente una o dos pantallas de alto a 1440x900, sin que asome
   el título de la sección siguiente. La única excepción es una sección viva
   de `photo-chapters`, de tres o cuatro pantallas, fijada por el momento.
4. **Bordes izquierdo y derecho iguales en el contenido.**
5. **Micro-animaciones al pasar el puntero:** una tarjeta enlazada sube 2 px,
   una foto hace zoom 1.02-1.03 dentro de su marco, los botones se marcan al
   pasar y se hunden al hacer clic, los subrayados se dibujan, los bucles de
   tarjeta ciclan en 2.5-4 s, se repiten y reinician al pasar el puntero. La
   capa de movimiento lo hace; nunca se quita ni se anula. Nada de inclinación,
   carruseles ni pestañas temporizadas. Cada hero entra una vez al cargar
   (`data-enter`), y cada página lleva uno o dos momentos repartidos.
6. **Más y mejores fotografías reales donde encajen;** mejores fondos, mejores
   heroes, mejores layouts y mejores fuentes.
7. **Iconos reales a todo color** (el icono real de un producto conocido, nunca
   uno dibujado); visuales de diagrama pequeños en tarjetas.
8. **Las grandes escenas y los momentos creativos son parte de la skill:**
   cada página reparte sus momentos (de foto y de tipo fuera de la tecnología),
   pero los efectos shader y las escenas solo donde el oficio tiene un tema
   técnico (tecnología, IA, herramientas de desarrollo, videojuegos, fintech,
   hardware), nunca en una cafetería, panadería, casa rural o tienda local:
   esas llevan fotografías.
9. **Direcciones:** calle y barrio solamente, sin número de portal, código
   postal ni coordenadas; sin números de registro ni de IVA; sin teléfono en
   formato real; los contactos van en `.example`.

## La corrida, en siete pasos

El detalle completo está en `SKILL.md`, sección 4. El resumen:

0. **El stack.** Una carpeta vacía construye una página estática: se copia
   `<skill>/assets` a `assets` y se parte de `assets/starter.html`. Un
   proyecto existente construye con su propio stack, sus componentes toman el
   marcado y las clases del starter, con el kit copiado en su carpeta pública
   (`public/assets`) y cargado desde ahí como archivos planos. Un brief que
   pide Next.js construye una exportación estática (`output: 'export'`) y se
   revisa sobre la página construida (`--root out`). Ver
   `ADAPTACION-NEXTJS.md`.
1. **Lee el brief.** Anota el tipo (sección 1 de la skill), qué se vende, quién
   lo compra, la acción principal (la transacción: reservar, pedir, empezar
   la prueba gratis) y el material real: logo, pantallas, fotografías,
   precios, dirección, horarios. Después arma la puerta de acabado, antes de
   que exista ninguna página: `node <skill>/scripts/gate.mjs --start
   index.html --kind <tipo> --category "<qué se vende>" --primary "<acción
   principal>"`. Un build de framework nombra la URL de su servidor de
   desarrollo o su página construida en lugar de `index.html`, y reconstruye
   antes de cada corrida de la puerta.
2. **Escribe todo el copy primero,** con la capa de copy (`copy-voice.md`): el
   h1 nombra la categoría y el comprador o el lugar, un dato duro en la primera
   pantalla, un sustantivo en cada título, los botones como verbo y objeto.
   Nada se inventa salvo un nombre de marca acuñado (buscado primero, el
   resultado se guarda en `names.json` junto a la página) y, en un lugar,
   horarios y precios plausibles, cada uno marcado `data-assumed`.
3. **Planea la página por pantallas.** Línea 1: el tipo. Línea 2: el reparto
   (paso 4), con una frase sobre por qué la paleta encaja con el oficio. Después
   una línea por sección: su id, su única idea, su imagen y su tipo, sus
   pantallas, qué sección lleva un momento y por qué se mueve.
4. **Reparte, nunca elijas por gusto.** Cada comando guarda un historial, así
   las páginas salen distintas: el hero se reparte con `deal.mjs`, las tres
   paletas hechas para el oficio con `start.mjs deal`, el CSS con `start.mjs
   css`, los colores propios del cliente con `start.mjs brand`, los momentos
   con `moments.mjs pick`. Se toma la primera paleta y el primer emparejamiento
   que se imprimen. Nunca violeta: se vuelve a repartir. El radio es `sharp`
   para fintech y herramientas de desarrollo, `soft` por defecto y `round`
   para apps de consumo.
5. **Construye.** En `starter.html`: `<html lang data-type data-radius
   data-buttons data-motion>`, los tres metas, el bloque head y la clase del
   nav; se copia solo la sección del hero repartido; cada sección es `main >
   section` con un `.wrap`, su h2 primero. La UI se pega desde
   `assets/ui/<nombre>/fragment.html` y se reescriben cada nombre, número y
   logo con los del cliente. Un efecto, objeto, momento o escena se monta
   exactamente como dice su referencia, nunca con un script propio.
6. **Revisa y mira.** Solo los scripts de la skill, en este orden:
   `copy-lint.mjs`, `consistency.mjs`, `assets/layout/check.mjs`,
   `shoot.mjs`, `perf.mjs`. Corrige cada FAIL (también los WARN de copy-lint,
   o di por qué quedan) y vuelve a disparar. Después la puerta:
   `node <skill>/scripts/gate.mjs index.html`. Corrige lo que liste y repite
   hasta que su última línea sea `GATE: PASS` o `GATE: OPEN`, tres rondas
   como máximo. Un FAIL que se juzgue falso se dispensa en
   `.taste-skill/waivers.json` con su motivo, nunca se arregla engañando a la
   comprobación.
7. **Informa:** la línea `GATE:` primero, después cada dispensa con su motivo
   y cada FAIL abierto; el tipo, el reparto, la tarjeta de voz en una línea;
   los resultados del verificador, del layout y del rendimiento; lo que no se
   pudo comprobar; cada dato asumido; las fotografías y el arte que el cliente
   debe entregar, con cada marco de sustitución entre ellos.

## El checklist

`SKILL.md`, sección 5, trae el checklist completo: primera pantalla, una
sección por pantalla, bordes iguales, cada visual dibujado, nada de pies de
foto, lo que corresponde a cada tipo, movimiento, contactos, teclado y head,
un solo sistema, copy y enlaces, velocidad, 820, 768, 390 y 320 píxeles, y la
mirada final contra los marcos de figma.com y x.ai. Cada línea nombra sus
comprobaciones: los ids de `consistency.mjs` entre corchetes, los hallazgos de
`check.mjs` entre llaves y las filas de `perf.mjs`.

## Qué no hacer nunca

- Una tarjeta, fila o baldosa que aparece al hacer scroll; un fade-in en cada
  sección; parallax en texto; scroll-jacking; parpadeos aleatorios.
- Fotografías de stock pasadas por producto, gente o lugar del cliente (una de
  sustitución se lista en el informe como tal, nunca se muestra con el nombre
  o el logo de otro fabricante); una página de producto que nunca muestra el
  producto.
- Un parecido dibujado de un logo real; reseñas, citas, clientes o cifras
  inventadas.
- Violeta o lavanda en el diseño propio de la página: acento, fondo, degradado,
  color de efecto o tinte. Un logo real de terceros conserva sus colores.
- Copiar el código, el copy, las imágenes o el efecto distintivo de un sitio
  de referencia.
- Borrar o editar los archivos del kit (`assets/`, `scripts/`) para limpiar una
  comprobación: una comprobación que señala un archivo del kit se informa, y
  la página se vuelve a comprobar después de cualquier cambio.

## Referencias

Todas en `references/`; la sección 3 de `SKILL.md` nombra la que necesita
cada familia de recursos. La biblioteca de paletas y tipografías está en
`library/` (`palettes.json`, `type.json`). Los scripts de verificación están
en `scripts/` y el kit de componentes en `assets/`.
