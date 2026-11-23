# flujo-pr: Rama, push, PR, verificación y merge

Skill propia de wekyt (MIT). El flujo completo para llevar un cambio a
producción sin romper nada y sin pedir permiso a cada paso: rama feature,
un solo commit, un solo push, pull request, verificación del PR en GitHub
antes de avisar y merge con el modelo que toque. Nació en los repos de
parluu, wekyt/hub y linkedin-ai-plugin, donde corre desde oct-2026.

## Reglas

1. **Nada directo a main.** Todo cambio va en rama feature, con el estado
   limpio en un commit antes de empezar. La rama se basa en el main actual.
2. **Un solo commit, un solo push.** Agrupa todo el cambio en un commit y
   un push. Cada escritura por conector pide una aprobación: tres
   operaciones sueltas son tres tarjetas, una sola subida es una.
3. **El PR se valida en GitHub antes de avisar.** tsc, tests y build local
   NO sustituyen esta verificación. En la página del PR se confirman 3
   cosas: (1) el PR está ABIERTO (no mergeado ya); (2) el diff contiene
   exactamente los cambios esperados, ni más ni menos; (3) la rama está
   basada en el main actual.
4. **Quién mergea se define antes de empezar.** Hay dos modelos y no se
   mezclan: (a) el dueño del repo mergea (siempre merge commit, nunca
   squash ni rebase); (b) el agente mergea por navegador con la sesión
   guardada, sin tarjeta del conector. Lo que no se hace: mergear por
   conector cuando el flujo pide navegador, ni pedirle al dueño que mergee
   algo que el agente podía mergear.
5. **Puertas antes del PR:** tests + build en verde. Sin verde, no hay PR.
6. **Puertas después del merge:** producción en Ready sola + smoke en
   incógnito + revisión del log de errores + verificar el deploy. El testeo
   en vivo del dueño es la puerta final.
7. **"No dañes nada".** En un repo ajeno o en producción: auditoría
   primero, solo lectura, y dirección a aprobación antes de cualquier
   cambio. Un resumen en caché no es fuente de verdad sobre el estado de
   un PR: se verifica en GitHub, no en notas viejas.
8. **Lo que el conector no cubre, va por navegador.** Crear repos y
   archivos de workflow (`.github/workflows/*`) devuelve 403 por conector:
   se hacen por navegador con la sesión guardada. Lo mismo vale para
   releases y para cambios de configuración del repo.

## Flujo paso a paso

```text
1. main limpio -> git checkout -b feature/<nombre>
2. cambios -> tests + build en verde
3. UN commit -> UN push (por conector, una sola tarjeta)
4. crear el PR con título y descripción claros
5. validar en GitHub: abierto, diff exacto, base actual
6. avisar al dueño (o mergear por navegador, según el modelo)
7. post-merge: producción Ready + smoke + log de errores
```

## Qué no hacer

- No abras un PR con el build en rojo "para ver qué pasa".
- No avises "el PR está listo" sin haberlo abierto en GitHub.
- No hagas squash ni rebase si el repo acordó merge commit.
- No reintentes un push denegado en trabajo proactivo: el conector no
  pide tarjeta en ese contexto; el push queda para un turno pedido por el
  dueño.
- No toques `.github/workflows/*` por conector: 403 garantizado.
