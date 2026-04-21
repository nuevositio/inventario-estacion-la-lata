# Inventario y Repositorio Documental - Estación La Lata

Proyecto de catalogación y gestión documental de la Estación La Lata del Municipio de Cardona.

## Descripción

Sistema de inventario y repositorio para organización, catalogación y preservación digital de documentos históricos y administrativos de la Estación La Lata.

## Estructura del Repositorio

```
├── Carpeta01/          ← Documentos digitalizados (carpeta física 01)
├── Carpeta02/          ← Documentos digitalizados (carpeta física 02)
├── ...
├── Carpeta25/          ← Documentos digitalizados (carpeta física 25)
└── _CONTROL/           ← Documentación de control y catalogación
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

## Autor del Inventario

**Sergio Pérez** - Especialista en Archivística y Gestión Documental

## Fecha de Inicio

21 de abril de 2026

## Estado del Proyecto

En desarrollo - Fase inicial de catalogación de Carpeta01

## Licencia

Municipio de Cardona - Uso Público

---

Para más información, consultar los archivos de protocolo en la carpeta `_CONTROL/`.
