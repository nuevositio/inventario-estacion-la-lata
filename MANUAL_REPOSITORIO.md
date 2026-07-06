# Manual de uso del repositorio documental

Repositorio: `nuevositio/inventario-estacion-la-lata`

Sitio público previsto: `https://nuevositio.github.io/inventario-estacion-la-lata/`

Este repositorio organiza documentos digitalizados de la Estación La Lata de AFE y sirve como ejemplo de trabajo para inventarios de bienes culturales. La regla principal es mantener juntos el archivo digital, su registro de inventario y una nomenclatura estable.

## 1. Estructura

```text
Carpeta01/                         Documentos digitalizados de la carpeta física 01
Carpeta02/                         Documentos digitalizados de la carpeta física 02
Carpeta03/                         Documentos digitalizados de la carpeta física 03
_CONTROL/INVENTARIO_ESTACION_LA_LATA.xlsx  Archivo base de inventario
_CONTROL/INVENTARIO_ESTACION_LA_LATA.csv   Exportación usada por la web
assets/inventory-data.js           Datos públicos generados para GitHub Pages
index.html                         Buscador público
MANUAL_REPOSITORIO.md              Este manual
```

## 2. Convención de nombres

Todos los PDF deben seguir este formato:

```text
LL_CarpetaXX_DOCXXXX.pdf
```

Ejemplo: `LL_Carpeta02_DOC0007.pdf`

La carpeta física y el número de documento deben coincidir con los campos `Carpeta_Fisica`, `Numero_Documento`, `Nombre_Normalizado` y `Ruta_Almacenamiento` del inventario.

## 3. Cargar nuevos documentos online

1. Entrar al repositorio en GitHub.
2. Abrir la carpeta correspondiente, por ejemplo `Carpeta03`.
3. Usar `Add file` y luego `Upload files`.
4. Subir el PDF ya nombrado con la convención oficial.
5. Confirmar el cambio con un mensaje claro, por ejemplo: `Agregar documento LL_Carpeta03_DOC0028`.
6. Actualizar el inventario base `_CONTROL/INVENTARIO_ESTACION_LA_LATA.xlsx`.
7. Exportar o actualizar `_CONTROL/INVENTARIO_ESTACION_LA_LATA.csv`.
8. Regenerar `assets/inventory-data.js` para que el buscador vea el nuevo registro.
9. Confirmar y subir esos cambios.

GitHub Pages se actualiza automáticamente unos minutos después de cada cambio en la rama `main`.

## 4. Cargar documentos desde la computadora

```bash
git pull
cp /ruta/al/documento.pdf Carpeta03/LL_Carpeta03_DOC0028.pdf
```

Después completar o actualizar la fila correspondiente en el inventario y regenerar los datos públicos:

```bash
python3 tools/generate_pages_data.py
git status
git add Carpeta03/LL_Carpeta03_DOC0028.pdf _CONTROL/INVENTARIO_ESTACION_LA_LATA.csv assets/inventory-data.js
git commit -m "Agregar documento LL_Carpeta03_DOC0028"
git push
```

## 5. Buscar documentos como usuario

Desde el sitio de GitHub Pages:

1. Escribir una palabra en el buscador: nombre, tema, año, autor, tipo documental o palabra clave.
2. Filtrar por carpeta física si se conoce el origen.
3. Filtrar por valor patrimonial o estado OCR cuando se necesita priorizar revisión.
4. Abrir el PDF con el botón `Abrir PDF`.
5. Usar `Copiar ruta` para citar o informar el documento exacto.

También se puede buscar directamente en GitHub usando el buscador del repositorio. Para búsquedas masivas, descargar `_CONTROL/INVENTARIO_ESTACION_LA_LATA.csv` y filtrar por columnas.

## 6. Control de calidad

Antes de publicar una carpeta nueva, revisar:

- Que cada PDF tenga una fila en el inventario.
- Que cada fila del inventario apunte a un PDF existente.
- Que no haya nombres duplicados.
- Que `Nivel_Acceso` sea correcto antes de publicar documentos sensibles.
- Que los campos `Titulo`, `Tema_Principal`, `Descripcion_Breve` y `Palabras_Clave` permitan encontrar el documento.

## 7. Criterio de publicación

La web pública inicial muestra las carpetas `Carpeta01`, `Carpeta02` y `Carpeta03`. Las demás carpetas pueden permanecer en proceso hasta que el equipo decida incorporarlas al sitio.
