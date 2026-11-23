# Pósters y miniaturas

Reglas de póster para cualquier pieza que tenga que llamar la atención en un
feed: la miniatura de un vídeo, la portada de un artículo, el hero de una
landing con imagen generada. Son reglas generales, no de un canal concreto:
adáptalas a la marca del producto (su logo, su paleta, su mascota) y mantén el
resto.

## La prueba del póster

Una pieza es un póster diseñado, no una captura. Un frame real solo sirve si
el sujeto mismo es el gancho, y aun así necesita diseño encima (texto con
pegada, sujeto 3D, dispositivos de atención). La pregunta del gate: ¿se ve como
un póster diseñado o como una captura? Si se ve como captura, se descarta.

## Las reglas

1. **Una palabra héroe, no una frase.** El titular es de 2 a 4 palabras, con
   una sola palabra clave gigante. Todo se entiende en menos de un segundo a
   unos 120 px de ancho. Si hacen falta más palabras para explicarlo, el
   concepto está mal.
2. **Una cifra siempre lleva su sustantivo.** Nunca una cifra sola: VISTAS,
   SUSCRIPTORES, LIBROS, DÍAS, MINUTOS. Una cifra sin sustantivo no dice nada.
   La cifra tiene que ser real y verificada: nada de cifras inventadas.
3. **Fondo cinematográfico con profundidad.** Bokeh, haz de luz, viñeta, un
   entorno con aire. Nunca fondo blanco plano, nunca degradado plano, nunca
   fotos en cajitas con texto plano encima: eso se lee barato, como hecho en
   Paint.
4. **Un solo sujeto focal.** Alto contraste, cero ruido, jerarquía clara de
   escala, separación entre sujeto y fondo. Los dispositivos de atención son
   flechas, comparaciones y un solo elemento que contrasta, no más texto.
5. **La brecha de información.** La imagen plantea una pregunta que solo el
   contenido responde. Un solo sujeto focal, alto contraste, cero ruido. La
   plantilla es la marca; el contenido es lo que varía.
6. **Veraz con el contenido.** La pieza puede exagerar pero debe representar
   honestamente lo que hay detrás. Nada que el producto o el vídeo no cumpla,
   ningún dato, persona ni resultado inventado. Un antes y después en una sola
   escena continua es mentira: va en paneles o momentos separados.
7. **Ortografía con lupa.** El titular se revisa palabra por palabra (tildes,
   concordancia) antes de componerlo. Un error en la pieza se ve en todo el
   feed.
8. **Zona segura.** El texto héroe nunca va en el 15% inferior. La esquina
   inferior derecha es la zona del badge de duración: nada clave ahí. La regla
   de tercios ayuda: el 9:16 se divide en 9 cuadros y todo elemento clave vive
   en el cuadro central y sus alrededores, con aire arriba y abajo, nunca
   pegado a los bordes.
9. **El texto nunca se quema en la generación.** La imagen base se genera sin
   texto (`No text, no readable labels, no watermark`) y el titular se compone
   por encima con tipografía real. El logo real va desde el archivo, nunca
   generado ni redibujado. El titular nunca cubre el sujeto.
10. **Variedad.** Si el concepto repite el de las 2 o 3 piezas anteriores, se
    descarta y se elige otro. Cada pieza lleva su propia paleta de acentos y su
    propio fondo: si todas se ven igual, se leen como plantilla.

## El concepto, antes de generar nada

1. Lee el contenido y anota: la promesa veraz en una frase, el elemento más
   sorprendente o contraintuitivo, y qué NO puede prometer la pieza.
2. Genera al menos 5 conceptos distintos. Un concepto puede combinar 2 ideas
   si la brecha se hace más fuerte sin saturar.
3. Elige el concepto con la brecha de información más fuerte: la imagen
   plantea una pregunta que solo el contenido responde, y se entiende en menos
   de un segundo a unos 120 px de ancho.

## Generación de la imagen base (sin texto)

Arma el prompt con el contrato en este orden (concreto y sensorial, menos de
unos 200 tokens; los negativos se formulan en positivo):

- **Marco:** póster de alto impacto, un solo cuadro unificado, sin pantalla
  dividida salvo que se pida.
- **Escena:** lo que muestra el contenido, exactamente.
- **Texto:** siempre sin texto, sin etiquetas legibles, sin marca de agua (el
  titular va por encima).
- **Sujeto:** grande, en primer plano, ocupando el 40-60% del cuadro, nítido.
- **Elementos clave:** solo los objetos que explican la brecha.
- **Lugar:** sitio, hora y atmósfera cuando importen.
- **Composición:** un héroe en un tercio de fuerza, jerarquía clara de escala,
  separación sujeto y fondo.
- **Fondo:** campo de color vivo de alto contraste (la paleta de la pieza) o
  entorno, viñeta suave.
- **Luz:** luz clave fuerte esculpiendo el sujeto, relleno suave, luz de
  contorno definida (el contorno puede llevar el color de acento).
- **Grado:** vívido, brillante, negros profundos, colores saturados, cohesivo.

## Gate post-render (antes de entregar)

Revisa cada variante a tamaño real y a unos 120 px de ancho:

1. ¿Se entiende en menos de un segundo a 120 px? Si no, se descarta.
2. ¿Hay texto espurio, marca de agua o glifo roto? Si lo hay, se regenera la
   base.
3. ¿El titular está exacto, carácter por carácter? Si no, se recompone.
4. ¿La pieza representa verazmente el contenido? Si promete algo que el
   contenido no cumple, se cambia el concepto.
5. ¿La paleta es la de la pieza y el concepto no repite los 2 o 3 anteriores?
   Si no, se cambia.
