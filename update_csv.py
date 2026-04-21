#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
import os

CSV_PATH = "/Users/sergio/Library/Mobile Documents/com~apple~CloudDocs/Documents/00 Municipio de Cardona /Inventario y repositorio Estación La Lata/_CONTROL/INVENTARIO_ESTACION_LA_LATA.csv"

NEW_DOCS = [
    {
        "ID_Unico": "LL_Carpeta02_DOC0002",
        "Nombre_Original": "Circular E.2046",
        "Nombre_Normalizado": "Circular E.2046 - Utilización Tablas Contra Puertas",
        "Tipo_Documental": "Circular Administrativa",
        "Titulo": "Utilización de Tablas Contra Puertas en Vagones Multiuso",
        "Fecha_Exacta": "1988-06-29",
        "Fecha_Aproximada": "",
        "Año": "1988",
        "Autor_Emisor": "Gerencia de Explotación AFE",
        "Destinatario": "Jefes de Estaciones",
        "Institucion_Vinculada": "AFE",
        "Lugar": "Montevideo",
        "Tema_Principal": "Administración Ferroviaria",
        "Descripcion_Breve": "Utilización de tablas contra puertas en vagones multiuso 40B",
        "Palabras_Clave": "Vagones, Tablas, Transporte, AFE",
        "Estado_Legibilidad": "Buena",
        "Medidas": "19.4 cm x 29.7 cm"
    },
    {
        "ID_Unico": "LL_Carpeta02_DOC0003",
        "Nombre_Original": "Circular E.2497",
        "Nombre_Normalizado": "Circular E.2497 - Control Tablas Vagones Graneleros",
        "Tipo_Documental": "Circular Administrativa",
        "Titulo": "Control de Tablas Contra Puertas para Vagones Graneleros",
        "Fecha_Exacta": "1984-03-19",
        "Año": "1984",
        "Autor_Emisor": "Gerencia de Explotación AFE",
        "Descripcion_Breve": "Control de tablas contra puertas en vagones graneleros",
        "Palabras_Clave": "Vagones graneleros, Control, Tablas, AFE",
        "Cantidad_Paginas": "1",
        "Medidas": "17.9 cm x 29.7 cm"
    },
    {
        "ID_Unico": "LL_Carpeta02_DOC0004",
        "Nombre_Original": "Circular E.2548",
        "Nombre_Normalizado": "Circular E.2548 - Encerados Lonas Productos Químicos",
        "Tipo_Documental": "Circular Administrativa",
        "Titulo": "Encerados o Lonas de Pisos en Transporte de Productos Químicos",
        "Fecha_Exacta": "1985-05-08",
        "Año": "1985",
        "Autor_Emisor": "Gerencia de Explotación AFE",
        "Descripcion_Breve": "Regulación de encerados/lonas para pisos en vagones con químicos",
        "Palabras_Clave": "Productos químicos, Seguridad, Encerados, Vagones, AFE",
        "Cantidad_Paginas": "1",
        "Medidas": "19.6 cm x 29.7 cm"
    },
    {
        "ID_Unico": "LL_Carpeta02_DOC0005",
        "Nombre_Original": "Circular E.2495",
        "Nombre_Normalizado": "Circular E.2495 - Sumarios Adelantos",
        "Tipo_Documental": "Circular Administrativa",
        "Titulo": "División de Sumarios - Remisión de Adelantos",
        "Fecha_Exacta": "1987-12-26",
        "Año": "1987",
        "Autor_Emisor": "Gerencia de Explotación AFE",
        "Descripcion_Breve": "Procedimientos para confección y remisión de sumarios de adelantos",
        "Palabras_Clave": "Sumarios, Adelantos, Procedimientos, AFE",
        "Cantidad_Paginas": "1",
        "Medidas": "20.2 cm x 29.7 cm"
    },
    {
        "ID_Unico": "LL_Carpeta02_DOC0006",
        "Nombre_Original": "Comunicación Movimiento Vagones",
        "Nombre_Normalizado": "Comunicación - Movimiento Vagones 1995",
        "Tipo_Documental": "Comunicación Operativa",
        "Titulo": "Movimiento de Vagones - Procedimiento Reporting",
        "Fecha_Exacta": "1995-09-22",
        "Año": "1995",
        "Autor_Emisor": "Jefatura de Tráfico AFE",
        "Descripcion_Breve": "Obligatoriedad de reportar movimiento de vagones a Departamento Técnico",
        "Palabras_Clave": "Vagones, Movimiento, Reporting, Operación, AFE",
        "Cantidad_Paginas": "1",
        "Medidas": "21.0 cm x 28.0 cm"
    },
    {
        "ID_Unico": "LL_Carpeta02_DOC0007",
        "Nombre_Original": "Comunicación Vagones Tolvas",
        "Nombre_Normalizado": "Comunicación - Control Vagones Tolvas 1998",
        "Tipo_Documental": "Comunicación Técnica",
        "Titulo": "Programa Computación para Control de Vagones Tolvas",
        "Fecha_Exacta": "1998-01-22",
        "Año": "1998",
        "Autor_Emisor": "Jefatura de Tráfico AFE",
        "Descripcion_Breve": "Instrucciones transmisión información vagones a Estaciones Concentradoras",
        "Palabras_Clave": "Computación, Control, Vagones tolvas, Información técnica, AFE",
        "Cantidad_Paginas": "4",
        "Medidas": "21.0 cm x 29.7 cm (aprox)"
    },
    {
        "ID_Unico": "LL_Carpeta02_DOC0008",
        "Nombre_Original": "Diagrama Técnico Vagones",
        "Nombre_Normalizado": "Diagrama - Sistema de Frenos Vagones",
        "Tipo_Documental": "Diagrama Técnico",
        "Titulo": "Esquema Técnico: Sistema de Frenos en Vagones",
        "Fecha_Exacta": "1991-01-01",
        "Año": "1991",
        "Autor_Emisor": "Departamento Técnico AFE",
        "Descripcion_Breve": "Diagrama del circuito de freno en vagones vacíos y cargados",
        "Palabras_Clave": "Vagones, Frenos, Sistema técnico, Diagrama, AFE",
        "Cantidad_Paginas": "4",
        "Medidas": "21.0 cm x 27.3 cm (aprox)"
    },
    {
        "ID_Unico": "LL_Carpeta02_DOC0009",
        "Nombre_Original": "Tabla Disponibilidad Vagones",
        "Nombre_Normalizado": "Tabla - Disponibilidad Vagones",
        "Tipo_Documental": "Formulario Operativo",
        "Titulo": "Tabla de Disponibilidad de Vagones",
        "Fecha_Exacta": "1998-12-31",
        "Año": "1998",
        "Autor_Emisor": "Departamento Técnico AFE",
        "Descripcion_Breve": "Registro disponibilidad de vagones vacíos listos para circulación",
        "Palabras_Clave": "Vagones disponibles, Inventario, Operación, AFE",
        "Cantidad_Paginas": "1",
        "Medidas": "29.7 cm x 16.8 cm"
    },
]

# Read existing CSV
with open(CSV_PATH, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    rows = list(reader)
    fieldnames = reader.fieldnames

# Add new documents
for doc in NEW_DOCS:
    new_row = {}
    for field in fieldnames:
        if field == "Fondo_Documental":
            new_row[field] = "Estación La Lata"
        elif field == "Carpeta_Fisica":
            new_row[field] = "Carpeta02"
        elif field == "Numero_Documento":
            doc_num = doc["ID_Unico"].split("_")[-1]
            new_row[field] = doc_num
        elif field == "Soporte_Original_Inferido":
            new_row[field] = "Papel fotocopia"
        elif field == "Idioma":
            new_row[field] = "Español"
        elif field == "Estado_Conservacion_Inferido":
            new_row[field] = "Bueno"
        elif field == "Valor_Administrativo":
            new_row[field] = "Alto"
        elif field == "Valor_Historico":
            new_row[field] = "Medio"
        elif field == "Valor_Patrimonial":
            new_row[field] = "Medio"
        elif field == "Nivel_Acceso":
            new_row[field] = "Publico"
        elif field == "Duplicado_SN":
            new_row[field] = "No"
        elif field == "Documento_Incompleto_SN":
            new_row[field] = "No"
        elif field == "OCR_Revisado_SN":
            new_row[field] = "No"
        elif field == "Ruta_Almacenamiento":
            new_row[field] = f"Carpeta02/{doc['ID_Unico']}.pdf"
        elif field == "Observaciones":
            new_row[field] = f"Catalogacion por S. Perez. Separado de sobre DOCS VARIOS 2."
        elif field in doc:
            new_row[field] = doc[field]
        else:
            new_row[field] = ""
    rows.append(new_row)

# Write updated CSV
with open(CSV_PATH, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f"✅ CSV actualizado con {len(NEW_DOCS)} nuevas entradas")
print(f"Total documentos: {len(rows)}")
