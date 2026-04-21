# 🚀 Guía de Configuración GitHub

## Paso 1: Crear Repositorio en GitHub

### Opción A: Vía Web (Recomendado)
1. Ir a https://github.com/new
2. **Repository name:** `Inventario-Estacion-La-Lata` (o similar)
3. **Description:** "Inventario y catalogación profesional de archivos de Estación La Lata - Cardona"
4. **Visibility:** Public (si es documentación pública) o Private (si es restringido)
5. **Opciones:**
   - ❌ NO inicializar con README (ya tenemos)
   - ❌ NO agregar .gitignore (ya tenemos)
   - ❌ NO agregar licencia (definir primero)
6. Click "Create repository"

### Opción B: Vía GitHub CLI
```bash
gh repo create Inventario-Estacion-La-Lata \
  --description "Inventario y catalogación de Estación La Lata - Cardona" \
  --public \
  --source=. \
  --remote=origin \
  --push
```

---

## Paso 2: Conectar Repositorio Local a Remoto

### Con HTTPS (sin clave SSH):
```bash
git remote add origin https://github.com/TU_USUARIO/Inventario-Estacion-La-Lata.git
git branch -M main
git push -u origin main
```

### Con SSH (recomendado si ya tienes SSH configurada):
```bash
git remote add origin git@github.com:TU_USUARIO/Inventario-Estacion-La-Lata.git
git branch -M main
git push -u origin main
```

---

## Paso 3: Verificar Conexión

```bash
git remote -v
# Debería mostrar:
# origin  https://github.com/TU_USUARIO/Inventario-Estacion-La-Lata.git (fetch)
# origin  https://github.com/TU_USUARIO/Inventario-Estacion-La-Lata.git (push)
```

---

## Consideraciones de Seguridad

### Datos Sensibles a Considerar:
- ⚠️ PDFs contienen documentos históricos (revisar si hay info sensible)
- ⚠️ Metadatos archivísticos (¿publicar o mantener privado?)
- ✅ CSV de inventario (públicamente accesible)

### Recomendación:
- Repositorio **PRIVADO** para preservar patrimonio
- O repositorio **PÚBLICO** con licencia Creative Commons

---

## Estructura de Ramas Recomendada

```
main (catalogación completada)
 ↓
develop (trabajo en progreso)
 ├── feature/carpeta03-catalogation
 ├── feature/ocr-improvements
 └── docs/metadata-standards
```

---

## Token de GitHub (si necesitas HTTPS sin SSH)

1. Ir a: https://github.com/settings/tokens
2. Click "Generate new token"
3. Scopes necesarios: `repo` (acceso a repositorios)
4. Copiar token y usarlo como contraseña en el push

**Alternativa moderna: Personal Access Token (Fine-grained)**
- Mejor control de permisos
- Token con expiración

---

## Primera Sincronización

Después de conectar el remoto:

```bash
# Ver estado actual
git status

# Hacer push del historial local
git push -u origin main

# Verificar que todo está sincronizado
git log --oneline
```

---

## Próximos Pasos

1. ✅ Crear repositorio en GitHub
2. ✅ Configurar acceso (HTTPS o SSH)
3. ✅ Hacer primer push
4. 📋 Añadir colaboradores (si es necesario)
5. 📋 Proteger rama `main` (require reviews)
6. 📋 Configurar Actions (CI/CD para validación)

