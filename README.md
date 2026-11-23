# wekyt/skills

Colección de skills mejoradas para agentes de IA, instalables desde el hub
wekyt. Skills con prueba: nadie cita un repo de promesas, se cita el repo
donde cada skill muestra que funciona. Cada skill lleva su demo visible
(GIF de antes/después con artefactos reales), su badge de prueba y su tabla
de antes/después. Si una skill aún no tiene video publicado, su README lo
dice ("En prueba", "Short en producción") y no inventa el badge.

## Skills

| Skill | Qué hace | Versión | Licencia |
|---|---|---|---|
| [unslop](unslop/) | Quita lo genérico de una UI y le da carácter propio, en 9 pasadas. Incluye reglas de póster y miniatura y lista rápida de auditoría. | 1.0.0 | CC BY 4.0 (heydamir) |
| [taste-skill](taste-skill/) | Frontend anti-slop al nivel de figma.com y x.ai, con verificador y puerta de acabado en navegador real. Adaptada a Next.js y a parluu.com. | 2.5.1-wekyt.1 | MIT (Leonxlnx) |
| [desarma-video](desarma-video/) | Desarma un video de referencia para hacer uno original en el mismo formato: cortes, ritmo, cuadros, transcripción, plan de remake. | 1.0.0 | MIT |
| [stack-architect](stack-architect/) | Diagramas de arquitectura con logos oficiales, en HTML autocontenido claro/oscuro, con validación de cada SVG antes de cachearlo. | 1.0.0 | MIT |
| [analisis-studio](analisis-studio/) | Análisis diario de YouTube Studio: mide cada video, guarda el historial en SQLite y escribe qué funcionó y qué ajustar. | 1.0.0 | MIT |
| [flujo-pr](flujo-pr/) | Rama, push, PR, verificación en GitHub y merge: un solo commit, un solo push, sin romper nada. | 1.0.0 | MIT |
| [respaldo](respaldo/) | Respaldo semanal en un solo comando: repo Git con escáner de secretos y copia de emergencia por correo. | 1.0.0 | MIT |

## Tabla de pruebas

Solo filas con datos reales verificados. "Referencia analizada" significa
que la skill se usó sobre ese video (que no es nuestro) para producir un
desarme; "Análisis" significa que la skill analizó ese video y escribió la
decisión con sus datos; "Short propio" significa un Short de Píldora Tech
producido con la skill.

| Skill | Video donde se usó | Vistas | Fecha |
|---|---|---|---|
| desarma-video | Referencia analizada: Anton, "6 plugins de Claude Code" (https://youtube.com/shorts/Q6y3h1OXBIs) | 5.232 | 22-nov-2026 |
| desarma-video | Referencia analizada: NoticiasDeIA, "LA IA QUE ROMPE GITHUB" (https://youtube.com/shorts/iYXJnTCCk_Y) | 2.565 | 22-nov-2026 |
| analisis-studio | Análisis: GTA VI, "GTA VI: $3.790 M en un día, récord del entretenimiento" (https://youtube.com/shorts/C59vRbUuqUY) | 1.026 | 22-nov-2026 |
| analisis-studio | Análisis: Gemini Mac, "Gemini ya maneja tu Mac por vos: solo en EE. UU." (https://youtube.com/shorts/95U-eTavgzg) | 63 | 22-nov-2026 |

unslop y taste-skill aún no tienen fila: su prueba en Píldora Tech está
pendiente. unslop se usó en la auditoría de parluu.com (2-nov, solo lectura,
sin rediseño publicado). taste-skill se revisó el 21-nov y no ha corrido sobre
ninguna página real todavía. stack-architect, flujo-pr y respaldo tampoco
tienen fila: su prueba está en sus propios README (corridas reales en repos
y sistemas, sin video).

## Instalación

Copia la carpeta de la skill a `~/.claude/skills/<nombre>` o al directorio de
skills de tu proyecto. Cada README de skill dice su nombre exacto de carpeta
y sus requisitos.

El comando `wekyt skill add` llegará después. Por ahora la instalación es
copiando la carpeta; no existe un instalador de skills en el hub.

## Cómo contribuir

1. Toma una skill que ya exista en otro repo, mejórala y súbela, o propón una
   nueva. La mejora tiene que ser concreta: una adaptación a un stack, una
   guía en español, reglas que ya estén escritas y probadas, no ideas sueltas.
2. Mantén la atribución y la licencia del original. Sin excepción.
3. Cada skill lleva demo visible: un GIF de 3 a 6 segundos en bucle con
   artefactos reales (antes/después o la skill en acción), nunca mockups
   inventados. Si el artefacto real aún no existe, el README lo marca como
   pendiente y dice qué falta.
4. Cada skill lleva su tabla de antes/después con números reales cuando
   existan (vistas, puntaje, tiempo). Nada de cifras inventadas.
5. Español primero en todo el texto visible. Cero guion largo en ningún texto:
   usa coma, dos puntos o punto.
6. Cada `SKILL.md` es autocontenida y usable sin contexto interno nuestro.
7. Abre un pull request con la skill, su README con demo, su `VERSION` y su
   `LICENSE`. No prometas funciones que no existen.

## Licencias

Cada skill trae su propia licencia en su carpeta: unslop es CC BY 4.0 con
atribución a Damir Sokolovsky (@heydamir); taste-skill es MIT con copyright de
Leonxlnx; desarma-video, stack-architect, analisis-studio, flujo-pr y
respaldo son MIT. La adaptación wekyt no cambia la licencia ni la autoría
de los originales.

---

# wekyt/skills

A collection of improved skills for AI agents, installable from the wekyt
hub. Skills with proof: nobody cites a repo of promises, you cite the repo
where each skill shows it works. Every skill ships a visible demo (a 3-6
second looping before/after GIF made from real artifacts), a test badge and a
before/after table. If a skill has no published video yet, its README says so
("En prueba", "Short en producción") and does not invent the badge.

## Skills

| Skill | What it does | Version | License |
|---|---|---|---|
| [unslop](unslop/) | Removes the generic AI look from a UI and gives it its own character, in 9 passes. Includes poster and thumbnail rules and a quick audit checklist. | 1.0.0 | CC BY 4.0 (heydamir) |
| [taste-skill](taste-skill/) | Anti-slop frontend at the figma.com and x.ai level, with a checker and finish gate in a real browser. Adapted to Next.js and parluu.com. | 2.5.1-wekyt.1 | MIT (Leonxlnx) |
| [desarma-video](desarma-video/) | Takes a reference video apart to make an original one in the same format: cuts, pace, frames, transcription, remake plan. | 1.0.0 | MIT |
| [stack-architect](stack-architect/) | Software architecture diagrams with official logos, in self-contained light/dark HTML, with validation of every SVG before caching. | 1.0.0 | MIT |
| [analisis-studio](analisis-studio/) | Daily YouTube Studio analysis: measures every video, stores history in SQLite, and writes what worked and what to adjust. | 1.0.0 | MIT |
| [flujo-pr](flujo-pr/) | Branch, push, PR, GitHub verification and merge: one commit, one push, without breaking anything. | 1.0.0 | MIT |
| [respaldo](respaldo/) | Weekly backup in one command: Git repo with a secret scanner plus an emergency email copy. | 1.0.0 | MIT |

## Test table

Only rows with real, verified data. "Reference analyzed" means the skill was
used on that video (not ours) to produce a teardown; "Analysis" means the
skill analyzed that video and wrote the decision with its data; "Own Short"
means a Píldora Tech Short produced with the skill.

| Skill | Video where it was used | Views | Date |
|---|---|---|---|
| desarma-video | Reference analyzed: Anton, "6 plugins de Claude Code" (https://youtube.com/shorts/Q6y3h1OXBIs) | 5,232 | Nov 22, 2026 |
| desarma-video | Reference analyzed: NoticiasDeIA, "LA IA QUE ROMPE GITHUB" (https://youtube.com/shorts/iYXJnTCCk_Y) | 2,565 | Nov 22, 2026 |
| analisis-studio | Analysis: GTA VI, "GTA VI: $3.790 M en un día, récord del entretenimiento" (https://youtube.com/shorts/C59vRbUuqUY) | 1,026 | Nov 22, 2026 |
| analisis-studio | Analysis: Gemini Mac, "Gemini ya maneja tu Mac por vos: solo en EE. UU." (https://youtube.com/shorts/95U-eTavgzg) | 63 | Nov 22, 2026 |

unslop and taste-skill have no rows yet: their Píldora Tech test is pending.
unslop was used in the parluu.com audit (Nov 2, read-only, no published
redesign). taste-skill was reviewed on Nov 21 and has not run on a real page
yet. stack-architect, flujo-pr and respaldo have no rows either: their proof
lives in their own READMEs (real runs on repos and systems, no video).

## Installation

Copy the skill folder to `~/.claude/skills/<name>` or your project's skills
directory. Each skill README states its exact folder name and requirements.

The `wekyt skill add` command is coming later. For now, installation is
copying the folder; there is no skill installer in the hub yet.

## Contributing

1. Take a skill from another repo, improve it and upload it, or propose a new
   one. The improvement must be concrete: an adaptation to a stack, a Spanish
   guide, rules already written and tested, not loose ideas.
2. Keep the original's attribution and license. No exceptions.
3. Every skill ships a visible demo: a 3-6 second looping GIF from real
   artifacts (before/after or the skill in action), never invented mockups. If
   the real artifact does not exist yet, the README marks it pending and says
   what is missing.
4. Every skill ships a before/after table with real numbers when they exist
   (views, score, time). No invented figures.
5. Spanish first in all visible text. No em dashes anywhere: use commas,
   colons or periods.
6. Every `SKILL.md` is self-contained and usable without our internal context.
7. Open a pull request with the skill, its README with demo, its `VERSION`
   and its `LICENSE`. Do not promise features that do not exist.

## Licenses

Each skill ships its own license in its folder: unslop is CC BY 4.0 with
attribution to Damir Sokolovsky (@heydamir); taste-skill is MIT, copyright
Leonxlnx; desarma-video, stack-architect, analisis-studio, flujo-pr and
respaldo are MIT. The wekyt adaptation does not change the originals'
license or authorship.
