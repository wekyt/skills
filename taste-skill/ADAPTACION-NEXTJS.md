# Adaptación Next.js

Cómo se usa taste-skill dentro de un proyecto Next.js, como parluu.com. Esto
es una adaptación de la corrida de `SKILL.md`, sección 4, no un reemplazo: la
skill manda, y lo que sigue traduce sus pasos al stack Next.js.

## El kit dentro de Next.js

Un proyecto existente construye con su propio stack. Los componentes toman el
marcado y las clases del starter, con el kit copiado en la carpeta pública y
cargado desde ahí como archivos planos.

En un proyecto Next.js eso significa:

- Primero trae los assets según `GUIA.md`, sección Assets: sin esa carpeta
  no hay kit que copiar a `public/assets`.
- Copia `<skill>/assets` a `public/assets`. El `system.css` y el `system.js`
  del kit se cargan desde ahí como archivos planos, no se importan como
  módulos del proyecto.
- Los componentes de React toman el marcado y las clases de `starter.html` y
  de los fragmentos de `assets/ui/<nombre>/fragment.html`. Se reescriben cada
  nombre, número y logo con los del cliente, como dice la skill.
- Un efecto, objeto, momento o escena se monta exactamente como dice su
  referencia, nunca con un script propio. Los `fx-*` de `assets/components`
  se montan como HTML, CSS y JS planos dentro de la página, no se
  reescriben como componentes React.
- Nunca se editan los archivos del kit (`assets/`, `scripts/`) para limpiar
  una comprobación. Una comprobación que señala un archivo del kit se
  informa, y la página se vuelve a comprobar después de cualquier cambio.

## Exportación estática para la puerta

Un brief que pide Next.js construye una exportación estática
(`output: 'export'`) y se revisa sobre la página construida (`--root out`).

La puerta de acabado se arma contra la página que un navegador puede abrir:

```bash
node <skill>/scripts/gate.mjs --start out/index.html --root out --kind software --category "<qué se vende>" --primary "<acción principal>"
```

O contra el servidor de desarrollo, con su URL en lugar de la página:

```bash
node <skill>/scripts/gate.mjs --start http://localhost:3000/ --kind software --category "<qué se vende>" --primary "<acción principal>"
```

Reconstruye antes de cada corrida de la puerta. Un build de framework nombra
la URL de su servidor de desarrollo o su página construida en lugar de
`index.html`.

## Las comprobaciones en Next.js

La misma secuencia que en la skill, con la página construida como objetivo:

```bash
node <skill>/scripts/copy-lint.mjs out/index.html --kind software
node <skill>/scripts/consistency.mjs out/index.html --widths 1440,1024,820,768,390 --rhythm-widths 1440,820,768,390 --profile .taste-skill/chrome-check --page software --category "<qué se vende>" --primary "<acción principal>"
node <skill>/assets/layout/check.mjs --url out/index.html --root out --profile .taste-skill/chrome-check --sizes 1440x900,1024x768,820x1180,768x1024,390x844 --shots shots/layout
node <skill>/scripts/shoot.mjs --url out/index.html --root out --w 1440 --out shots/1440.png --profile .taste-skill/chrome-check
node <skill>/scripts/perf.mjs out/index.html --root out --profile .taste-skill/chrome-check
node <skill>/scripts/gate.mjs out/index.html --root out
```

Cada script abre un Chrome headless con WebGL por CPU, uno a la vez, en
primer plano, con un tiempo límite de 10 minutos. Nunca en segundo plano,
nunca en un navegador con ventana, nunca con una herramienta de navegador.

`--profile` es el perfil de Chrome: una carpeta propia en la carpeta temporal
del sistema o en la carpeta `.taste-skill` del proyecto
(`.taste-skill/chrome-check`), nunca fuera del proyecto.

## El copy en español

La skill se escribió para copy en inglés y su `copy-lint.mjs` trae una lista
de palabras de relleno en inglés. En una página en español esa lista no cubre
las palabras de relleno en español, así que el copy en español se revisa a
mano con las mismas ideas: nada de "revolucionario", "mágico", "desbloquea",
"sin fricción", "potenciado por IA" en todo, ni de cifras que no se puedan
comprobar. Un dato que no se puede comprobar se vuelve discreto y específico
si el usuario confirma que es real, y se quita en caso contrario.

## Lo que la skill no cambia

La skill pule la página. No cambia el stack, no cambia el modelo de datos,
no toca la base de datos, no toca la autenticación ni los pagos, y no publica
nada por sí sola. Cada cambio que propone se entrega como código para revisar,
y en un proyecto con flujo de ramas y pull requests ese flujo manda sobre la
skill.
