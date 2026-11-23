"""Motor geométrico: nodos 132x100, aristas ORTOGONALES, etiquetas sobre la línea.

Reglas de anclaje (un nodo = tile 60x60 + texto; caja 132x100):
- Horizontal (misma fila): lado del tile al lado del tile, y = topY+30.
  Ahí no hay texto al lado de los tiles: seguro.
- Vertical (misma columna): base de la caja (topY+100) al tope del tile.
  NUNCA del fondo del tile (topY+60): cruzaría el texto.
- Codo (distinta fila Y columna, capas adyacentes): horizontal corta hasta
  el corredor entre columnas (libre por construcción), vertical en el
  corredor, horizontal corta al tile destino.
- Salto de >1 capa: curva por DEBAJO (caso raro; el layout favorece
  capas adyacentes).

Etiquetas: sobre la línea con halo (paint-order: stroke en CSS).
"""
import math

TILE = 60
NODE_W, NODE_H = 132, 100
COL_GAP, ROW_PITCH = 120, 170
MARGIN = 48
GROUP_PAD = 24
LABEL_BAND = 56   # aire sobre la primera fila para etiquetas de grupo


def layout(arch):
    nodes = arch["nodes"]
    layers = {}
    for n in nodes:
        layers.setdefault(n.get("layer", 1), []).append(n)
    max_layer = max(layers) if layers else 0
    max_rows = max(len(c) for c in layers.values()) if layers else 0

    def col_x(layer):
        return MARGIN + layer * (NODE_W + COL_GAP)

    def row_y(r):
        return MARGIN + LABEL_BAND + r * ROW_PITCH

    pos = {}
    for layer in sorted(layers):
        for r, n in enumerate(layers[layer]):
            x = col_x(layer)
            y = row_y(r)
            pos[n["id"]] = {"x": x, "topY": y, "cx": x + NODE_W // 2,
                            "layer": layer, "row": r}

    width = MARGIN * 2 + (max_layer + 1) * NODE_W + max_layer * COL_GAP
    height = MARGIN * 2 + LABEL_BAND + max_rows * ROW_PITCH + GROUP_PAD

    # grupos: bounding box de las CAJAS de sus nodos
    groups = []
    for g in arch.get("groups", []):
        members = [pos[n["id"]] for n in nodes
                   if n.get("group") == g["id"] and n["id"] in pos]
        if not members:
            continue
        x0 = min(m["cx"] - NODE_W // 2 for m in members) - GROUP_PAD
        y0 = min(m["topY"] for m in members) - LABEL_BAND + 8
        x1 = max(m["cx"] + NODE_W // 2 for m in members) + GROUP_PAD
        y1 = max(m["topY"] + NODE_H for m in members) + GROUP_PAD
        groups.append({"id": g["id"], "label": g["label"],
                       "icon": g.get("icon", ""),
                       "x": x0, "y": y0, "w": x1 - x0, "h": y1 - y0})

    node_by_id = {n["id"]: n for n in nodes}
    edges = []
    for e in arch.get("edges", []):
        a, b = pos.get(e["from"]), pos.get(e["to"])
        if not a or not b:
            continue
        kind = e.get("kind", "data")
        label = e.get("label", "")
        la, lb = a["layer"], b["layer"]

        if la == lb:
            # pila vertical: base de caja -> tope de tile
            if a["topY"] < b["topY"]:
                x, y1, y2 = a["cx"], a["topY"] + NODE_H + 4, b["topY"] - 4
            else:
                x, y1, y2 = a["cx"], a["topY"] - 4, b["topY"] + NODE_H + 4
            d = f"M{x},{y1} V{y2}"
            lx, ly, anchor = x + 10, (y1 + y2) / 2, "start"
        elif abs(lb - la) == 1:
            # codo por el corredor entre columnas
            y1, y2 = a["topY"] + TILE // 2, b["topY"] + TILE // 2
            if lb > la:  # destino a la derecha
                xs, xt = a["cx"] + TILE // 2 + 4, b["cx"] - TILE // 2 - 4
                corr = col_x(la) + NODE_W + COL_GAP // 2
            else:        # destino a la izquierda
                xs, xt = a["cx"] - TILE // 2 - 4, b["cx"] + TILE // 2 + 4
                corr = col_x(lb) + NODE_W + COL_GAP // 2
            if y1 == y2:
                d = f"M{xs},{y1} H{xt}"
                lx, ly, anchor = (xs + xt) / 2, y1 - 8, "middle"
            else:
                d = f"M{xs},{y1} H{corr} V{y2} H{xt}"
                # El corredor se comparte entre varias aristas: la etiqueta va
                # JUNTO A LA RAMA destino (no al punto medio, que es ambiguo).
                if abs(y2 - y1) > 60:
                    lx, ly = corr + 10, (y2 - 20 if y2 > y1 else y2 + 20)
                    anchor = "start"
                else:
                    lx, ly, anchor = (xs + corr) / 2, y1 - 8, "middle"
        else:
            # salto de >1 capa: carril dedicado POR DEBAJO de todo.
            # verticales en corredores (libres por construcción), horizontal
            # en el carril, aproximación final vertical al centro de la caja.
            la_cx, lb_cx = a["cx"], b["cx"]
            y1, y2 = a["topY"] + NODE_H + 4, b["topY"] + NODE_H + 4
            lane = height - 30
            if lb > la:
                corr1 = col_x(la) + NODE_W + COL_GAP // 2
                corr2 = col_x(lb) - COL_GAP // 2
            else:
                corr1 = col_x(la) - COL_GAP // 2
                corr2 = col_x(lb) + NODE_W + COL_GAP // 2
            # ¿la vertical final choca con nodos bajo el destino?
            bloqueada = False
            for nid, p in pos.items():
                if nid in (e["from"], e["to"]):
                    continue
                bx0, by0 = p["x"], p["topY"]
                if bx0 < lb_cx < bx0 + NODE_W and y2 < by0 + NODE_H:
                    bloqueada = True
                    break
            if bloqueada:
                # aproximación lateral bajo la caja (nunca sobre texto)
                d = (f"M{la_cx},{y1} H{corr1} V{lane} H{corr2} "
                     f"V{y2} H{lb_cx - 44}")
                lx, ly, anchor = (corr1 + corr2) / 2, lane - 8, "middle"
            else:
                d = f"M{la_cx},{y1} H{corr1} V{lane} H{lb_cx} V{y2}"
                lx, ly, anchor = (corr1 + lb_cx) / 2, lane - 8, "middle"

        edges.append({"d": d, "label": label, "kind": kind,
                      "lx": lx, "ly": ly, "anchor": anchor})

    return {"width": width, "height": height, "pos": pos,
            "groups": groups, "edges": edges}
