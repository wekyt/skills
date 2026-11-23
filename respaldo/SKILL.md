# respaldo: Respaldo semanal de tu trabajo en un solo comando

Skill propia de wekyt (MIT). Un sistema de respaldo en dos vías: el repo
Git (fuente de verdad, con escaneo de secretos como puerta) y el correo
(copia de emergencia en ZIP). Nació para el harness de un asistente, donde
corre cada semana desde nov-2026.

## Reglas

1. **Secretos jamás, media jamás, nada mayor a 5 MB.** El escáner
   (`scripts/escanear-secretos.sh`) revisa lo stageado por nombre (`.env`,
   `.pem`, `credentials`, `id_rsa`…), por contenido (claves con pinta de
   `sk-`, `ghp_`, `AKIA`, `BEGIN PRIVATE KEY`…) y por tamaño (>5 MB). Si
   falla, el push ABORTA. Sin excepciones.
2. **Archivos grandes fuera del repo, en su lote.** Un archivo de notas
   de más de 5 MB no se fuerza al commit: lleva
   `git update-index --skip-worktree` (NO `assume-unchanged`: un
   `git reset` borra esa marca) y se pushea solo, en su propio lote.
3. **Un solo commit, un solo push.** Igual que en `flujo-pr`: agrupar
   escrituras es lo que evita una tarjeta de aprobación por operación.
4. **El push desde trabajo proactivo se deniega.** El conector no pide
   tarjeta en ese contexto: queda el commit local y el push se hace en un
   turno pedido por el dueño. No reintentes en loop.
5. **push-files solo acepta UTF-8.** Los binarios (fuentes, imágenes,
   video, ZIP) se filtran del push y se reinstalan desde su origen. El
   script ya los excluye.
6. **El correo tiene dos límites reales.** (a) Base64: el límite de 25 MB
   es del mensaje total, no del archivo; un ZIP de 21,4 MB son ~29 MB en
   base64 y el conector lo rechaza. La salida es armar el ZIP sin lo
   regenerable (HTML compilados, salidas de build): `git archive HEAD --
   ':!*.html'`. (b) Tipo de archivo: Gmail bloquea ZIPs que contienen
   ejecutables o scripts (`.py`, `.sh`, `.js`), aunque el tamaño entre.
   El ZIP del correo debe excluirlos: el código vive en GitHub una vez
   pusheado. Esta exclusión es la receta vigente y se verifica en la
   próxima corrida (dom 29-nov-2026): si ese envío llega, la receta queda
   confirmada. **Verifica siempre el rebote en Gmail antes de reportar
   "enviado": el send del conector devuelve éxito aunque Gmail lo rechace
   después.**

## Flujo

```bash
bash scripts/respaldo.sh   # sincroniza, stagea, escanea, commitea y pushea
```

El script sincroniza tus fuentes (edita `SOURCES` arriba del todo),
regenera el inventario si lo tienes, hace `git add -A`, corre el escáner
y, si está limpio, crea UN commit y UN push vía conector GitHub.

## Copia por correo (emergencia)

```bash
git archive HEAD -- ':!*.html' -- ':!*.py' -- ':!*.sh' -- ':!*.js' -o respaldo.zip
```

Solo texto y documentos: nada de ejecutables, nada regenerable. El cuerpo
del correo dice qué es, qué contiene y cómo restaurar. Si el ZIP pasa de
~18 MB en crudo, parte en dos o deja fuera más regenerable: en base64 no
entra.

## Demo

Demo pendiente. Falta una grabación de terminal de una corrida semanal real
(rsync, escaneo limpio, commit y push en un solo comando). Cuando exista,
este archivo muestra el GIF en bucle. No se usa mockup en su lugar.

## Verlo en video

Short en producción. La skill no ha producido todavía un Short de Píldora
Tech. Su prueba son las corridas semanales reales (ver Antes / después).

## Antes / después

**Corrida del 15-nov-2026.** ZIP por correo de 15,8 MB: llegó al inbox.
Respaldo completo en GitHub en el mismo lote.

**Corrida del 22-nov-2026 (23-nov 11:36).** El escáner abortó el push con
4 hallazgos: `memory/bank/reflections.md` con 6.226.353 bytes (>5 MB) y 3
archivos de un scratch de grabación con contenido con pinta de clave. Se
arregló con `.gitignore` para el scratch y `skip-worktree` para el archivo
grande; el escáner quedó limpio y el commit local `e2dc7a6` se creó. El
push se denegó (trabajo proactivo, regla 4) y quedó pendiente. El ZIP por
correo se armó sin los HTML compilados: 17,1 MB (base64 ~22,8 MB, entra en
el límite). El send devolvió éxito, pero Gmail lo rebotó el mismo minuto
por tipo de archivo (el ZIP llevaba `.py`, `.sh` y `.js`). Lección que
quedó escrita en la regla 6: el ZIP del correo excluye scripts, y el
rebote se verifica antes de reportar. El respaldo quedó a salvo como
commit local.

**Lo que la skill no hace:** no respalda secretos ni media; no promete
que el correo llegue sin verificar el rebote; no reintenta un push
denegado.

## Instalación

Copia esta carpeta a `~/.claude/skills/respaldo` o al directorio de skills
de tu proyecto. Necesita `git`, `rsync` y `bash`. Edita `REPO` y `SOURCES`
arriba de `scripts/respaldo.sh` antes de la primera corrida. El comando
`wekyt skill add` llegará después; por ahora la instalación es copiando la
carpeta.

## Estructura

- `SKILL.md`: la skill completa.
- `scripts/respaldo.sh`: el comando único de respaldo.
- `scripts/escanear-secretos.sh`: la puerta de secretos.

## Licencia

MIT (ver `LICENSE`). Versión `1.0.0` (ver `VERSION`).

---

# respaldo

**In testing**

A weekly backup system in one command: a Git repo (source of truth, with a
secret scanner as a gate) plus an email copy (emergency ZIP). Built for an
assistant's harness, running weekly since Nov 2026.

Demo GIF pending: it needs a terminal recording of a real weekly run (rsync,
clean scan, one commit, one push). No Píldora Tech Short has been produced
with this skill yet; its proof is the real weekly runs: Nov 15, 2026, 15.8 MB
email backup delivered; Nov 23, 2026, the scanner stopped the push with 4
findings (fixed with .gitignore and skip-worktree), the 17.1 MB email ZIP
was sent but bounced on file type (scripts inside the ZIP), which is now
rule 6 of the skill.

Install: copy this folder to `~/.claude/skills/respaldo` or your project's
skills directory. Requires git, rsync and bash. Edit `REPO` and `SOURCES` at
the top of `scripts/respaldo.sh` before the first run. MIT license, version
`1.0.0`.
