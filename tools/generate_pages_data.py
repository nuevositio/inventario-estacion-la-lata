#!/usr/bin/env python3
"""Genera el catalogo publico usado por GitHub Pages."""

from __future__ import annotations

import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "_CONTROL" / "INVENTARIO_ESTACION_LA_LATA.csv"
OUTPUT_PATH = ROOT / "assets" / "inventory-data.js"
PUBLIC_FOLDERS = ("Carpeta01", "Carpeta02", "Carpeta03")


def clean(value: str | None) -> str:
    return (value or "").strip()


def main() -> None:
    records: list[dict[str, str | bool]] = []
    indexed_paths: set[str] = set()

    with CSV_PATH.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            folder = clean(row.get("Carpeta_Fisica"))
            if folder not in PUBLIC_FOLDERS:
                continue

            route = clean(row.get("Ruta_Almacenamiento"))
            indexed_paths.add(route)
            path = ROOT / route

            records.append(
                {
                    "id": clean(row.get("ID_Unico")),
                    "folder": folder,
                    "number": clean(row.get("Numero_Documento")),
                    "originalName": clean(row.get("Nombre_Original")),
                    "normalizedName": clean(row.get("Nombre_Normalizado")),
                    "type": clean(row.get("Tipo_Documental")),
                    "title": clean(row.get("Titulo")),
                    "exactDate": clean(row.get("Fecha_Exacta")),
                    "approxDate": clean(row.get("Fecha_Aproximada")),
                    "year": clean(row.get("Año")),
                    "author": clean(row.get("Autor_Emisor")),
                    "recipient": clean(row.get("Destinatario")),
                    "institution": clean(row.get("Institucion_Vinculada")),
                    "place": clean(row.get("Lugar")),
                    "topic": clean(row.get("Tema_Principal")),
                    "description": clean(row.get("Descripcion_Breve")),
                    "keywords": clean(row.get("Palabras_Clave")),
                    "pages": clean(row.get("Cantidad_Paginas")),
                    "legibility": clean(row.get("Estado_Legibilidad")),
                    "adminValue": clean(row.get("Valor_Administrativo")),
                    "historicValue": clean(row.get("Valor_Historico")),
                    "heritageValue": clean(row.get("Valor_Patrimonial")),
                    "access": clean(row.get("Nivel_Acceso")),
                    "ocrReviewed": clean(row.get("OCR_Revisado_SN")),
                    "path": route,
                    "notes": clean(row.get("Observaciones")),
                    "fileExists": path.is_file(),
                    "source": "inventario",
                }
            )

    for folder in PUBLIC_FOLDERS:
        for file_path in sorted((ROOT / folder).glob("*.pdf")):
            route = file_path.relative_to(ROOT).as_posix()
            if route in indexed_paths:
                continue
            records.append(
                {
                    "id": "",
                    "folder": folder,
                    "number": file_path.stem.split("_")[-1],
                    "originalName": file_path.name,
                    "normalizedName": file_path.name,
                    "type": "[Sin registro en inventario]",
                    "title": "[Documento pendiente de alta en inventario]",
                    "exactDate": "",
                    "approxDate": "",
                    "year": "",
                    "author": "",
                    "recipient": "",
                    "institution": "",
                    "place": "",
                    "topic": "[Requiere catalogación]",
                    "description": "El PDF existe en la carpeta digitalizada, pero no tiene una fila correspondiente en el inventario CSV.",
                    "keywords": "pendiente; inventario; control",
                    "pages": "",
                    "legibility": "",
                    "adminValue": "",
                    "historicValue": "",
                    "heritageValue": "",
                    "access": "Público",
                    "ocrReviewed": "",
                    "path": route,
                    "notes": "Alta pendiente en _CONTROL/INVENTARIO_ESTACION_LA_LATA.csv.",
                    "fileExists": True,
                    "source": "archivo_sin_registro",
                }
            )

    records.sort(key=lambda item: (str(item["folder"]), str(item["number"]), str(item["path"])))

    payload = {
        "generatedFrom": "_CONTROL/INVENTARIO_ESTACION_LA_LATA.csv",
        "publishedFolders": list(PUBLIC_FOLDERS),
        "recordCount": len(records),
        "records": records,
    }

    OUTPUT_PATH.write_text(
        "window.INVENTORY_DATA = "
        + json.dumps(payload, ensure_ascii=False, indent=2)
        + ";\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
