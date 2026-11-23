#!/usr/bin/env python3
"""Analizador multipropósito: repo, frase o documento -> architecture.json."""
import argparse, json, os, re, sys

# (palabras clave en archivos/texto) -> (id, label, sublabel, brand, layer, group)
STACK_MAP = [
    (r"\bnext(\.js)?\b", ("nextjs", "Next.js", "App Router", "nextdotjs", 1, "app")),
    (r"\breact\b", ("react", "React", "", "react", 1, "app")),
    (r"\bvercel\b", ("vercel", "Vercel", "Hosting + Edge", "vercel", 1, "cloud")),
    (r"\bsupabase", ("supabase", "Supabase", "Postgres + Auth", "supabase", 2, "data")),
    (r"\bpostgres", ("postgres", "PostgreSQL", "", "postgresql", 2, "data")),
    (r"\bneon\b", ("neon", "Neon", "Postgres serverless", "neon", 2, "data")),
    (r"\bredis\b", ("redis", "Redis", "Caché / colas", "redis", 2, "data")),
    (r"\bn8n\b", ("n8n", "n8n", "Automatización", "n8n", 3, "services")),
    (r"\bstripe\b", ("stripe", "Stripe", "Pagos", "stripe", 3, "services")),
    (r"\bresend\b", ("resend", "Resend", "Email transaccional", "resend", 3, "services")),
    (r"\bclaude\b|\banthropic\b", ("claude", "Claude", "Anthropic API", "anthropic", 3, "ai")),
    (r"\bopenai\b", ("openai", "OpenAI", "", "openai", 3, "ai")),
    (r"\bgoogle.?books\b", ("gbooks", "Google Books", "API catálogo", "googlebooks", 4, "ai")),
    (r"\bturnstile\b|\bcloudflare\b", ("cloudflare", "Cloudflare", "Turnstile / CDN", "cloudflare", 1, "cloud")),
    (r"\bdocker\b", ("docker", "Docker", "Contenedores", "docker", 2, "infra")),
    (r"\bgithub\b", ("github", "GitHub", "Repo + CI", "github", 0, "infra")),
    (r"\baws\b|\bamazon\b", ("aws", "AWS", "", "amazonaws", 2, "cloud")),
    (r"\bfirebase\b", ("firebase", "Firebase", "", "firebase", 2, "data")),
    (r"\bprisma\b", ("prisma", "Prisma", "ORM", "prisma", 2, "data")),
    (r"\btailwind", ("tailwind", "Tailwind", "CSS", "tailwindcss", 1, "app")),
    (r"\bpython\b", ("python", "Python", "", "python", 1, "app")),
    (r"\bfastapi\b", ("fastapi", "FastAPI", "", "fastapi", 1, "app")),
    (r"\btypescript\b", ("ts", "TypeScript", "", "typescript", 1, "app")),
]

GROUP_LABELS = {
    "user": "Cliente", "app": "Aplicación", "cloud": "Nube",
    "data": "Datos", "services": "Servicios", "ai": "IA / APIs", "infra": "Infraestructura",
}

EDGE_HINTS = [  # (regex_origen, regex_destino, label, kind)
    (r"user|client", r"nextjs|react|fastapi|web", "HTTPS", "primary"),
    (r"nextjs|react|web|app", r"supabase|postgres|neon|prisma|db", "SQL / API", "primary"),
    (r"nextjs|react|web|app", r"claude|openai|ai", "API", "data"),
    (r"nextjs|react|web|app", r"stripe|resend|n8n|service", "API / Webhook", "data"),
    (r"nextjs|react|web|app", r"cloudflare|turnstile", "Verify", "data"),
    (r"supabase|db|postgres", r"app|nextjs", "Datos", "data"),
    (r"github|actions|ci", r"vercel|netlify|app", "deploy", "trigger"),
]


CONFIG_FILES = {"package.json", "docker-compose.yml", "docker-compose.yaml",
                "pyproject.toml", "requirements.txt", "Pipfile", ".env.example",
                "Dockerfile", "fly.toml", "render.yaml"}
SOURCE_EXTS = (".ts", ".tsx", ".js", ".jsx", ".py", ".go", ".rb", ".java")
SKIP_DIRS = ("node_modules", ".git", ".next", "__pycache__", ".venv", "dist", "build")


def scan_repo(path):
    text = ""
    for root, _, files in os.walk(path):
        if any(part in SKIP_DIRS for part in root.split(os.sep)):
            continue
        for f in files:
            fp = os.path.join(root, f)
            is_config = f in CONFIG_FILES or f.endswith(".tf")
            is_source = f.endswith(SOURCE_EXTS)
            if not (is_config or is_source):
                continue
            try:
                if os.path.getsize(fp) > 300_000:
                    continue
                with open(fp, encoding="utf-8", errors="ignore") as fh:
                    content = fh.read(120_000) if is_source else fh.read()
                # del código solo importan las pistas de stack: imports, URLs, SDKs
                if is_source:
                    pistas = [
                        m.group(0) for m in re.finditer(
                            r"(?i)(?:import|from|require)\s+[\"'][^\"']+[\"']"
                            r"|https?://[a-z0-9.-]+\.[a-z]{2,}[a-z0-9/._-]*"
                            r"|\b(?:anthropic|openai|stripe|resend|supabase|prisma"
                            r"|n8n|twilio|sendgrid|turnstile|cloudflare|google)\b[\w.-]*",
                            content)
                    ]
                    content = "\n".join(pistas)
                text += "\n" + content
            except OSError:
                pass
    # package.json: nombres de dependencias pesan más
    pj = os.path.join(path, "package.json")
    if os.path.exists(pj):
        try:
            deps = json.load(open(pj)).get("dependencies", {})
            text += "\n" + " ".join(deps.keys())
        except (OSError, json.JSONDecodeError):
            pass
    return text


def extract(text, title):
    low = text.lower()
    nodes, seen = [], set()
    for pattern, (nid, label, sub, brand, layer, group) in STACK_MAP:
        if nid in seen:
            continue
        if re.search(pattern, low):
            nodes.append({"id": nid, "label": label, "sublabel": sub,
                          "brand": brand, "layer": layer, "group": group})
            seen.add(nid)
    nodes.sort(key=lambda n: (n["layer"], n["id"]))
    # nodo usuario siempre al inicio
    nodes.insert(0, {"id": "user", "label": "Usuario", "sublabel": "Navegador",
                     "brand": "lucide:globe", "layer": 0, "group": "user"})
    groups = [{"id": g, "label": GROUP_LABELS.get(g, g)}
              for g in dict.fromkeys(n["group"] for n in nodes)]
    edges = []
    for ro, rd, lab, kind in EDGE_HINTS:
        srcs = [n["id"] for n in nodes if re.search(ro, n["id"])]
        dsts = [n["id"] for n in nodes if re.search(rd, n["id"])]
        for s in srcs:
            for d in dsts:
                if s != d and not any(e["from"] == s and e["to"] == d for e in edges):
                    edges.append({"from": s, "to": d, "label": lab,
                                  "kind": kind})
    return {"title": title, "direction": "LR", "groups": groups,
            "nodes": nodes, "edges": edges}


def main():
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--repo", help="ruta al repositorio a analizar")
    g.add_argument("--text", help="frase en lenguaje natural")
    g.add_argument("--text-file", help="archivo con PRD/documento")
    ap.add_argument("-o", "--output", required=True)
    ap.add_argument("--title", default="Arquitectura del sistema")
    a = ap.parse_args()

    if a.repo:
        text = scan_repo(a.repo)
        title = a.title if a.title != "Arquitectura del sistema" \
            else os.path.basename(os.path.abspath(a.repo)) + ": Arquitectura"
    elif a.text:
        text, title = a.text, a.title
    else:
        with open(a.text_file, encoding="utf-8") as fh:
            text = fh.read()
        title = a.title

    arch = extract(text, title)
    with open(a.output, "w", encoding="utf-8") as fh:
        json.dump(arch, fh, ensure_ascii=False, indent=2)
    print(f"{len(arch['nodes'])} nodos, {len(arch['edges'])} conexiones -> {a.output}")
    print("Revisa el JSON antes de renderizar: ajusta layers/groups/edges si hace falta.")


if __name__ == "__main__":
    main()
