#!/usr/bin/env python3
"""Renderiza el HTML del diagrama a PNG con Chromium headless.

  python3 scripts/render_png.py diagrama.html -o check.png [--dark] [--scale 2]

Sin --dark captura el tema claro; con --dark fuerza el modo oscuro.
Úsalo para VERIFICAR el diagrama antes de entregarlo (la skill lo exige).
"""
import argparse, os, shutil, subprocess, sys

CHROME = (shutil.which("google-chrome") or shutil.which("chromium")
          or shutil.which("chromium-browser")
          or ("/opt/meta-chromium/chrome"
              if os.path.exists("/opt/meta-chromium/chrome") else None))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("input", help="HTML del diagrama")
    ap.add_argument("-o", "--output", required=True)
    ap.add_argument("--dark", action="store_true", help="forzar modo oscuro")
    ap.add_argument("--scale", type=float, default=2.0,
                    help="device scale factor (nitidez del texto)")
    ap.add_argument("--width", type=int, default=1600)
    ap.add_argument("--height", type=int, default=900)
    a = ap.parse_args()

    if not CHROME:
        sys.exit("no se encontró google-chrome ni chromium en el PATH")
    path = os.path.abspath(a.input)
    cmd = [CHROME, "--headless", "--disable-gpu", "--no-sandbox",
           f"--window-size={a.width},{a.height}",
           f"--force-device-scale-factor={a.scale}",
           f"--screenshot={os.path.abspath(a.output)}"]
    if a.dark:
        cmd.append("--force-dark-mode")
    cmd.append(f"file://{path}")
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
    if r.returncode != 0:
        sys.exit(f"chromium falló: {r.stderr[-500:]}")
    print(f"OK -> {a.output} ({'oscuro' if a.dark else 'claro'}, scale {a.scale})")


if __name__ == "__main__":
    main()
