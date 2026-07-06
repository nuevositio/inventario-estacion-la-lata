# Inventario y Repositorio Documental - Estación La Lata

Proyecto de catalogación, preservación digital y publicación web del fondo documental de la Estación La Lata del Municipio de Cardona.

Sitio público previsto en GitHub Pages:

`https://nuevositio.github.io/inventario-estacion-la-lata/`

## Descripción

Sistema de inventario y repositorio para organización, catalogación y preservación digital de documentos históricos y administrativos de la Estación La Lata.

## Estructura del Repositorio

```
├── index.html          ← Buscador público para GitHub Pages
├── assets/            ← Datos públicos generados para el buscador
├── Carpeta01/          ← Documentos digitalizados (carpeta física 01)
├── Carpeta02/          ← Documentos digitalizados (carpeta física 02)
├── ...
├── Carpeta25/          ← Documentos digitalizados (carpeta física 25)
├── MANUAL_REPOSITORIO.md              ← Manual de carga y búsqueda
├── tools/generate_pages_data.py       ← Generador de datos web desde CSV
└── _CONTROL/           ← Documentación de control y catalogación
    ├── INVENTARIO_ESTACION_LA_LATA.xlsx   ← Archivo base de trabajo
    ├── INVENTARIO_ESTACION_LA_LATA.csv    ← Base de datos principal
    ├── PROTOCOLO_ANALISIS.md               ← Protocolo de catalogación
    ├── GUIA_RAPIDA.txt                     ← Guía rápida de referencia
    ├── PLANTILLA_FICHA_CATALOGRAFICA.txt   ← Plantilla de fichas
    └── README.md                            ← Este archivo
```

## Convención de Nomenclatura

**Formato obligatorio:** `LL_CarpetaXX_DOCXXXX.pdf`

- **LL** = Estación La Lata (identificación del fondo)
- **CarpetaXX** = Número de carpeta física (01-25)
- **DOCXXXX** = Número correlativo del documento (0001-9999)

**Ejemplo:** `LL_Carpeta01_DOC0001.pdf`

## Publicación en GitHub Pages

La web estática se publica desde la raíz de la rama `main` para que los enlaces a `Carpeta01`, `Carpeta02` y `Carpeta03` funcionen directamente.

Configuración recomendada en GitHub:

- **Settings → Pages**
- **Source:** Deploy from a branch
- **Branch:** `main`
- **Folder:** `/ (root)`

Después de cada actualización del inventario CSV, regenerar los datos públicos:

```bash
python3 tools/generate_pages_data.py
```

Luego confirmar y subir los cambios:

```bash
git add _CONTROL/INVENTARIO_ESTACION_LA_LATA.csv assets/inventory-data.js
git commit -m "Actualizar datos del inventario web"
git push
```

## Alcance publicado inicialmente

El sitio web inicial publica las primeras tres carpetas:

- `Carpeta01`: 11 documentos.
- `Carpeta02`: 13 documentos.
- `Carpeta03`: 26 registros de inventario, con control visible de diferencias entre CSV y PDF existentes.

El resto de las carpetas queda en el repositorio para trabajo progresivo de catalogación y publicación.

## Campos de Catalogación

| Campo | Descripción |
|-------|-------------|
| ID_Unico | Correlativo único del inventario |
| Nombre_Normalizado | Nombre técnico del archivo |
| Tipo_Documental | Clasificación (Oficio, Carta, Circular, etc.) |
| Titulo | Título descriptivo del documento |
| Fecha_Exacta | Fecha precisa si existe |
| Fecha_Aproximada | Estimación si no hay fecha exacta |
| Autor_Emisor | Quién produjo el documento |
| Tema_Principal | Asunto central del documento |
| Descripcion_Breve | 2-5 líneas de contexto |
| Palabras_Clave | 5-12 términos para búsqueda |
| Valor_Administrativo | Relevancia para gestión |
| Valor_Historico | Relevancia para historia local |
| Valor_Patrimonial | Relevancia para patrimonio cultural |

## Protocolo de Catalogación

1. **Carga**: Escanear documento y colocar en carpeta física correspondiente
2. **Análisis**: Revisar contenido, tipo, fecha, autor, tema
3. **Nomenclatura**: Generar nombre técnico (LL_CarpetaXX_DOCXXXX.pdf)
4. **Renombramiento**: Actualizar nombre del archivo
5. **Catalogación**: Completar datos en INVENTARIO_ESTACION_LA_LATA.csv
6. **Validación**: Verificar todos los campos según PROTOCOLO_ANALISIS.md
7. **Publicación**: Regenerar `assets/inventory-data.js` y subir los cambios a GitHub

## Manual de uso

Consultar [MANUAL_REPOSITORIO.md](MANUAL_REPOSITORIO.md) para el flujo detallado de carga online, carga desde computadora, búsqueda de documentos y control de calidad.

## Autor del Inventario

**Sergio Pérez** - Especialista en Archivística y Gestión Documental

## Fecha de Inicio

21 de abril de 2026

## Estado del Proyecto

En desarrollo - publicación inicial de `Carpeta01`, `Carpeta02` y `Carpeta03` como ejemplo metodológico para inventarios de bienes culturales.

## Licencia

Municipio de Cardona - Uso Público

---

Para más información, consultar los archivos de protocolo en la carpeta `_CONTROL/`.
