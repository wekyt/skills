#!/usr/bin/env python3
"""Valida architecture.json, calcula layout ortogonal y emite .html autocontenido."""
import argparse, base64, html, json, os, sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE, "scripts"))
from layout_engine import layout
from fetch_logos import resolve_brand, CACHE

MANIFEST = os.path.join(CACHE, "manifest.json")


def validar(arch):
    assert isinstance(arch.get("title"), str), "falta title"
    ids = set()
    for n in arch.get("nodes", []):
        for k in ("id", "label", "brand"):
            assert k in n, f"nodo sin {k}: {n}"
        assert n["id"] not in ids, f"id duplicado: {n['id']}"
        ids.add(n["id"])
        n.setdefault("layer", 1)
        n.setdefault("sublabel", "")
    for e in arch.get("edges", []):
        assert e["from"] in ids, f"edge from desconocido: {e['from']}"
        assert e["to"] in ids, f"edge to desconocido: {e['to']}"
        e.setdefault("kind", "data")
    return arch


def logo_data_uri(brand):
    """Logo oficial como data URI. Nunca se altera."""
    slug, path = resolve_brand(brand)
    raw = open(path, "rb").read()
    ext = os.path.splitext(path)[1].lower()
    mime = {"svg": "image/svg+xml", "png": "image/png",
            "webp": "image/webp"}.get(ext.lstrip("."), "image/svg+xml")
    return f"data:{mime};base64," + base64.b64encode(raw).decode()


def icon_sources():
    try:
        man = json.load(open(MANIFEST, encoding="utf-8"))
    except (OSError, ValueError):
        return ""
    fuentes = sorted({v.get("fuente", "?") for v in man.values() if isinstance(v, dict)})
    return " / ".join(fuentes)


EDGE_CLASS = {"primary": "e", "data": "n", "trigger": "n dash"}
LABEL_CLASS = {"primary": "el a", "data": "el", "trigger": "el"}

TEMPLATE = """<!DOCTYPE html>
<html lang="es" data-theme="light">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<style>
/* dibujo de ingeniería: papel cuadriculado sutil, un acento, etiquetas mono.
   Tokens en :root; el tema oscuro va en [data-theme="dark"]. */
:root {{
  --paper: #fafbfd; --rule: #e8ebf0; --rule2: #d4d9e2;
  --ink: #1a1d21; --ink2: #3c414b; --muted: #6b7280;
  --neutral: #5b6472; --accent: #2563eb;
  --veil: rgba(250,251,253,.82); --tile-br: #dfe3ea;
  --group-br: #c9d1dd; --group-bg: rgba(37,99,235,.045);
}}
[data-theme="dark"] {{
  --paper: #14161c; --rule: #1e222b; --rule2: #2e3542;
  --ink: #eef1f6; --ink2: #c8cfdb; --muted: #98a1b3;
  --neutral: #a7b0c2; --accent: #6b9bff;
  --veil: rgba(20,22,28,.82); --tile-br: #2e3542;
  --group-br: #3a4354; --group-bg: rgba(107,155,255,.07);
}}
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{ background: var(--paper); color: var(--ink);
  font-family: -apple-system, "Segoe UI", Inter, Roboto, sans-serif;
  padding: 32px; }}
.head {{ display: flex; justify-content: space-between; align-items: end;
  gap: 24px; padding-bottom: 16px; border-bottom: 1px solid var(--rule2);
  margin-bottom: 24px; }}
.kicker {{ font-family: ui-monospace, "SF Mono", Menlo, monospace; font-size: 11px;
  letter-spacing: .04em; color: var(--accent); margin-bottom: 8px; }}
h1 {{ font-size: 24px; font-weight: 700; letter-spacing: -.01em; }}
.lede {{ max-width: 320px; font-size: 12px; line-height: 1.7; color: var(--neutral); }}
.theme-btn {{ font-family: ui-monospace, monospace; font-size: 11px; color: var(--muted);
  background: none; border: 1px solid var(--rule2); border-radius: 8px;
  padding: 6px 12px; cursor: pointer; }}
.scroller {{ overflow-x: auto; border: 1px solid var(--rule2); border-radius: 12px; }}
.canvas {{ position: relative; width: {width}px; height: {height}px;
  background-color: var(--paper);
  background-image:
    linear-gradient(var(--rule) 1px, transparent 1px),
    linear-gradient(90deg, var(--rule) 1px, transparent 1px);
  background-size: 24px 24px; background-position: -1px -1px; }}
.group {{ position: absolute; border: 1.5px solid var(--group-br);
  background: var(--group-bg); border-radius: 12px; }}
.g-label {{ position: absolute; top: 12px; left: 12px; display: flex;
  align-items: center; gap: 6px; font-size: 12px; font-weight: 600;
  color: var(--neutral); white-space: nowrap; }}
.g-label img {{ width: 14px; height: 14px; }}
.node {{ position: absolute; width: 132px; text-align: center; }}
.tile {{ width: 60px; height: 60px; margin: 0 auto; background: #fff;
  border: 1px solid var(--tile-br); border-radius: 12px;
  display: grid; place-items: center;
  box-shadow: 0 1px 2px rgba(20,24,40,.06); }}
.tile img {{ width: 34px; height: 34px; object-fit: contain; }}
.node .name {{ font-size: 13px; font-weight: 600; margin-top: 8px; }}
.node .role {{ font-family: ui-monospace, "SF Mono", Menlo, monospace;
  font-size: 9.5px; letter-spacing: .04em; color: var(--muted); margin-top: 2px; }}
.node .name span, .node .role span {{ background: var(--veil);
  padding: 0 4px; border-radius: 3px; }}
svg.edges {{ position: absolute; inset: 0; pointer-events: none; }}
.e {{ stroke: var(--accent); stroke-width: 1.6; fill: none; }}
.n {{ stroke: var(--neutral); stroke-width: 1.4; fill: none; }}
.dash {{ stroke-dasharray: 4 5; }}
.el {{ font-family: ui-monospace, "SF Mono", Menlo, monospace; font-size: 10.5px;
  letter-spacing: .04em; fill: var(--neutral);
  paint-order: stroke; stroke: var(--paper); stroke-width: 4px; stroke-linejoin: round; }}
.el.a {{ fill: var(--accent); }}
.legend {{ display: flex; gap: 24px; margin-top: 16px; font-family: ui-monospace, monospace;
  font-size: 10px; letter-spacing: .04em; color: var(--muted); }}
.sw {{ display: inline-block; width: 30px; border-top: 1.6px solid var(--accent);
  vertical-align: middle; margin-right: 6px; }}
.sw.n {{ border-color: var(--neutral); }}
.sw.dash {{ border-top-style: dashed; }}
.foot {{ margin-top: 24px; padding-top: 16px; border-top: 1px solid var(--rule2);
  display: flex; justify-content: space-between; gap: 16px; flex-wrap: wrap;
  font-family: ui-monospace, monospace; font-size: 10px; color: var(--muted); }}
</style>
</head>
<body>
<div class="head">
  <div><div class="kicker">stack-architect</div><h1>{title}</h1></div>
  <div style="display:flex;gap:16px;align-items:end">
    <p class="lede">{lede}</p>
    <button class="theme-btn" onclick="toggleTheme()">◐ tema</button>
  </div>
</div>
<div class="scroller"><div class="canvas">
{groups_html}
<svg class="edges" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
<defs><marker id="ar" viewBox="0 0 10 10" refX="8" refY="5"
  markerWidth="6.5" markerHeight="6.5" orient="auto-start-reverse">
<path d="M0 0 L10 5 L0 10 z" fill="context-stroke"/></marker></defs>
{edges_svg}
</svg>
{nodes_html}
</div></div>
<div class="legend">{legend_html}</div>
<div class="foot"><span>{credits}</span>
<span>Logos: marcas de sus respectivos dueños · solo uso descriptivo</span></div>
<script>
function toggleTheme() {{
  const h = document.documentElement;
  h.dataset.theme = h.dataset.theme === "dark" ? "light" : "dark";
}}
if (matchMedia("(prefers-color-scheme: dark)").matches) toggleTheme();
</script>
</body>
</html>
"""

LEGEND_ITEMS = {
    "primary": '<span><span class="sw"></span>flujo principal</span>',
    "data": '<span><span class="sw n"></span>conexión</span>',
    "trigger": '<span><span class="sw n dash"></span>dev / deploy</span>',
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("input", help="architecture.json")
    ap.add_argument("-o", "--output", required=True)
    ap.add_argument("--lede", default="",
                    help="1-2 frases de contexto bajo el título")
    a = ap.parse_args()

    arch = validar(json.load(open(a.input, encoding="utf-8")))
    L = layout(arch)

    groups_html = []
    for g in L["groups"]:
        icon = (f'<img src="{logo_data_uri(g["icon"])}" alt="">'
                if g.get("icon") else "")
        groups_html.append(
            f'<div class="group" style="left:{g["x"]}px;top:{g["y"]}px;'
            f'width:{g["w"]}px;height:{g["h"]}px">'
            f'<div class="g-label">{icon}{html.escape(g["label"])}</div></div>')

    nodes_html = []
    for n in arch["nodes"]:
        p = L["pos"][n["id"]]
        try:
            logo = logo_data_uri(n["brand"])
        except ValueError as e:
            print(f"aviso: {e} -> fallback", file=sys.stderr)
            logo = logo_data_uri("lucide:box")
        role = (f'<div class="role"><span>{html.escape(n["sublabel"])}</span></div>'
                if n["sublabel"] else '<div class="role"><span>&nbsp;</span></div>')
        nodes_html.append(
            f'<div class="node" style="left:{p["x"]}px;top:{p["topY"]}px">'
            f'<div class="tile"><img src="{logo}" alt=""></div>'
            f'<div class="name"><span>{html.escape(n["label"])}</span></div>'
            f'{role}</div>')

    edges_svg = []
    kinds = set()
    for e in L["edges"]:
        k = e["kind"]
        kinds.add(k)
        edges_svg.append(
            f'<path class="{EDGE_CLASS.get(k, "n")}" d="{e["d"]}" '
            f'marker-end="url(#ar)"/>')
        if e["label"]:
            anchor = e["anchor"]
            base = 'dominant-baseline="middle"' if anchor == "start" else ""
            edges_svg.append(
                f'<text class="{LABEL_CLASS.get(k, "el")}" x="{e["lx"]:.0f}" '
                f'y="{e["ly"]:.0f}" text-anchor="{anchor}" {base}>'
                f'{html.escape(e["label"])}</text>')

    legend_html = "".join(LEGEND_ITEMS[k] for k in
                          ("primary", "data", "trigger") if k in kinds)
    credits = f"iconos: {icon_sources()}" if icon_sources() else ""

    out = TEMPLATE.format(
        title=html.escape(arch["title"]), lede=html.escape(a.lede),
        width=L["width"], height=L["height"],
        groups_html="\n".join(groups_html),
        edges_svg="\n".join(edges_svg),
        nodes_html="\n".join(nodes_html),
        legend_html=legend_html, credits=html.escape(credits))
    with open(a.output, "w", encoding="utf-8") as fh:
        fh.write(out)
    print(f"OK -> {a.output} ({len(arch['nodes'])} nodos, {len(L['edges'])} flechas)")


if __name__ == "__main__":
    main()
