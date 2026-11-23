#!/usr/bin/env python3
"""Busca logos oficiales por nombre en las fuentes recomendadas.

  python3 scripts/buscar_logos.py "Next.js" [--descargar]

Sin --descargar solo lista candidatos. Con --descargar guarda el mejor en
assets/cache/logos/ tras pasarlo por validar_svg.py (si falla, prueba el
siguiente candidato).

Fuentes: Simple Icons CDN -> Devicon -> gilbarbara/logos.
"""
import argparse, json, os, re, sys
import requests

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE = os.path.join(BASE, "assets", "cache", "logos")
sys.path.insert(0, os.path.join(BASE, "scripts"))
from validar_svg import validar_svg

SESSION = requests.Session()
SESSION.headers.update({"User-Agent": "stack-architect/1.0"})

# Nombres complicados -> slug por fuente. Se amplía con el uso.
INDICE_CURADO = {
    "next.js": {"simpleicons": "nextdotjs"},
    "nextjs": {"simpleicons": "nextdotjs"},
    "google books": {"simpleicons": "google"},
    "claude": {"simpleicons": "anthropic"},
    "postgres": {"simpleicons": "postgresql", "devicon": "postgresql"},
    "postgresql": {"simpleicons": "postgresql", "devicon": "postgresql"},
    "aws": {"simpleicons": "amazonaws"},
    "gcp": {"simpleicons": "googlecloud"},
    "github actions": {"simpleicons": "githubactions"},
}


def normalizar(q):
    return re.sub(r"[^a-z0-9]", "", q.lower())


def variantes_slug(q):
    n = normalizar(q)
    yield n
    yield q.lower().replace(" ", "").replace(".", "").replace("-", "")
    yield q.lower().replace(" ", "-")


def sondear_svgl(slug):
    """svgl.app: marcas oficiales. Solo coincidencia exacta de título."""
    from urllib.parse import quote
    queries = [slug, re.sub(r"[-_.]+", " ", slug).strip()]
    targets = {normalizar(slug)}
    for q in dict.fromkeys(queries):
        r = SESSION.get(f"https://api.svgl.app?search={quote(q)}", timeout=20)
        r.raise_for_status()
        items = r.json()
        if not isinstance(items, list):
            continue
        for it in items:
            if normalizar(it.get("title", "")) in targets:
                route = it.get("route")
                url = route.get("light") or route.get("dark") if isinstance(route, dict) else route
                if not url:
                    continue
                svg = SESSION.get(url, timeout=20).text
                if "<svg" not in svg[:2000]:
                    continue
                return ("svgl", slug, url, svg)
    raise ValueError("no encontrado")


def sondear_simpleicons(slug):
    url = f"https://cdn.simpleicons.org/{slug}"
    r = SESSION.get(url, timeout=20)
    r.raise_for_status()
    return ("simpleicons", slug, url, r.text)


def sondear_devicon(slug):
    for variant in ("original", "plain"):
        url = (f"https://raw.githubusercontent.com/devicons/devicon/master/"
               f"icons/{slug}/{slug}-{variant}.svg")
        r = SESSION.get(url, timeout=20)
        if r.status_code == 200 and "<svg" in r.text[:2000]:
            return ("devicon", slug, url, r.text)
    raise ValueError("no encontrado")


def sondear_gilbarbara(slug):
    url = f"https://raw.githubusercontent.com/gilbarbara/logos/main/logos/{slug}.svg"
    r = SESSION.get(url, timeout=20)
    r.raise_for_status()
    return ("gilbarbara", slug, url, r.text)


def buscar(query, descargar=False, timeout_por_fuente=3):
    qn = query.lower().strip()
    candidatos = []
    vistos = set()

    # 1. índice curado
    for slug in INDICE_CURADO.get(qn, {}).values():
        if slug not in vistos:
            vistos.add(slug)
            candidatos.append(("indice", slug))

    # 2. variantes del nombre
    for v in variantes_slug(query):
        if v and v not in vistos:
            vistos.add(v)
            candidatos.append(("variante", v))

    resultados = []
    for origen, slug in candidatos:
        for nombre, fn in (("svgl", sondear_svgl),
                           ("simpleicons", sondear_simpleicons),
                           ("devicon", sondear_devicon),
                           ("gilbarbara", sondear_gilbarbara)):
            try:
                fuente, s, url, svg = fn(slug)
                ok, motivo = validar_svg(svg)
                resultados.append({"query": query, "fuente": fuente,
                                   "slug": s, "url": url,
                                   "seguro": ok, "motivo": motivo})
                if ok:
                    if descargar:
                        os.makedirs(CACHE, exist_ok=True)
                        p = os.path.join(CACHE, f"{s}.svg")
                        with open(p, "w", encoding="utf-8") as fh:
                            fh.write(svg)
                        print(f"guardado: {p}")
                    return resultados
                # inseguro: sigue a la siguiente fuente
            except Exception:
                continue
    return resultados


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("query", help='nombre de la marca, ej. "Next.js"')
    ap.add_argument("--descargar", action="store_true",
                    help="guardar el primer candidato seguro en caché")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    res = buscar(a.query, descargar=a.descargar)
    if a.json:
        print(json.dumps(res, indent=2))
        return
    if not res:
        print(f"sin resultados para '{a.query}'")
        return
    for r in res:
        marca = "✓" if r["seguro"] else "✗"
        print(f"{marca} [{r['fuente']}] {r['slug']}: {r['motivo']}\n    {r['url']}")


if __name__ == "__main__":
    main()
