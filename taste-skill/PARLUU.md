# Notas de pulido para parluu.com

Cómo se aplica taste-skill a parluu.com. Son notas de trabajo, no un cambio
aplicado: cada propuesta se entrega como código para revisar, y en parluu el
flujo manda (rama, push, pull request, merge por el dueño del repo). La skill
no publica nada por sí sola y no toca la base de datos, la autenticación ni
los pagos.

## El producto

parluu.com es una recomendación de libros por historial, gratis: el usuario
elige 2 libros y Claude regala el tercero. Stack: Next.js 14 con Supabase
(proyecto `tus3libros`), Resend, Turnstile y un límite de 3 análisis por día
por IP. Paleta de marca: crema, naranja y carbón. Antes de aplicar cualquier
nota, verifica en el repo los valores exactos (los tokens de la paleta, los
límites y los textos actuales de la página), porque la página cambia y estas
notas describen el estado conocido, no el estado verificado hoy.

## El tipo

parluu.com es **software**: una app que vende un servicio. Tipo de página
`software`, `site-kind` `software`. La acción principal es la recomendación:
el formulario que pide los 2 libros y la página de resultado con los 3 libros
y sus motivos.

## Los colores son de marca, no se reparten

La paleta crema, naranja y carbón es la marca real del producto. Los colores
propios del cliente van por `start.mjs brand` en lugar de repartir una paleta
(`sections.md`, sección 4, Look). Nunca violeta: la skill lo prohíbe en el
diseño propio de la página. Si la paleta del repo trae valores distintos a los
anotados aquí, mandan los del repo.

## La UI real es el resultado

La página de resultado, con los 3 libros recomendados y sus motivos, es el
`app-frame` del producto: la UI real mostrando aquello en lo que trabaja. Se
muestra real, con datos plausibles, nunca un dashboard genérico ni solo
fragmentos en paneles. El hero no lleva una imagen decorativa en lugar del
producto: el producto es la recomendación misma.

## El copy

La página está en español. El h1 nombra la categoría y el comprador, la
primera pantalla lleva un dato duro, y cada botón es un verbo y un objeto. La
lista de palabras de relleno de `copy-lint.mjs` es en inglés y no cubre el
español, así que el copy en español se revisa a mano con las mismas ideas:
nada de "revolucionario", "mágico", "desbloquea" ni "potenciado por IA" en
todo. Las cifras que se muestren (límite de análisis, precio, cantidad de
libros) tienen que ser las reales del repo y del producto, no inventadas. Un
dato que no se puede comprobar se vuelve discreto y específico si el dueño
confirma que es real, y se quita en caso contrario.

## La puerta en parluu.com

La puerta se corre contra la exportación estática o contra el servidor de
desarrollo, con reconstrucción antes de cada corrida. Ver
`ADAPTACION-NEXTJS.md` para los comandos. Un FAIL que se juzgue falso se
dispensa en `.taste-skill/waivers.json` con su motivo, nunca se arregla
engañando a la comprobación. La línea `GATE:` va primero en el informe, con
cada dispensa y cada FAIL abierto.

## Qué revisar primero

Estas son las comprobaciones que más suelen fallar en una página de este tipo,
según el checklist de la skill:

- **Primera pantalla:** dice qué se vende y para quién, con un dato duro, y
  el hero la llena solo a cada ancho, con su botón principal dentro.
- **Una sección por pantalla:** cada sección una o dos pantallas, su h2
  primero y arriba, sin que asome la sección vecina.
- **Bordes iguales:** cada bloque sobre las líneas de `.wrap`, nada cargado
  hacia un lado, nada de scroll lateral.
- **Cada visual se dibuja** a 1440, 1024, 768 y 390. Las portadas de los
  libros son contenido real del producto, no decoración: si una portada falta,
  el marco no queda vacío ni con una nota de muestra.
- **Nada de pies de foto** que expliquen o se disculpen por una imagen; los
  créditos van en una sola línea del pie.
- **Un solo sistema:** un par de botones, un estilo de tarjeta, una escala de
  radios, un aspecto de enlace.
- **Formularios:** cada campo con su etiqueta visible, cada error debajo de su
  propio campo, y la confirmación solo después de un envío real. El límite de
  3 análisis por día por IP es un dato real del producto: si se muestra, se
  muestra con su número exacto y verificado en el repo.
