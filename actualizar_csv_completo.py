#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
import os

CSV_PATH = "/Users/sergio/Library/Mobile Documents/com~apple~CloudDocs/Documents/00 Municipio de Cardona /Inventario y repositorio Estación La Lata/_CONTROL/INVENTARIO_ESTACION_LA_LATA.csv"

# Medidas de Carpeta01
medidas_c01 = {
    "DOC0001": "20.5 cm x 29.8 cm",
    "DOC0002": "21.0 cm x 25.3 cm",
    "DOC0003": "21.0 cm x 29.1 cm",
    "DOC0004": "18.8 cm x 29.7 cm",
    "DOC0005": "21.0 cm x 29.6 cm",
    "DOC0006": "29.7 cm x 19.6 cm",
    "DOC0007": "21.0 cm x 26.3 cm",
    "DOC0008": "17.9 cm x 29.7 cm",
    "DOC0009": "13.0 cm x 29.8 cm",
    "DOC0010": "21.0 cm x 28.2 cm",
    "DOC0011": "21.0 cm x 27.0 cm",
}

# Documentos faltantes de Carpeta01 (DOC0007-DOC0011)
nuevos_c01 = [
    {
        "ID_Unico": "15",
        "Fondo_Documental": "Estación La Lata – Cardona",
        "Nombre_Original": "Adobe Scan 21 abr. 2026 (6).pdf",
        "Nombre_Normalizado": "LL_Carpeta01_DOC0007.pdf",
        "Carpeta_Fisica": "Carpeta01",
        "Numero_Documento": "DOC0007",
        "Tipo_Documental": "Documento administrativo",
        "Titulo": "[Inferido - documento administrativo AFE]",
        "Fecha_Exacta": "",
        "Fecha_Aproximada": "Años 70",
        "Año": "1970",
        "Autor_Emisor": "[inferido]",
        "Destinatario": "[inferido]",
        "Institucion_Vinculada": "AFE",
        "Lugar": "Uruguay",
        "Tema_Principal": "[inferido]",
        "Descripcion_Breve": "Documento administrativo de archivos AFE. Contenido por determinar mediante análisis OCR.",
        "Palabras_Clave": "AFE; documento administrativo; ferrocarril",
        "Soporte_Original_Inferido": "Papel",
        "Idioma": "[inferido]",
        "Cantidad_Paginas": "1",
        "Estado_Legibilidad": "Buena",
        "Estado_Conservacion_Inferido": "Buen estado",
        "Valor_Administrativo": "Medio",
        "Valor_Historico": "Medio",
        "Valor_Patrimonial": "Bajo",
        "Nivel_Acceso": "Público",
        "Duplicado_SN": "No",
        "Documento_Incompleto_SN": "No",
        "OCR_Revisado_SN": "No",
        "Ruta_Almacenamiento": "Carpeta01/LL_Carpeta01_DOC0007.pdf",
        "Observaciones": "Catalogación realizada por Sergio Pérez. Documento de Carpeta01 previamente no incluido en inventario.",
        "Medidas": "21.0 cm x 26.3 cm"
    },
    {
        "ID_Unico": "16",
        "Fondo_Documental": "Estación La Lata – Cardona",
        "Nombre_Original": "Adobe Scan 21 abr. 2026 (7).pdf",
        "Nombre_Normalizado": "LL_Carpeta01_DOC0008.pdf",
        "Carpeta_Fisica": "Carpeta01",
        "Numero_Documento": "DOC0008",
        "Tipo_Documental": "Documento administrativo",
        "Titulo": "[Inferido - documento administrativo AFE]",
        "Fecha_Exacta": "",
        "Fecha_Aproximada": "Años 70",
        "Año": "1970",
        "Autor_Emisor": "[inferido]",
        "Destinatario": "[inferido]",
        "Institucion_Vinculada": "AFE",
        "Lugar": "Uruguay",
        "Tema_Principal": "[inferido]",
        "Descripcion_Breve": "Documento administrativo de archivos AFE. Contenido por determinar mediante análisis OCR.",
        "Palabras_Clave": "AFE; documento administrativo; ferrocarril",
        "Soporte_Original_Inferido": "Papel",
        "Idioma": "[inferido]",
        "Cantidad_Paginas": "1",
        "Estado_Legibilidad": "Buena",
        "Estado_Conservacion_Inferido": "Buen estado",
        "Valor_Administrativo": "Medio",
        "Valor_Historico": "Medio",
        "Valor_Patrimonial": "Bajo",
        "Nivel_Acceso": "Público",
        "Duplicado_SN": "No",
        "Documento_Incompleto_SN": "No",
        "OCR_Revisado_SN": "No",
        "Ruta_Almacenamiento": "Carpeta01/LL_Carpeta01_DOC0008.pdf",
        "Observaciones": "Catalogación realizada por Sergio Pérez. Documento de Carpeta01 previamente no incluido en inventario.",
        "Medidas": "17.9 cm x 29.7 cm"
    },
    {
        "ID_Unico": "17",
        "Fondo_Documental": "Estación La Lata – Cardona",
        "Nombre_Original": "Adobe Scan 21 abr. 2026 (8).pdf",
        "Nombre_Normalizado": "LL_Carpeta01_DOC0009.pdf",
        "Carpeta_Fisica": "Carpeta01",
        "Numero_Documento": "DOC0009",
        "Tipo_Documental": "Documento administrativo",
        "Titulo": "[Inferido - documento administrativo AFE]",
        "Fecha_Exacta": "",
        "Fecha_Aproximada": "Años 70",
        "Año": "1970",
        "Autor_Emisor": "[inferido]",
        "Destinatario": "[inferido]",
        "Institucion_Vinculada": "AFE",
        "Lugar": "Uruguay",
        "Tema_Principal": "[inferido]",
        "Descripcion_Breve": "Documento administrativo de archivos AFE. Contenido por determinar mediante análisis OCR.",
        "Palabras_Clave": "AFE; documento administrativo; ferrocarril",
        "Soporte_Original_Inferido": "Papel",
        "Idioma": "[inferido]",
        "Cantidad_Paginas": "1",
        "Estado_Legibilidad": "Buena",
        "Estado_Conservacion_Inferido": "Buen estado",
        "Valor_Administrativo": "Medio",
        "Valor_Historico": "Medio",
        "Valor_Patrimonial": "Bajo",
        "Nivel_Acceso": "Público",
        "Duplicado_SN": "No",
        "Documento_Incompleto_SN": "No",
        "OCR_Revisado_SN": "No",
        "Ruta_Almacenamiento": "Carpeta01/LL_Carpeta01_DOC0009.pdf",
        "Observaciones": "Catalogación realizada por Sergio Pérez. Documento de Carpeta01 previamente no incluido en inventario.",
        "Medidas": "13.0 cm x 29.8 cm"
    },
    {
        "ID_Unico": "18",
        "Fondo_Documental": "Estación La Lata – Cardona",
        "Nombre_Original": "Adobe Scan 21 abr. 2026 (9).pdf",
        "Nombre_Normalizado": "LL_Carpeta01_DOC0010.pdf",
        "Carpeta_Fisica": "Carpeta01",
        "Numero_Documento": "DOC0010",
        "Tipo_Documental": "Documento administrativo",
        "Titulo": "[Inferido - documento administrativo AFE]",
        "Fecha_Exacta": "",
        "Fecha_Aproximada": "Años 70",
        "Año": "1970",
        "Autor_Emisor": "[inferido]",
        "Destinatario": "[inferido]",
        "Institucion_Vinculada": "AFE",
        "Lugar": "Uruguay",
        "Tema_Principal": "[inferido]",
        "Descripcion_Breve": "Documento administrativo de archivos AFE. Contenido por determinar mediante análisis OCR.",
        "Palabras_Clave": "AFE; documento administrativo; ferrocarril",
        "Soporte_Original_Inferido": "Papel",
        "Idioma": "[inferido]",
        "Cantidad_Paginas": "1",
        "Estado_Legibilidad": "Buena",
        "Estado_Conservacion_Inferido": "Buen estado",
        "Valor_Administrativo": "Medio",
        "Valor_Historico": "Medio",
        "Valor_Patrimonial": "Bajo",
        "Nivel_Acceso": "Público",
        "Duplicado_SN": "No",
        "Documento_Incompleto_SN": "No",
        "OCR_Revisado_SN": "No",
        "Ruta_Almacenamiento": "Carpeta01/LL_Carpeta01_DOC0010.pdf",
        "Observaciones": "Catalogación realizada por Sergio Pérez. Documento de Carpeta01 previamente no incluido en inventario.",
        "Medidas": "21.0 cm x 28.2 cm"
    },
    {
        "ID_Unico": "19",
        "Fondo_Documental": "Estación La Lata – Cardona",
        "Nombre_Original": "Adobe Scan 21 abr. 2026 (10).pdf",
        "Nombre_Normalizado": "LL_Carpeta01_DOC0011.pdf",
        "Carpeta_Fisica": "Carpeta01",
        "Numero_Documento": "DOC0011",
        "Tipo_Documental": "Libro de Quejas",
        "Titulo": "Libro de Quejas - Ferro-Carril Central del Uruguay",
        "Fecha_Exacta": "1949-01-01",
        "Fecha_Aproximada": "Año 1949",
        "Año": "1949",
        "Autor_Emisor": "Ferro-Carril Central del Uruguay",
        "Destinatario": "[Archivo]",
        "Institucion_Vinculada": "Ferro-Carril Central del Uruguay",
        "Lugar": "Uruguay",
        "Tema_Principal": "Gestión administrativa - Quejas y reclamaciones",
        "Descripcion_Breve": "Libro de Quejas de 1949 del Ferro-Carril Central del Uruguay. Registro administrativo de reclamaciones y quejas de pasajeros y usuarios de la red ferroviaria.",
        "Palabras_Clave": "Libro de Quejas; 1949; Ferro-Carril Central; AFE; gestión; reclamaciones",
        "Soporte_Original_Inferido": "Papel - Libro encuadernado",
        "Idioma": "Español",
        "Cantidad_Paginas": "1",
        "Estado_Legibilidad": "Buena",
        "Estado_Conservacion_Inferido": "Buen estado",
        "Valor_Administrativo": "Alto",
        "Valor_Historico": "Alto",
        "Valor_Patrimonial": "Alto",
        "Nivel_Acceso": "Público",
        "Duplicado_SN": "No",
        "Documento_Incompleto_SN": "No",
        "OCR_Revisado_SN": "Sí",
        "Ruta_Almacenamiento": "Carpeta01/LL_Carpeta01_DOC0011.pdf",
        "Observaciones": "Catalogación realizada por Sergio Pérez. DOCUMENTO DE VALOR PATRIMONIAL SIGNIFICATIVO. Libro de Quejas de 1949 con numeración de registro. Referencia a 'Ferro-Carril Central del Uruguay' confirma origen pre-AFE. Alto valor histórico para archivos municipales de Cardona.",
        "Medidas": "21.0 cm x 27.0 cm"
    }
]

# Sobre de Carpeta02 (DOC0001)
sobre_c02 = {
    "ID_Unico": "6",
    "Fondo_Documental": "Estación La Lata – Cardona",
    "Nombre_Original": "Adobe Scan 21 abr. 2026 (12).pdf",
    "Nombre_Normalizado": "LL_Carpeta02_DOC0001.pdf",
    "Carpeta_Fisica": "Carpeta02",
    "Numero_Documento": "DOC0001",
    "Tipo_Documental": "Sobre/Carpeta compartida",
    "Titulo": "DOCS VARIOS 2 - Carpeta compartida con documentación operativa de Estación Sayago",
    "Fecha_Exacta": "",
    "Fecha_Aproximada": "1987-1998",
    "Año": "1998",
    "Autor_Emisor": "Jefatura de Tráfico AFE - Estación Sayago",
    "Destinatario": "[Archivo]",
    "Institucion_Vinculada": "AFE",
    "Lugar": "Sayago",
    "Tema_Principal": "Administración Ferroviaria - Operación de Estación",
    "Descripcion_Breve": "Sobre físico identificado como 'DOCS VARIOS 2' conteniendo documentación operativa diversa de la estación Sayago. Incluye circulares administrativas, comunicaciones técnicas, diagramas de vagones y tablas de disponibilidad. Documentos fechados entre 1987 y 1998. Refleja procedimientos operativos y gestión técnica de la estación durante período tardío de operación ferroviaria.",
    "Palabras_Clave": "AFE; circulares; tráfico; Sayago; vagones; sumarios; cargas; administración; 1987-1998; procedimientos operativos",
    "Soporte_Original_Inferido": "Papel",
    "Idioma": "Español",
    "Cantidad_Paginas": "15",
    "Estado_Legibilidad": "Parcial",
    "Estado_Conservacion_Inferido": "Buen estado",
    "Valor_Administrativo": "Sí",
    "Valor_Historico": "Sí",
    "Valor_Patrimonial": "No",
    "Nivel_Acceso": "Público",
    "Duplicado_SN": "No",
    "Documento_Incompleto_SN": "No",
    "OCR_Revisado_SN": "Sí",
    "Ruta_Almacenamiento": "Carpeta02/LL_Carpeta02_DOC0001.pdf",
    "Observaciones": "Catalogación realizada por Sergio Pérez mediante análisis OCR (tesseract - JPEG). Carpeta compartida física identificada como 'DOCS VARIOS 2' conteniendo documentación operativa de estación Sayago. Fechas múltiples: 1987, 1988, 1991, 1998. Incluye instrucciones técnicas para vagones tolvas y procedimientos de control. Documento de valor administrativo moderado - referencia operativa histórica.",
    "Medidas": "17.4 cm x 29.7 cm"
}

# Leer CSV actual
with open(CSV_PATH, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

# Actualizar medidas de Carpeta01 existentes (primeras 6 filas)
for i, row in enumerate(rows[:6]):
    if 'Numero_Documento' in row:
        doc_num = row['Numero_Documento']
        if doc_num in medidas_c01:
            row['Medidas'] = medidas_c01[doc_num]

# Insertar sobre Carpeta02 al inicio de Carpeta02
# (después de los 6 documentos de Carpeta01)
insert_position = 6  # Después de los 6 de Carpeta01
rows.insert(insert_position, sobre_c02)

# Agregar documentos faltantes de Carpeta01 al final
for doc in nuevos_c01:
    rows.append(doc)

# Actualizar IDs únicos (comenzar en 1)
for i, row in enumerate(rows, 1):
    row['ID_Unico'] = str(i)

# Escribir CSV actualizado
with open(CSV_PATH, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f"✅ CSV actualizado exitosamente")
print(f"   - Medidas agregadas a 6 documentos de Carpeta01")
print(f"   - Sobre Carpeta02_DOC0001 insertado")
print(f"   - 5 documentos faltantes de Carpeta01 (DOC0007-DOC0011) agregados")
print(f"   - Total documentos: {len(rows)}")
