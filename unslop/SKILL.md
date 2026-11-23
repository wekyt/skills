---
name: unslop
description: Convierte una UI con aspecto de haber sido generada por IA en una interfaz diseñada con carácter propio. Encuentra una dirección en el producto mismo y después arregla el espaciado, el color, los iconos, el copy, la tipografía, el layout, los detalles, los visuales y el movimiento en ese orden, y puede generar un visual de hero real con una herramienta de imagen cuando hay una disponible. Se usa cuando el usuario pide quitarle lo genérico, pulir, limpiar o rediseñar una pantalla para que deje de verse generada por IA, o cuando una UI muestra los signos habituales, como degradados violetas, brillos, texto con degradado, etiquetas con emoji, insignias de "Nuevo ✨", manchas brillantes, etiquetas en mayúsculas con tracking, elementos que pulsan o espaciado irregular. Funciona en React, Tailwind, HTML y CSS, para dashboards, apps y landing pages. También audita pósters y miniaturas con las reglas de póster de la sección 10.
license: CC-BY-4.0
version: 1.0.0
metadata:
  author: Damir Sokolovsky
  x: https://x.com/heydamir
  site: https://heydamir.design/unslop
---

# Unslop

unslop fue creado por Damir Sokolovsky ([@heydamir](https://x.com/heydamir)),
quien empezó la serie Unslopping en X. Tiene licencia CC BY 4.0, así que
mantén este crédito en cualquier copia o adaptación. La versión en español es
una adaptación wekyt: el método y los valores son los del original; lo nuevo
es la sección 10 (pósters y miniaturas) y la lista rápida de auditoría en
[references/checklist-auditoria.md](references/checklist-auditoria.md). Los
archivos de referencia (`signs.md`, `tokens.md`, `visuals.md`, `refs.md`,
`effects.md`) se mantienen en su inglés original; los dos archivos nuevos
(`posters.md`, `checklist-auditoria.md`) están en español.

La UI hecha con vibecoding falla siempre de las mismas formas previsibles.
Cada superficie brilla, cada etiqueta lleva un emoji, el espaciado es lo que
el modelo escribió ese día y el copy grita. Quitar lo genérico arregla el
oficio y conserva el producto. Las funciones, el contenido y el orden de las
secciones se quedan. Lo que cambia es que cada tamaño, color, palabra e imagen
se vuelve deliberado.

Quitar lo genérico es solo la mitad del trabajo. Una pantalla limpia pero que
podría pertenecer a cualquier producto es la siguiente plantilla. Cada corrida
termina con una pantalla que solo podría tener este producto.

La diferencia entre lo genérico y el oficio está en dónde va la riqueza. Lo
genérico reparte color y efectos por el cromo: los fondos, los botones, los
bordes y las etiquetas. El oficio mantiene el cromo callado y pone la riqueza
en uno o dos momentos de contenido que la gente recuerda, como un objeto
renderizado, un gráfico bonito o una imagen del mundo del producto.

Trabaja como un diseñador haciendo una pasada de corrección, capa por capa, en
toda la pantalla.

## Cómo se ve el buen trabajo

- **Un elemento brillante.** Cada pantalla tiene una cosa pulida que lleva el
  color y el oficio, un objeto renderizado, una escena pintada o un gráfico
  rico. Todo alrededor está callado, así se lee al instante.
- **Cromo callado.** La navegación, los botones y el texto usan los neutros
  teñidos y un acento. Nada brilla, nada compite con el elemento brillante.
- **Una idea clara.** Se puede decir en una frase qué muestra el visual y por
  qué pertenece a este producto.
- **Texto sobre espacio en calma.** El titular va sobre la parte de la imagen
  o del layout que se dejó vacía para él, corto y específico, con una acción
  primaria y una secundaria y nada apilado debajo.
- **Producto real, material real.** Las vistas previas se ven como la app real
  con datos plausibles, y los objetos se ven como cosas reales con peso, luz
  y sombra.

Qué estilos visuales suelen funcionar y cuáles fallan está en
[references/visuals.md](references/visuals.md). Ejemplos terminados para
aprender de ellos están en [references/refs.md](references/refs.md), y
tratamientos de código como dibujar una imagen con glifos están en
[references/effects.md](references/effects.md).

## Cómo se usa

1. **Mira la pantalla.** Encuentra los archivos que la dibujan. Si puedes
   correr la app o abrir el archivo en un navegador y sacar una captura, hazlo,
   para juzgar lo que la gente ve y no solo el código.
   - ¿Solo un enlace a un sitio en vivo, sin código? Guarda la página con
     `node <carpeta de la skill>/scripts/snapshot.mjs <url> unslop/original.html`
     y trabaja sobre una copia de ese archivo. Añade `--dark` o `--light` para
     que coincida con el tema que ve el usuario. También guarda
     `original.live.png`, una captura de la página en vivo, así que dibuja la
     copia guardada y compara las dos antes de empezar. Los fondos animados
     dibujados por scripts no sobreviven, así que descríbelos en la auditoría
     desde la página en vivo.
   - ¿Solo una captura? Reconstruye la pantalla como un solo archivo HTML
     estático primero, igualándola de cerca, y trátala como la original.
   - En ambos casos el resultado es una página rediseñada en código que el
     usuario puede entregar a quien sea dueño del sitio real, así que dilo en
     el informe.
2. **Audita.** Recorre [references/signs.md](references/signs.md) y lista cada
   signo que encuentres, una línea por cada uno con el lugar donde vive.
3. **Decide cuánto cambiar.** Lee la auditoría con honestidad antes de planear
   nada.
   - **Mucho de lo genérico**, muchos signos en color, tipografía, iconos y
     copy. Corre el proceso completo de abajo.
   - **Poco de lo genérico**, una pantalla mayormente diseñada con unos pocos
     signos restantes. Modo pulido. Arregla solo lo que encontró la auditoría,
     toma la dirección de la marca que ya existe en lugar de inventar una
     nueva, y mantén la paleta, la tipografía, el layout y el visual. Las
     ideas grandes, como un momento que falta o una escena para el hero, van al
     informe como sugerencias, no como cambios.
   - **Nada de lo genérico.** Dilo con claridad y sugiere dos o tres
     refinamientos pequeños como mucho, con valores exactos. Aplícalos solo si
     el usuario está de acuerdo, y para ahí. Nunca cambies una buena pantalla
     solo para que se vea distinta.
4. **Fija la dirección y para.** Escribe las cinco líneas que se describen
   abajo. Muestra la auditoría y la dirección al usuario y espera su respuesta
   antes de editar, porque cambiar la dirección después significa rehacer todo.
   Si tienes una herramienta para preguntar al usuario, pregunta con ella; si
   no, pregunta en texto plano y para. Sáltate la espera solo cuando el usuario
   ya haya dicho que lo hagas sin más.
5. **Arregla en nueve pasadas, en orden.** Termina una pasada en toda la
   pantalla antes de empezar la siguiente. Cuando casi cada línea cambia,
   planea las pasadas en orden y después escribe la pantalla nueva de una vez,
   siempre que se aplique cada pasada. El espaciado va primero porque todo lo
   demás se lee distinto una vez que el ritmo está bien. El copy va antes que
   la tipografía y el layout porque la longitud del titular decide su tamaño y
   su lugar. Los visuales y el movimiento van al final porque deben encajar en
   una pantalla que ya funciona sin ellos.
6. **Comprueba.** Corre el checklist del final de este archivo, dibuja de nuevo
   y compara con la lista de la auditoría. Todo lo que siga en la lista se
   arregla.
7. **Informa** la dirección, unas líneas por pasada sobre qué cambió, y
   cualquier prompt de imagen que hayas escrito.
8. **Registra, cuando lo pidan o cuando el usuario quiera algo para compartir.**
   Construye el archivo de historia y dibuja el vídeo que se describe en
   [Vídeo de historia](#vídeo-de-historia). Si el usuario lo pide al empezar,
   escribe cada pasada en el archivo de historia a medida que avanzas.

Mantén la corrida rápida. Dibuja la pantalla para revisarla tres veces como
mucho. Cuando generes una imagen, empieza justo después de que se confirme la
dirección y sigue con las primeras pasadas mientras se genera, en lugar de
esperar.

Los valores exactos de cada pasada están en
[references/tokens.md](references/tokens.md).

## Dirección

Antes de tocar nada, escribe cinco líneas cortas. Derívalas de lo que la
página dice que hace el producto y para quién es. Nunca de lo que está de moda.

- **Producto.** Qué hace y para quién, en una frase llana.
- **Carácter.** Dos o tres palabras concretas, como `tranquilo, exacto, un
  poco cálido` o `rápido, técnico, juguetón`. Palabras como limpio, moderno,
  elegante, mínimo y premium no valen, porque describen cada plantilla.
- **Mundo.** El lugar o el material al que el producto pertenece de forma
  natural. Una app de notas vive cerca del papel y la tinta, una herramienta de
  monitoreo cerca de los instrumentos y los turnos de noche, una app de viajes
  cerca de los mapas y la luz de la ventana. Este mundo fija el tinte de los
  neutros, el acento y el visual.
- **Momentos.** Uno o dos lugares donde la pantalla se vuelve rica en color,
  material y detalle, elegidos entre lo que el producto muestra. Una tarjeta o
  un dispositivo renderizado dentro de la vista previa, un gráfico cuyos
  colores significan cada uno una serie, un objeto del mundo puesto junto al
  contenido. Escribe cuáles son.
- **Firma.** Un detalle pequeño que solo tendría este producto, usado con
  constancia. Un punto de estado vivo para una herramienta de monitoreo,
  teclas para una herramienta de desarrollo, subrayados dibujados a mano para
  una app de enseñanza, una línea de ruta para una app de reparto. Un detalle,
  no cinco.

Los ejemplos muestran solo la forma de una respuesta. Deriva la tuya del
producto que tienes delante, aunque un ejemplo encaje por casualidad.

Si el producto ya tiene una marca real, como un archivo de logo, un color o
una tipografía que no es de lo genérico, consérvala y construye la dirección
alrededor de ella. Un degradado de violeta a azul, destellos y brillo son de lo
genérico aunque estén en el logo, así que no cuentan como marca a menos que el
usuario lo diga.

## 1. Espaciado

- Todo va sobre una rejilla de 4 px. Los márgenes, los rellenos, los huecos y
  las alturas fijas son múltiplos de 4, así que 28 o 104 valen aunque no estén
  en la lista de tokens. Un paso de 2 px vale para ajustes dentro de controles
  pequeños, y un valor impar que centra algo exactamente se queda.
- Lo mismo, del mismo tamaño. Todas las filas de una lista comparten una
  altura y un hueco, todas las tarjetas de una fila comparten un relleno.
- El espacio muestra la agrupación. El espacio dentro de un grupo es menor que
  el espacio entre grupos, así una lista se lee como un bloque y las secciones
  se leen como separadas.
- Las cosas se alinean. Los iconos van en una columna, las etiquetas empiezan
  en una línea, los números se alinean a la derecha en una columna. Nada se
  empuja fuera de la línea con un translate perdido o un margen raro.
- El relleno sigue la densidad. Paneles compactos y barras laterales alrededor
  de 16, tarjetas de 20 a 24, bordes de página de 24 a 32.
- La navegación es la parte más densa de una app. Filas de 32 a 36 de alto con
  2 a 4 entre ellas, iconos en una columna, etiquetas en una línea. Una
  etiqueta de sección va más cerca de sus propios elementos que de la sección
  de arriba, como 24 arriba y 8 abajo. Mide la barra lateral después de la
  pasada, ahí es donde más se rompe el espaciado.
- Quita los valores únicos que rompen el ritmo, como `mt-[13px]` o `py-[11px]`,
  y reemplázalos con pasos de la escala.

## 2. Color

- Construye desde una sola rampa de neutros, teñida hacia el mundo de la
  dirección. Elige grafito, cálido o tinta de los tokens, o tiñe la tuya de la
  misma manera. El fondo, las superficies elevadas, los bordes y el texto
  salen todos de esa rampa.
- En apps y dashboards los fondos, las superficies, los bordes y el texto se
  mantienen neutros, la rampa de grafito o algo igual de gris. La gente los
  mira durante horas y el contenido tiene que llevar el color. Una pantalla
  cuyo fondo se lee naranja, marrón, azul o verde se ha pasado. El mundo se
  muestra en el acento, los gráficos y los momentos, no en las superficies.
  Las landing pages pueden teñir sus superficies más hacia el mundo.
- Tres roles de texto: primario, secundario y apagado. No diez lavandas apenas
  distintos.
- En el cromo, un acento, usado poco. Marca la acción primaria, la selección o
  el único número que importa.
- Los momentos de la dirección son la excepción. Dentro de ellos el color puede
  ser rico, varios tonos en un gráfico, un objeto renderizado con materiales
  reales, una imagen con su propia luz, siempre que se mantenga dentro del
  mundo y cada color signifique algo.
- Si la marca tiene un color real, se vuelve el acento y sale de las
  superficies. Si no hay color real de marca, toma el acento del mundo.
- El acento con texto encima llega a 4.5 a 1 de contraste. Si no llega, se
  oscurece o se pone texto oscuro encima. El acento usado como texto o tinta
  sobre una superficie clara necesita el mismo contraste, así que usa un tono
  más oscuro ahí.
- En temas oscuros el botón primario puede ser un blanco roto de la rampa con
  texto oscuro, y el acento puede vivir en un lugar más pequeño, como la
  selección o una cifra clave. Muchas veces se ve más deliberado que un botón
  de color.
- Los colores semánticos solo llevan significado, como verde para un cambio
  bueno y rojo para un error, y se atenúan para sentarse dentro de la paleta.
- Quita los degradados de tono en superficies, el texto con degradado, los
  brillos de color y las sombras de color, los lavados radiales de color y las
  manchas detrás del contenido, y los bordes neón.
- Los bordes son líneas finas y calladas, el color de texto de la rampa al 6 o
  10% de opacidad.
- En temas oscuros la profundidad viene de los pasos de superficie y las líneas
  finas, no de las sombras. Una ventana o un objeto flotando sobre una imagen
  puede mantener una sombra suave y neutra. En temas claros las sombras son
  neutras, suaves y pequeñas.
- Un degradado solo vale como un cambio pequeño de tono dentro de un neutro,
  como una fila activa que pasa de #2b2b2b a #1f1f1f. Nunca de un tono a otro.

## 3. Iconos

- Cada emoji usado como icono o como decoración en una etiqueta se vuelve un
  icono de línea de un solo conjunto. Usa el conjunto que el proyecto ya tiene;
  si no, lucide.
- Un tamaño y un grosor en todas partes, 16 o 18 px con un trazo de 1.5.
- Los iconos toman el color de su rol de texto, normalmente secundario o
  apagado. Nunca llevan sus propios colores.
- La caja del icono tiene el mismo ancho en cada fila y el hueco hasta la
  etiqueta es fijo, 8 o 10, así las etiquetas se alinean.
- Quita los iconos que no aportan nada, como un emoji en cada título de tarjeta
  o antes de cada etiqueta de sección. Las categorías que necesitan color
  llevan un punto pequeño de estado.

## 4. Copy

- Los titulares dicen qué hace el producto y para quién, en palabras llanas,
  así que no podrían encajar en otro producto. Usa los datos que ya están en la
  página y no inventes datos nuevos.
- Nada de signos de exclamación en el texto de la interfaz, y nunca `!!`.
- Nada de titulares de saludo como `Welcome back, Damir! 👋`. El título nombra
  el contexto, como el nombre de la página o el periodo, por ejemplo `Octubre
  2026`.
- Etiquetas cortas. `Buscar`, no `Buscar cualquier cosa...`.
- Un cambio dice con qué se compara, como `+12% frente al mes pasado` o `3
  menos que el mes pasado`.
- Los titulares, subtítulos, etiquetas, botones y pies terminan sin punto.
  Solo los párrafos de varias frases conservan sus puntos.
- Nada de palabras de bombo como supercharge, seamless, unlock, magic,
  revolutionize o game-changing, y nada de `AI-powered` en todo.
- Las afirmaciones que no se pueden comprobar, como `Lo quieren más de 10.000
  equipos` o `10x más rápido`, se vuelven calladas y específicas si el usuario
  confirma que son reales, y se quitan en caso contrario. Pregunta, y ponlas
  en el informe.
- Los datos de muestra se ven reales, con números y nombres plausibles, nunca
  `[X]` ni `123,456`.
- Las insignias como `PRO`, `Nuevo ✨` o `Beta 🚀` se van a menos que el
  producto las necesite de verdad, y entonces son texto callado.

## 5. Tipografía

- Elige la tipografía por el carácter de la dirección, entre las familias de
  los tokens. Mantén la fuente del proyecto cuando sea parte de una marca real.
  Una fuente por defecto como Inter que nadie eligió se puede cambiar cuando
  otra familia encaje mejor con el carácter. Una familia para la interfaz, más
  como mucho una compañera de cualquier fila de los tokens, una mono para
  cifras y meta o una display para titulares grandes.
- Unos pocos tamaños de una escala y dos pesos, 400 y 500, con 600 como mucho
  para un énfasis raro. Nada de títulos de 700 a 900, nada de texto con
  degradado.
- La jerarquía viene del tamaño y el color, no del peso.
- Mayúsculas de frase en todas partes. Etiquetas como `NAVEGACIÓN` o `PAGADO
  ESTE MES` con tracking ancho se vuelven `Navegación` y `Pagado este mes`.
- El texto pequeño nunca lleva tracking negativo. La legibilidad en texto
  pequeño significa más grande, un poco más grueso o un poco más suelto. El
  tracking ajustado es solo para texto display grande.
- Los números usan `tabular-nums` y un formato en toda la pantalla. Si una
  cifra es `$48,210`, la siguiente no es `$124,860.40`.
- Nada de cursiva para enfatizar.

## 6. Layout

- Mantén las secciones y su orden. Dentro de una sección, la alineación y las
  proporciones pueden cambiar cuando eso deje la pantalla más clara.
- Las apps y los dashboards mantienen proporciones reales de app. El marco
  llena el viewport, una barra lateral de 240 a 280 y contenido fluido,
  normalmente con un tope alrededor de 1440 a 1600 de ancho, y la página es
  tan larga como su contenido, con más secciones debajo de la primera pantalla.
  Nunca encojas una app en una columna estrecha y centrada. Si la original se
  dibujó como una ventana pequeña sobre un fondo, mantenla visiblemente como
  una ventana, con su marco y su fondo, y dale proporciones de escritorio
  dentro.
- El hero de landing más fuerte es una escena. Una imagen generada llena el
  hero de borde a borde, su sujeto va a un lado, y el titular va sobre la parte
  vacía y en calma de la misma imagen, con la vista del producto subiendo
  desde el borde inferior. Mira el hero en las referencias para verlo.
- Sin escena, usa una división asimétrica, texto a un lado y el visual con al
  menos la mitad del ancho, o texto sobre una vista grande del producto debajo.
  Todo apilado y centrado es el valor por defecto de la plantilla; consérvalo
  solo para un hero corto sin visual.
- En un hero de escena, el bloque de texto va en la parte superior, en el
  espacio entre la navegación y la parte alta de la vista del producto, en su
  centro óptico, un poco por encima del medio real.
- En una división, centra el bloque de texto en vertical contra el visual, así
  ningún lado deja una esquina grande y vacía. Si el visual es mucho más alto,
  acórtalo en lugar de empujar el texto hacia abajo. Las tarjetas y los
  dispositivos flotantes junto al texto son difíciles de equilibrar; prefiere
  un visual sólido. El token de espaciado de la navegación al titular se aplica
  a los heroes apilados; un hero dividido se centra.
- Los titulares largos se alinean a la izquierda. El texto centrado funciona
  para una o dos líneas cortas.
- Una acción primaria y como mucho una secundaria junto a ella. Cualquier otra
  cosa sale del hero.
- La navegación se mantiene callada. Logo, los enlaces que ya hay, un botón.
  Iniciar sesión es un enlace de texto callado junto a él, no un segundo botón.
  Un header flotante en forma de píldora no es obligatorio. En pantallas
  pequeñas los enlaces se pliegan en un botón de menú.
- Compón la primera pantalla como un todo. El hero llena la altura del viewport
  sin una banda vacía y muerta. Si el contenido es más corto, céntralo o deja
  que la vista del producto empiece baja y siga más allá del borde inferior,
  así la página invita a bajar.
- En pantallas pequeñas todo se apila en orden de lectura, el titular baja al
  tamaño móvil de los tokens y el visual viene después de las acciones. Una
  vista previa densa se simplifica en móvil, con menos filas y columnas, en
  lugar de reducirse con zoom. Ningún texto baja de 11 px.

## 7. Detalles

- Radios anidados. Un radio interior es igual al radio exterior menos el
  relleno entre ellos, nunca menos de 4. Controles de 8 a 10, tarjetas de 12 a
  16, paneles de 14 a 20. No todo es una píldora.
- Los conteos y la meta se vuelven texto callado, a menudo mono y apagado, en
  lugar de píldoras brillantes.
- Los atajos de teclado se vuelven teclas pequeñas.
- Los gráficos van sobre una rejilla apagada con etiquetas mono apagadas. Nada
  de barras arcoíris dentro de una serie, nada de barras brillantes, nada de
  etiquetas de día en mayúsculas. Si el gráfico es ruido de relleno,
  reemplázalo con datos que cuenten algo real.
- Los gráficos tienen jerarquía, como el texto. Un gráfico principal es
  claramente lo más grande de la pantalla, dibujado con cuidado, como líneas
  suaves o una comparación en espejo. Cualquier otra cosa que muestre datos es
  más pequeña y distinta en tipo, como una lista ordenada con barras finas o
  una tabla corta, nunca un segundo gráfico del mismo tamaño.
- Un acento por gráfico. Lo que importa, como el mes actual, la línea que se
  sigue o el plan que creció, lleva el acento, y todo lo demás va en pasos
  neutros de la rampa. Varios tonos solo cuando el gráfico tiene que distinguir
  series de verdad, y aun así uno manda y el resto son callados.
- Las tarjetas de estadísticas son números. Una etiqueta, una cifra grande y un
  cambio con aquello con lo que se compara. Nada de sparklines, conteos, mini
  barras o iconos añadidos para rellenarlas: se leen como decoración. Una
  tarjeta puede llevar un objeto de aspecto real cuando es justo aquello que su
  número cuenta, como un recibo pagado junto a los ingresos pagados o tarjetas
  bancarias junto al gasto. Usa tantas como tengan sentido para ese dashboard,
  siempre que cada una se lea sola y ninguna sea un mini gráfico.
- Varía los tamaños. Tarjetas de igual ancho lado a lado, cada una con el mismo
  tipo de contenido, se leen como plantilla. Dale ritmo a la rejilla, como tres
  o cuatro estadísticas compactas en una fila sobre un gráfico ancho, o un
  gráfico ancho junto a una lista estrecha.
- Elige el tipo de gráfico por los datos. Una tendencia es una línea, una
  comparación son barras, una parte es una barra apilada o una lista con
  barras, un solo objetivo es una barra de progreso.
- El estado activo es un paso pequeño de superficie con una línea fina de
  resalte, no un degradado con brillo.
- Los estados hover y focus existen y se mantienen dentro de la paleta. Un
  anillo de focus visible para quienes usan el teclado.
- El logo es el nombre del producto en la familia principal, más una marca
  simple si la hay. Nada de wordmark con degradado ni baldosa con destellos.
- El detalle de firma de la dirección aparece donde le toca y en ningún otro
  lugar.

## 8. Visuales

- El relleno decorativo se va. Las manchas brillantes, los orbes, las nebulosas,
  los cubos flotantes, las rejillas brillantes, los cerebros holográficos y los
  robots no dicen nada del producto.
- Un hero de landing lleva un visual que muestra algo verdadero.
- Los dashboards y las pantallas de app casi nunca necesitan imágenes
  generadas. Sus momentos vienen del producto mismo: un gráfico dibujado con
  cuidado, cifras bien compuestas, contenido real como fotos de producto o
  avatares, un estado que se siente vivo. Una cosa física con la que trata el
  producto, como una tarjeta de pago en una app de finanzas, suele quedar mejor
  construida en código con materiales reales, un degradado suave, un chip, un
  número.
- Genera imágenes para una app solo para estados vacíos, onboarding y momentos
  de marketing, o cuando el usuario lo pide.
- Con una herramienta de generación de imagen, la primera opción para un hero
  de landing es una escena del mundo de la dirección, generada lo bastante
  ancha como para ir detrás de todo el hero, con espacio vacío y en calma donde
  va el texto. Lleva el color y el ánimo, y el cromo se mantiene callado sobre
  ella.
- Debajo de la escena, o como visual cuando no hay herramienta, muestra el
  producto. Construye una vista previa en código de lo que la página ya
  promete, con los componentes del proyecto o HTML cuidadoso y datos
  plausibles, como la pantalla principal, una tarjeta clave o el resultado que
  produce el producto. Mostrar lo que el copy ya afirma no es inventar una
  función. En un hero de escena sube desde el borde inferior y sigue más allá.
- La vista del producto lleva un momento, no solo una tarjeta plana. Un objeto
  renderizado dentro de ella, como una tarjeta de pago sobre una cifra, un
  gráfico rico o un objeto pequeño del mundo. Son tipos de objetos, así que
  usar uno que encaje está bien.
- Antes de esta pasada, mira las referencias en
  [references/refs.md](references/refs.md). Toma cualidades de ellas, como la
  composición, la luz, la contención y cómo se coloca el momento, nunca su tema
  ni su layout.
- Los objetos y las escenas renderizados vienen de una herramienta de generación
  de imagen cuando la tienes. Si no la tienes, construye lo que puedas en
  código, escribe los prompts del resto y deja huecos vacíos del tamaño
  adecuado.
- Cómo elegir el tema, la receta del prompt y cómo colocar la imagen están en
  [references/visuals.md](references/visuals.md). Léelo antes de esta pasada.

## 9. Movimiento

- Quita el movimiento que se repite sin motivo, como `animate-pulse` o
  `animate-ping` en cosas que no están en vivo, el shimmer en titulares, los
  brillos que respiran, los elementos flotantes y el parallax.
- Quita `transition-all`, los muelles con rebote, el `hover:scale` en tarjetas
  y cualquier cosa que se mueva más de unos pocos píxeles al pasar el puntero.
- Mantén el movimiento que explica algo. Un hover es un cambio rápido de color
  o de superficie, una pulsación es una escala pequeña hacia abajo, un menú se
  desvanece y sube unos píxeles desde donde se abre, un número que cambia hace
  tween.
- Haz transición de color, fondo, borde, opacidad y transform, y nómbralos,
  como `transition-colors` o `transition-[transform,opacity]` en Tailwind, en
  lugar de un comodín. Nunca animes ancho, alto, top, left, márgenes ni
  desenfoques grandes: se entrecortan en dispositivos débiles.
- Una curva de easing y unas pocas duraciones en toda la pantalla, de los
  tokens. Corta para la respuesta, un poco más larga para las cosas que entran.
- Como mucho una entrada al cargar, un fade corto con subida para el contenido
  principal con un stagger pequeño. No cada tarjeta volando desde un lado
  distinto.

## 10. Pósters y miniaturas

Esta sección es de la adaptación wekyt, no del original. Aplica las reglas de
póster a cualquier pieza que tenga que llamar la atención en un feed: la
miniatura de un vídeo, la portada de un artículo, el hero de una landing con
imagen generada. El detalle está en
[references/posters.md](references/posters.md).

- **La pieza es un póster diseñado, no una captura.** Un frame real solo sirve
  si el sujeto mismo es el gancho, y aun así necesita diseño encima (texto con
  pegada, sujeto 3D, dispositivos de atención). La prueba del gate: ¿se ve como
  un póster diseñado o como una captura? Si se ve como captura, se descarta.
- **Una palabra héroe, no una frase.** El titular es de 2 a 4 palabras, una
  sola palabra clave gigante. Todo se entiende en menos de un segundo a unos
  120 px de ancho.
- **Una cifra siempre lleva su sustantivo.** Nunca una cifra sola: VISTAS,
  SUSCRIPTORES, LIBROS, DÍAS. Una cifra sin sustantivo no dice nada.
- **Fondo cinematográfico con profundidad.** Bokeh, haz de luz, viñeta, un
  entorno con aire. Nunca fondo blanco plano, nunca degradado plano, nunca
  fotos en cajitas con texto plano encima: eso se lee barato, como hecho en
  Paint.
- **Un solo sujeto focal.** Alto contraste, cero ruido, jerarquía clara de
  escala, separación entre sujeto y fondo. Los dispositivos de atención son
  flechas, comparaciones y un solo elemento que contrasta, no más texto.
- **Veraz con el contenido.** La pieza puede exagerar pero debe representar
  honestamente lo que hay detrás. Nada que el producto o el vídeo no cumpla,
  ningún dato, persona ni resultado inventado. Un antes y después en una sola
  escena continua es mentira: va en paneles o momentos separados.
- **Ortografía con lupa.** El titular se revisa palabra por palabra (tildes,
  concordancia) antes de componerlo. Un error en la pieza se ve en todo el
  feed.
- **Zona segura.** El texto héroe nunca va en el 15% inferior. La esquina
  inferior derecha es la zona del badge de duración: nada clave ahí.
- **El texto nunca se quema en la generación.** La imagen base se genera sin
  texto y el titular se compone por encima con tipografía real. El logo real
  va desde el archivo, nunca generado ni redibujado.
- **Variedad.** Si el concepto repite el de las 2 o 3 piezas anteriores, se
  descarta y se elige otro.

## Vídeo de historia

Un vídeo corto donde la pantalla se quita lo genérico paso a paso, con
redlines rojas sobre lo genérico. Mira
[refs/story-dashboard-frames.webp](references/refs/story-dashboard-frames.webp)
antes de construirlo: ocho frames de ese vídeo, en orden. Ese vídeo se hizo
viral, y así funciona:

- **Nada se cambia, todo se transforma.** Una página, y cada paso solo cambia
  CSS, así el relleno, los huecos, los tamaños, los colores, los radios y las
  sombras pasan del valor viejo al nuevo en su lugar. Se ve cómo se abre el
  espaciado, cómo se va el violeta, cómo se suavizan las esquinas.
- **Una ola.** Los elementos empiezan con unas decenas de milisegundos de
  diferencia desde arriba a la izquierda hacia abajo, así el cambio recorre la
  pantalla en lugar de que todo cambie a la vez.
- **El texto rueda.** El copy que cambia se desenfoca, y las palabras nuevas
  suben letra a letra.
- **Redlines primero.** Lo genérico lleva cajas de selección rojas con
  etiquetas, un paso de espaciado muestra medidas rojas que se vuelven blancas
  al arreglarse, un paso de detalles perfila las esquinas con su radio.
- **Corto y cerrado.** Cuadrado, recortado y cerca sobre la parte que más
  cambia, así se lee en un teléfono, y unos 10 segundos.

Añade unos minutos, así que hazlo solo cuando el usuario lo quiera.

1. **Un archivo de historia.** Construye `unslop-story/story.html`, una copia
   independiente de la pantalla original con sus estilos en el archivo. Mantén
   las reglas originales como están: son el paso 0.
2. **Pasos.** De tres a cinco, uniendo pasadas para que cada uno cambie algo
   que se vea, como `Espaciado`, `Color e iconos`, `Tipografía y copy`,
   `Detalles`. Un gráfico o visual nuevo va en el último paso. Ponlos en el
   head como `<meta name="unslop-steps" content="Espaciado, Color e iconos,
   Tipografía y copy, Detalles">`. Un nombre con Espaciado muestra medidas de
   espaciado, uno con Detalles muestra los perfiles de esquina.
3. **Cada paso es CSS encima.** Escribe los cambios del paso 1 bajo `.s1`, los
   del paso 2 bajo `.s2` y así, como `.s1 .card { padding: 24px }` o `.s2 body
   { background-color: #141415 }`. Las clases se suman, así el paso 3 sigue
   teniendo las reglas de los pasos 1 y 2. Cambia valores, nunca estructura,
   para que el navegador pueda hacer tween.
4. **Lo que no puede hacer tween, y cómo se trata.**
   - Degradados, brillos y lavados: ponlos en su propia capa y baja su
     `opacity` a 0, con el color sólido debajo cambiando. El texto con
     degradado va solo en el span `.from`, nunca en el swap ni en su padre,
     porque un clip de texto también atrapa el texto nuevo oculto.
   - Píldoras: escribe su radio como la mitad de la altura, como `23px`, no
     `9999px`, o la esquina solo cambia en el último frame.
   - Usa swaps con moderación, solo donde cambian las palabras, ocho como
     mucho en una historia. Veinte swaps desenfocándose a la vez se leen como
     un corte entre dos fotos, que es justo lo que el vídeo no debe parecer.
     Los cambios de peso, tamaño, tracking y color hacen tween solos, así que
     nunca necesitan un swap. Una familia de fuente nueva cambia directamente
     en su paso, sin swaps.
   - Texto que cambia, una familia de fuente nueva, un emoji que se vuelve
     icono: `<span class="swap" data-at="3"><span class="from">Welcome back,
     Damir! 👋</span><span class="to">Octubre 2026</span></span>`. En el paso
     3 la parte vieja se desenfoca y la nueva sube.
   - Emojis que se vuelven iconos: pon el icono nuevo junto al emoji dentro de
     la misma caja, los dos apilados en absoluto, y cruza sus `opacity` en el
     paso. Eso no es un swap y no cuenta para el límite.
   - Cosas que desaparecen, como una insignia `Nuevo ✨`: `data-out="2"` las
     pliega en el paso 2.
   - Cosas que aparecen, como una leyenda: `data-in="4"` las desvanece en el
     paso 4. Reserva su espacio para que nada salte.
5. **Redlines.** Las medidas siguen a los elementos en vivo, así sus números
   cuentan del valor viejo al nuevo mientras las cosas se mueven. Ese es el
   momento que la gente mira, así que elígelas bien.
   - `data-gap` va en los bloques de una pila vertical, como la fila de marca,
     la búsqueda, el grupo de navegación y el grupo de planes en una barra
     lateral, o el titular, la fila de estadísticas y el gráfico en la columna
     principal. No en cada fila, o la pantalla se llena de etiquetas diminutas
     de 2 px. Apunta a cuatro o seis huecos medidos por pila, y dale a cada
     pila su propio nombre si hay más de una, como `data-gap="sidebar"` y
     `data-gap="main"`.
   - `data-radius` va en dos a cuatro botones y tarjetas cuyas esquinas
     cambian.
   - `data-slop="Texto con degradado"` y así marca lo genérico para un primer
     momento corto, cinco como mucho, en los ejemplos más claros y separados
     entre sí, con etiquetas cortas. Es opcional: el vídeo de referencia no
     tiene ninguno.
6. **Solo la pantalla y su fondo.** El vídeo muestra la página de historia
   como es, sin ventana, borde ni sombra extra alrededor, así el propio fondo
   de la página llena el cuadro y la pantalla es la única caja. Si la pantalla
   va en una ventana que crece a proporciones de escritorio, ancla la ventana a
   la izquierda en la historia para que se ensanche hacia la derecha en lugar
   de deslizarse de lado. La página de historia se dibuja a 1440 de ancho y al
   menos 900 de alto, así que no dimensiones nada desde `100vh`, y mantén
   `position: fixed` solo para las capas de fondo.
7. **Cámara.** `<meta name="unslop-frame" content="0 0 960">` fija qué parte de
   la página llena el cuadro, como x, y y ancho en píxeles de página. Apunta x
   e y a la esquina superior izquierda de la propia pantalla, así el cuadro
   empieza con el fondo de la página alrededor, y recorta cerca sobre el lugar
   donde ocurre el cambio más visible, normalmente la barra lateral o el
   titular y las primeras tarjetas.
8. **Dibujo.** `node <carpeta de la skill>/scripts/story.mjs
   unslop-story/story.html unslop-story.mp4`, cuadrado por defecto, `--wide`
   para 16:9. Necesita Playwright y ffmpeg, así que si falta alguno, dile al
   usuario el comando que lo instala. Para verlo en vivo primero, córrelo con
   `--play` en lugar de la ruta de salida, y se repite en una ventana del
   navegador hasta cerrarlo. Saca unos frames con ffmpeg y míralos antes de
   entregarlo. Revisar el archivo de historia y el vídeo no cuenta para el
   límite de dibujos de una corrida.
9. **El archivo de historia es una pieza de presentación.** El resultado limpio
   se entrega como código normal en el stack del proyecto, sin clases `.s` ni
   atributos de historia. Cada vídeo lleva un crédito pequeño `unslop by
   @heydamir`, como pide la licencia.

## No hacer

- No renombres el producto, aunque el nombre tenga IA. Mantén un logo real
  como está. Cuando el propio logo es de lo genérico, como un emoji o un
  destello en una baldosa con degradado, redibújalo plano: solo el wordmark en
  la tipografía nueva, o un glifo simple de la idea del producto en un color
  sólido. Nunca una bola brillante o con degradado, un brillo o una baldosa con
  degradado: eso se lee como IA a primera vista.
- No cambies lo que el producto es. Mantén sus funciones, su contenido y el
  orden de las secciones a menos que el usuario pida más. El contenido de
  relleno que no significa nada se puede reemplazar con contenido que sí lo
  haga.
- No reemplaces la decoración quitada con decoración nueva, y no cambies una
  tendencia por otra, como cristal, grano, ruido, neón o rejillas bento.
- No inventes funciones, afirmaciones ni datos.
- No caigas en el mismo aspecto para cada producto. La dirección decide el
  tinte de la paleta, la tipografía y el visual, no la costumbre.

## Checklist

- [ ] La dirección está escrita y cada pasada la sigue
- [ ] Cada valor de espaciado está en la escala de 4 px y las cosas iguales
  tienen tamaños iguales
- [ ] Los iconos, las etiquetas y los números van cada uno en una columna
  alineada
- [ ] Una rampa de neutros teñida, tres roles de texto, un acento con contraste
  suficiente
- [ ] Nada de degradados de tono, texto con degradado, brillos, sombras de
  color ni manchas de color
- [ ] Nada de emoji en la interfaz
- [ ] Un conjunto de iconos con un tamaño y un grosor
- [ ] Tipografía elegida por el carácter, pesos de 400 a 600, nada de etiquetas
  en mayúsculas con tracking, nada de cursiva, nada de tracking negativo en
  texto pequeño
- [ ] Nada de signos de exclamación, nada de puntos finales en textos cortos,
  nada de titular de saludo, nada de afirmaciones sin verificar
- [ ] Los números en un formato con cifras tabulares
- [ ] Los radios anidados suman
- [ ] Un hero tiene un visual real o una vista previa del producto con al menos
  un momento, nunca relleno y nunca un marcador con etiqueta
- [ ] La primera pantalla está compuesta como un todo, sin banda vacía y muerta
- [ ] Nada de movimiento en bucle ni con rebote, una curva de easing, nada de
  propiedades de layout animadas
- [ ] Póster (sección 10): una palabra héroe de 2 a 4 palabras, una cifra con
  su sustantivo, fondo con profundidad (nunca blanco plano), un solo sujeto
  focal, veraz con el contenido, ortografía revisada, texto héroe fuera del
  15% inferior, nada clave en la esquina inferior derecha
- [ ] Prueba de plantilla. Si cambiaras el nombre del producto por el de otro
  producto, ¿la pantalla seguiría encajando? Si sí, empuja la dirección con más
  fuerza en el copy, el visual y el detalle de firma

## Archivos de referencia

- `references/signs.md`: los signos de lo genérico, para la auditoría.
- `references/tokens.md`: los valores exactos (escala de espaciado, rampas,
  tipografías, duraciones).
- `references/visuals.md`: qué estilos visuales funcionan y cuáles fallan, y
  la receta del prompt de imagen.
- `references/refs.md`: ejemplos terminados.
- `references/effects.md`: tratamientos de código, como dibujar una imagen
  con glifos.
- `references/posters.md` (español, añadido wekyt): las reglas de póster y
  miniatura de la sección 10.
- `references/checklist-auditoria.md` (español, añadido wekyt): la lista
  rápida de auditoría para una pasada de 5 minutos.
- `scripts/snapshot.mjs`: guarda una página en vivo como HTML para trabajar
  sobre ella.
- `scripts/story.mjs`: dibuja el vídeo de historia desde `story.html`.
