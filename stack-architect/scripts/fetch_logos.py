#!/usr/bin/env python3
"""Descarga en cascada SVGs oficiales y los cachea en assets/cache/logos/.

Orden: caché local -> svgl (marcas oficiales) -> Simple Icons CDN ->
Devicon -> gilbarbara/logos -> Lucide (solo `lucide:<nombre>` explícito).
Los SVG originales NUNCA se alteran; todo lo descargado pasa por
validar_svg.py ANTES de cachearse.

El brand puede ser:
  "nextdotjs"            -> slug en la cascada
  "nextjs"               -> alias (ver BRAND_ALIASES)
  "logo=https://..."     -> URL explícita (el oficial que no está en fuentes)
  "lucide:database"      -> icono genérico Lucide
"""
import json, os, re, sys
import requests

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE = os.path.join(BASE, "assets", "cache", "logos")
MANIFEST = os.path.join(CACHE, "manifest.json")
sys.path.insert(0, os.path.join(BASE, "scripts"))
from validar_svg import validar_svg

# alias comunes -> slug real
BRAND_ALIASES = {
    "nextjs": "nextdotjs", "next.js": "nextdotjs",
    "googlebooks": "google", "gbooks": "google",
    "claude": "anthropic", "postgres": "postgresql",
    "aws": "amazonaws", "gcp": "googlecloud",
}

LUCIDE_ICONS = {"globe", "database", "server", "cpu", "webhook", "cloud",
                "mail", "key", "bot", "zap", "layers", "box", "lock",
                "terminal", "clock", "hard-drive", "wifi", "smartphone"}

SESSION = requests.Session()
SESSION.headers.update({"User-Agent": "stack-architect/1.0"})


def norm(s):
    return re.sub(r"[^a-z0-9]", "", s.lower())


def white_fill(svg):
    """True si la marca es blanca en general (invisible sobre tarjeta blanca).
    Un detalle blanco sobre un logo de color NO cuenta."""
    paints = re.findall(r'(?:fill|stroke|stop-color)[=:]\s*"?([#a-zA-Z][^";\s>]*)', svg)
    white = colored = False
    for p in paints:
        p = p.strip().lower()
        if p in ("none", "transparent", "currentcolor") or p.startswith("url("):
            continue
        if re.fullmatch(r"#f{3}(f{3})?|white", p):
            white = True
        else:
            colored = True
    return white and not colored


def _get(url, timeout=20):
    r = SESSION.get(url, timeout=timeout)
    r.raise_for_status()
    txt = r.text
    if "<svg" not in txt[:2000]:
        raise ValueError("no es SVG")
    return txt


def _save(slug, content, fuente="", url=""):
    # SEGURIDAD: todo SVG descargado se valida antes de cachearse.
    ok, motivo = validar_svg(content)
    if not ok:
        raise ValueError(f"SVG inseguro ({fuente}): {motivo}")
    os.makedirs(CACHE, exist_ok=True)
    p = os.path.join(CACHE, f"{slug}.svg")
    with open(p, "w", encoding="utf-8") as fh:
        fh.write(content)
    # manifest para créditos y auditoría
    man = {}
    if os.path.exists(MANIFEST):
        try:
            man = json.load(open(MANIFEST, encoding="utf-8"))
        except (OSError, ValueError):
            pass
    man[slug] = {"fuente": fuente, "url": url, "white_fill": white_fill(content)}
    json.dump(man, open(MANIFEST, "w", encoding="utf-8"), indent=2)
    return p


def svgl_lookup(slug):
    """svgl.app primero: marcas OFICIALES actuales. Solo coincidencia exacta
    de título normalizado (un match difuso podría traer la marca equivocada)."""
    queries = [slug, re.sub(r"[-_.]+", " ", slug).strip()]
    targets = {norm(slug)}
    if len(slug) > 4 and slug.endswith("js"):
        queries.append(slug[:-2])
        targets.add(norm(slug[:-2]))
    for q in dict.fromkeys(queries):
        try:
            r = SESSION.get(
                f"https://api.svgl.app?search={requests.utils.quote(q)}",
                timeout=20)
            r.raise_for_status()
            items = r.json()
        except Exception:
            continue
        if not isinstance(items, list):
            continue
        for it in items:
            if norm(it.get("title", "")) in targets:
                route = it.get("route")
                if isinstance(route, dict):
                    light, dark = route.get("light"), route.get("dark")
                    url = light or dark
                else:
                    url = route
                if url:
                    return url
    raise ValueError("svgl sin coincidencia exacta")


def fetch_simpleicons(slug):
    return _get(f"https://cdn.simpleicons.org/{slug}")


def fetch_devicon(slug):
    for variant in ("original", "plain"):
        try:
            return _get(f"https://raw.githubusercontent.com/devicons/devicon/master"
                        f"/icons/{slug}/{slug}-{variant}.svg")
        except Exception:
            continue
    raise ValueError("devicon sin variante")


def fetch_gilbarbara(slug):
    try:
        return _get(f"https://cdn.jsdelivr.net/gh/gilbarbara/logos/logos/{slug}-icon.svg")
    except Exception:
        return _get(f"https://cdn.jsdelivr.net/gh/gilbarbara/logos/logos/{slug}.svg")


def fetch_lucide(name):
    return _get(f"https://unpkg.com/lucide-static@latest/icons/{name}.svg")


def fetch_url(url):
    return _get(url)


def resolve_brand(brand):
    """Devuelve (slug_cache, ruta_svg)."""
    # URL explícita: "logo=https://sitio.com/logo.svg"
    if "=" in brand and brand.split("=", 1)[1].startswith("http"):
        name, url = brand.split("=", 1)
        slug = re.sub(r"[^a-z0-9_-]", "", name.lower()) or "custom"
        p = os.path.join(CACHE, f"{slug}.svg")
        if os.path.exists(p):
            return slug, p
        return slug, _save(slug, fetch_url(url), "explicit", url)
    if brand.startswith("lucide:"):
        slug, icon = f"lucide-{brand[7:]}", brand[7:]
        p = os.path.join(CACHE, f"{slug}.svg")
        if os.path.exists(p):
            return slug, p
        if icon not in LUCIDE_ICONS:
            raise ValueError(f"icono lucide desconocido: {icon}")
        url = f"https://unpkg.com/lucide-static@latest/icons/{icon}.svg"
        return slug, _save(slug, fetch_lucide(icon), "lucide", url)
    slug = BRAND_ALIASES.get(brand, brand)
    p = os.path.join(CACHE, f"{slug}.svg")
    if os.path.exists(p):
        return slug, p
    errors = []
    # (nombre_fuente, función(slug) -> svg)
    chain = [("svgl", lambda: _get(svgl_lookup(slug))),
             ("simpleicons", lambda: fetch_simpleicons(slug)),
             ("devicon", lambda: fetch_devicon(slug)),
             ("gilbarbara", lambda: fetch_gilbarbara(slug))]
    for name, fn in chain:
        try:
            content = fn()
            url = {"svgl": f"https://svgl.app",
                   "simpleicons": f"https://cdn.simpleicons.org/{slug}",
                   "devicon": "https://devicon.dev",
                   "gilbarbara": "https://github.com/gilbarbara/logos"}.get(name, "")
            path = _save(slug, content, name, url)
            if white_fill(content):
                print(f"  aviso: {slug} tiene fill blanco (verificar sobre tarjeta blanca)",
                      file=sys.stderr)
            return slug, path
        except Exception as e:
            errors.append(f"{name}: {e}")
    raise ValueError(f"sin logo para '{brand}': " + " | ".join(errors))


def main():
    if len(sys.argv) < 2:
        sys.exit("uso: fetch_logos.py architecture.json")
    arch = json.load(open(sys.argv[1], encoding="utf-8"))
    ok, fallos = [], []
    for n in arch.get("nodes", []):
        brand = n.get("brand", "")
        if not brand:
            continue
        try:
            slug, path = resolve_brand(brand)
            ok.append(f"{n['id']} <- {slug}")
        except ValueError as e:
            fallos.append(f"{n['id']}: {e}")
            n["brand"] = "lucide:box"
            slug, path = resolve_brand(n["brand"])
            ok.append(f"{n['id']} <- {slug} (fallback)")
    json.dump(arch, open(sys.argv[1], "w", encoding="utf-8"),
              ensure_ascii=False, indent=2)
    print("\n".join(ok))
    if fallos:
        print("\nFALLOS (usado fallback):")
        print("\n".join(fallos))


if __name__ == "__main__":
    main()
