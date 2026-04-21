# REPOSITORIO DOCUMENTAL ESTACIÓN LA LATA – CARDONA

## Estructura y Descripción

```
Inventario y repositorio Estación La Lata/
├── Carpeta01/           ← PDFs originales de la carpeta física 01
├── Carpeta02/           ← PDFs originales de la carpeta física 02
├── Carpeta03/           ← PDFs originales de la carpeta física 03
├── ...
├── Carpeta10/           ← PDFs originales de la carpeta física 10
└── _CONTROL/            ← Documentación de control y catalogación
    ├── INVENTARIO_ESTACION_LA_LATA.csv
    ├── PROTOCOLO_ANALISIS.md
    ├── GUIA_RAPIDA.txt
    ├── PLANTILLA_FICHA_CATALOGRAFICA.txt
    └── README.md
```

---

## Archivos de Control

### 1. **INVENTARIO_ESTACION_LA_LATA.csv**
- Base de datos principal de catalogación
- Contiene todos los documentos analizados
- Importable a Excel para gestión completa
- Actualizable en tiempo real conforme se carguen nuevos documentos

**Campos principales:**
- ID único
- Nombre original y normalizado
- Tipo documental
- Fecha, autor, tema
- Descripción, palabras clave
- Valores (administrativo, histórico, patrimonial)
- Estado y observaciones

### 2. **PROTOCOLO_ANALISIS.md**
- Flujo de trabajo paso a paso
- Definiciones de tipos documentales
- Criterios de descripción y palabras clave
- Checklist de validación
- Ejemplos de nomenclatura

### 3. **GUIA_RAPIDA.txt**
- Referencia rápida durante la catalogación
- Convención de nomenclatura resumida
- Tipos documentales comunes
- Checklist abreviado
- Marcas especiales

### 4. **PLANTILLA_FICHA_CATALOGRAFICA.txt**
- Formulario completable para cada documento
- Campos estructurados
- Facilita captura de datos uniformes
- Base para ficha definitiva en Excel

### 5. **README.md**
- Este archivo
- Descripción de la estructura
- Instrucciones de uso general

---

## Convención de Nomenclatura

**Formato obligatorio:**
```
LL_CarpetaXX_DOCXXXX.pdf
```

**Componentes:**
- **LL** = Estación La Lata (identificación del fondo)
- **CarpetaXX** = Número de carpeta física (con dos dígitos: 01, 02, ..., 10, 11, etc.)
- **DOCXXXX** = Número correlativo del documento en esa carpeta (con cuatro dígitos: 0001, 0002, ..., 9999)

**Ejemplos correctos:**
- `LL_Carpeta01_DOC0001.pdf` ← Primer documento de la carpeta 01
- `LL_Carpeta01_DOC0002.pdf` ← Segundo documento de la carpeta 01
- `LL_Carpeta03_DOC0015.pdf` ← Decimoquinto documento de la carpeta 03
- `LL_Carpeta10_DOC0247.pdf` ← Documento 247 de la carpeta 10

**Ejemplos INCORRECTOS (no usar):**
- `LL_Carpeta_1_DOC_1.pdf` ← Falta padding de ceros
- `Oficio_1982_Cardona.pdf` ← Contiene descripción interpretativa
- `Documento_Importante.pdf` ← No sigue convención
- `LL_Carpeta01_Solicitud_DOC0001.pdf` ← Incluye tema

---

## Flujo de Trabajo

### Fase 1: Carga
1. Escanear documento física en formato PDF
2. Cargar en la carpeta digital correspondiente (Carpeta01, Carpeta02, etc.)
3. Nombre provisional durante carga: cualquiera
4. Confirmar que PDF es legible

### Fase 2: Análisis
1. Abrir documento PDF
2. Leer completamente y comprender contenido
3. Identificar:
   - Tipo documental (oficio, carta, acta, etc.)
   - Fecha exacta o aproximada
   - Autor/emisor
   - Destinatario
   - Tema principal
   - Institución vinculada
   - Lugar de referencia

### Fase 3: Descripción
1. Redactar título (máximo 100 caracteres)
2. Escribir descripción breve (2-5 líneas)
3. Asignar 5-12 palabras clave relevantes
4. Evaluar valores archivísticos (administrativo, histórico, patrimonial)
5. Completar campos complementarios

### Fase 4: Normalización
1. Generar nombre técnico: `LL_CarpetaXX_DOCXXXX.pdf`
2. Renombrar archivo PDF en carpeta digital
3. Garantizar trazabilidad con ubicación física

### Fase 5: Registro
1. Completar todos los campos en formulario de ficha catalográfica
2. Copiar datos a INVENTARIO_ESTACION_LA_LATA.csv
3. Revisar consistencia
4. Validar contra duplicados
5. Registrar observaciones y marcar incertidumbres

### Fase 6: Control
1. Verificar que todos los campos están completos
2. Confirmar que no hay datos inventados
3. Marcar datos [inferidos] cuando corresponda
4. Revisar ortografía y coherencia terminológica
5. Validar enlaces entre carpeta física y digital

---

## Tipos Documentales

**Documentos administrativos:**
- Oficio, Memorándum, Resolución, Decreto
- Acta, Expediente, Registro
- Certificado, Solicitud

**Documentos financieros:**
- Factura, Recibo, Comprobante
- Presupuesto, Nómina

**Documentos de información:**
- Listado, Catálogo, Censo
- Periódico, Recorte de prensa, Anuncio

**Documentos técnicos:**
- Mapa, Plano, Esquema
- Informe técnico

**Documentos multimedia:**
- Fotografía, Negativo
- Dibujo, Ilustración

---

## Criterios de Catalogación

### Descripción
- **Máximo:** 5 líneas
- **Contenido:** Nombres, fechas, instituciones, contexto
- **Estilo:** Objetivo, sin interpretación subjetiva
- **Redacción:** Oraciones completas, terminología archivística

**Ejemplo:**
> Oficio del Director de la Estación La Lata dirigido al Ayuntamiento de Cardona, fechado el 12 de marzo de 1982. Solicita autorización y fondos para reparaciones en la canalización principal del sistema de distribución de agua. Incluye estimación de costos y cronograma de obras.

### Palabras Clave
- **Cantidad:** 5-12 términos
- **Tipos:** Nombres, lugares, instituciones, temas, procesos, eventos
- **Formato:** Separadas por comas o por categoría
- **Objetivo:** Facilitar búsqueda futura

**Ejemplo:**
```
agua, infraestructura, reparación, Estación La Lata, Cardona, 
Ayuntamiento, distribución, autorización, 1982, obras, mantenimiento
```

---

## Marcas Especiales

- **[inferido]** → Información deducida del contexto, no explícita en el documento
- **[dudoso]** → Hay incertidumbre sobre la información
- **[incompleto]** → Faltan páginas o el documento está cortado
- **[ilegible]** → No legible o parcialmente ilegible
- **DUPLICADO** → Documento repetido en el fondo
- **PATRIMONIO** → Valor histórico o cultural excepcional

**Uso en observaciones:**
> [Inferido] Autor probable es Juan García basado en firma reconocible

> DUPLICADO: Referencia LL_Carpeta03_DOC0025

> PATRIMONIO: Documento de excepcional valor histórico para la historia local

---

## Acceso a Datos

### Inventario en Excel
1. Abrir `INVENTARIO_ESTACION_LA_LATA.csv` con Excel
2. Importar como tabla para facilitar búsquedas y filtros
3. Aplicar filtros por:
   - Tipo documental
   - Fecha/Año
   - Tema principal
   - Valor patrimonial
   - Estado de legibilidad

### Búsqueda de documentos
- **Por nombre:** Usar convención LL_CarpetaXX_DOCXXXX
- **Por palabras clave:** Búsqueda en columna "Palabras_Clave"
- **Por tema:** Filtro en "Tema_Principal"
- **Por ubicación física:** Referencia en "Carpeta_Fisica"

---

## Validación y Garantía de Calidad

### Antes de finalizar cada documento:
- [ ] Tipo documental identificado correctamente
- [ ] Fecha asignada (exacta o aproximada)
- [ ] Autor/emisor identificado
- [ ] Tema principal definido
- [ ] Descripción redactada (2-5 líneas)
- [ ] Palabras clave asignadas (5-12)
- [ ] Nombre técnico generado correctamente
- [ ] Todos los campos completados
- [ ] Sin datos inventados
- [ ] Incertidumbres registradas como [inferido] o [dudoso]
- [ ] Trazabilidad perfecta: carpeta física = carpeta digital

---

## Próximas Fases (Futuro)

1. **Expansión a más carpetas** según número de carpetas físicas reales
2. **Integración con sistema de gestión documental** (Goobi, Koha, etc.)
3. **Digitalización completa** con OCR revisado
4. **Publicación en repositorio institucional** para acceso público
5. **Vinculación con cronología histórica** y eventos de Cardona
6. **Análisis temático avanzado** para investigación histórica

---

## Responsables

- **Catalogación y análisis:** Especialista en archivística
- **Control de calidad:** Revisor técnico
- **Actualización:** Administrador del repositorio
- **Acceso:** Usuarios autorizados según nivel

---

## Información General

- **Fondo:** Estación La Lata – Cardona
- **Institución:** Municipio de Cardona
- **Fecha de inicio:** 21 de abril de 2026
- **Versión del sistema:** 1.0
- **Responsable:** Gestión del Patrimonio Documental
- **Contacto:** [Completar según corresponda]

---

**Última actualización:** 21 de abril de 2026

