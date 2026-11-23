#!/usr/bin/env python3
"""Validador de seguridad para SVGs descargados.

Un SVG inlinado en HTML es código activo: puede traer <script>, handlers
on*, <foreignObject> con HTML, o referencias externas. Este validador es
ESTRICTO: ante la duda, rechaza. Los logos oficiales nunca se alteran;
si un SVG no pasa, se descarta y se prueba la siguiente fuente.
"""
import re
import sys
import xml.etree.ElementTree as ET

MAX_BYTES = 1_000_000

# Patrones letales (case-insensitive). Cualquiera -> rechazo.
RECHAZAR = [
    (r"<script[\s>]", "contiene <script>"),
    (r"<foreignObject[\s>]", "contiene <foreignObject> (HTML embebido)"),
    (r"<(iframe|embed|object|link|meta|base)[\s>]", "contiene elemento activo"),
    (r"\son\w+\s*=", "contiene handler de eventos (on*)"),
    (r"javascript\s*:", "contiene javascript: URI"),
    (r"data\s*:\s*text/html", "contiene data:text/html"),
    (r"(href|src|xlink:href)\s*=\s*[\"']\s*https?://", "referencia externa http(s)"),
    (r"(href|src|xlink:href)\s*=\s*[\"']\s*//", "referencia externa protocol-relative"),
    (r"@import\s+url\(\s*[\"']?\s*https?://", "@import externo en CSS"),
    (r"<\?xml-stylesheet[^>]*href\s*=\s*[\"']\s*https?://", "stylesheet externa"),
]

NS_SVG = "{http://www.w3.org/2000/svg}"


def validar_svg(contenido: str) -> tuple[bool, str]:
    """Devuelve (ok, motivo)."""
    if not contenido or len(contenido.encode("utf-8", "ignore")) > MAX_BYTES:
        return False, "vacío o supera 1 MB"
    # Debe ser XML bien formado con raíz <svg>
    try:
        root = ET.fromstring(contenido)
    except ET.ParseError as e:
        return False, f"XML mal formado: {e}"
    tag = root.tag
    if tag != "svg" and tag != NS_SVG + "svg":
        return False, f"raíz no es <svg> (es <{tag}>)"
    for patron, motivo in RECHAZAR:
        if re.search(patron, contenido, re.IGNORECASE):
            return False, motivo
    # Sin entidades externas (XXE)
    if re.search(r"<!ENTITY", contenido, re.IGNORECASE):
        return False, "contiene <!ENTITY (riesgo XXE)"
    return True, "ok"


def main():
    if len(sys.argv) < 2:
        sys.exit("uso: validar_svg.py archivo.svg [...]")
    rc = 0
    for path in sys.argv[1:]:
        try:
            with open(path, encoding="utf-8") as fh:
                contenido = fh.read()
        except OSError as e:
            print(f"{path}: ERROR lectura ({e})")
            rc = 1
            continue
        ok, motivo = validar_svg(contenido)
        print(f"{path}: {'SEGURO' if ok else 'RECHAZADO'} ({motivo})")
        if not ok:
            rc = 1
    sys.exit(rc)


if __name__ == "__main__":
    main()
