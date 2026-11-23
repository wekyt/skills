# flujo-pr

**En prueba**

Rama, push, PR, verificación y merge sin romper nada y sin pedir permiso a
cada paso: un solo commit, un solo push, el PR validado en GitHub antes de
avisar y el merge con el modelo que toque (lo mergea el dueño o lo mergea el
agente por navegador).

## Demo

Demo pendiente. Falta una grabación de pantalla de una validación real de PR
en GitHub (abrir el PR, comprobar que está abierto, revisar el diff exacto
y confirmar la base actual). Cuando exista, este archivo muestra el GIF en
bucle. No se usa mockup en su lugar.

## Verlo en video

Short en producción. La skill no ha producido todavía un Short de Píldora
Tech. Su prueba son los PRs reales que pasaron por este flujo (ver Antes /
después).

## Antes / después

**PR #144, parluu (repo privado Zitr0/parluu).** "Quitar botón Librería
Nacional de /resultado". El PR fue mergeado por el dueño el 2026-11-08
11:37 UTC (head `bde414d0`, base main `8d248a07`). El 21-nov yo lo reporté
mal como pendiente, desde un resumen en caché. El 22-nov la regla 3 del
flujo (validar en GitHub, no en notas viejas) lo corrigió: mergeado, sin
nada pendiente ahí. Antes: un resumen viejo como fuente de verdad. Después:
GitHub como fuente de verdad.

**Release 0.4.0, wekyt/hub (22-nov-2026).** Push aprobado 09:17, commit
`882d41a0` ("Fix Windows handler spawn: extensionless npm shadows
npm.cmd"). Workflow run #12 en verde (tests en ubuntu y windows, publish
OK). npm latest pasó a 0.4.0 y el release v0.4.0 quedó publicado. Un solo
commit, un solo push, una sola tarjeta.

**linkedin-ai-plugin (18-nov-2026).** Repo privado creado y pusheado con
commit `ce421d42`, 5 skills, límite duro sin login ni cookies ni
automatización de publicación.

**Lo que el flujo evita:** avisar de un PR sin haberlo abierto en GitHub;
tres tarjetas de aprobación por tres escrituras sueltas; squash o rebase
donde se acordó merge commit; tocar workflows por conector (403).

## Instalación

Copia esta carpeta a `~/.claude/skills/flujo-pr` o al directorio de skills
de tu proyecto. No necesita dependencias: es un flujo de trabajo, no un
programa. El comando `wekyt skill add` llegará después; por ahora la
instalación es copiando la carpeta.

## Estructura

- `SKILL.md`: la skill completa.

## Licencia

MIT (ver `LICENSE`). Versión `1.0.0` (ver `VERSION`).

---

# flujo-pr

**In testing**

Branch, push, PR, verification and merge without breaking anything and
without asking permission at every step: one commit, one push, the PR
validated on GitHub before announcing it, and the merge with whichever model
applies (the owner merges, or the agent merges via browser).

Demo GIF pending: it needs a screen recording of a real PR validation on
GitHub (open the PR, confirm it is open, review the exact diff, confirm the
current base). No Píldora Tech Short has been produced with this skill yet;
its proof is the real PRs that went through this flow (parluu PR #144,
merged Nov 8, 2026; wekyt/hub 0.4.0, commit `882d41a0`, workflow run #12
green).

Install: copy this folder to `~/.claude/skills/flujo-pr` or your project's
skills directory. No dependencies: it is a workflow, not a program. MIT
license, version `1.0.0`.
