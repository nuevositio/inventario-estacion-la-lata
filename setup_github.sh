#!/bin/bash

# 🚀 Setup GitHub - Script Automatizado
# Uso: ./setup_github.sh

set -e

echo "╔════════════════════════════════════════════════════════════════╗"
echo "║  SETUP GITHUB - INVENTARIO ESTACIÓN LA LATA                   ║"
echo "╚════════════════════════════════════════════════════════════════╝"
echo ""

# Verificar que tenemos credenciales de Git
echo "📋 Verificando configuración de Git..."
git config --global user.name > /dev/null 2>&1 || {
    echo "❌ Error: Git no está configurado"
    echo "Ejecuta primero:"
    echo "  git config --global user.name 'Tu Nombre'"
    echo "  git config --global user.email 'tu@email.com'"
    exit 1
}

USER_NAME=$(git config --global user.name)
USER_EMAIL=$(git config --global user.email)
echo "✅ Usuario: $USER_NAME <$USER_EMAIL>"
echo ""

# Pedir nombre de usuario GitHub
read -p "📝 Ingresa tu usuario de GitHub: " GITHUB_USER

if [ -z "$GITHUB_USER" ]; then
    echo "❌ Usuario de GitHub requerido"
    exit 1
fi

REPO_NAME="Inventario-Estacion-La-Lata"

echo ""
echo "🔧 Configuración:"
echo "  Usuario GitHub: $GITHUB_USER"
echo "  Repositorio: $REPO_NAME"
echo "  URL SSH: git@github.com:$GITHUB_USER/$REPO_NAME.git"
echo "  URL HTTPS: https://github.com/$GITHUB_USER/$REPO_NAME.git"
echo ""

# Preguntar por método de autenticación
echo "¿Qué método de autenticación prefieres?"
echo "1) SSH (recomendado si tienes clave configurada)"
echo "2) HTTPS (Token o credentials)"
read -p "Selecciona (1 o 2): " AUTH_METHOD

if [ "$AUTH_METHOD" = "1" ]; then
    REMOTE_URL="git@github.com:$GITHUB_USER/$REPO_NAME.git"
    echo "📡 Usando SSH"
elif [ "$AUTH_METHOD" = "2" ]; then
    REMOTE_URL="https://github.com/$GITHUB_USER/$REPO_NAME.git"
    echo "📡 Usando HTTPS"
else
    echo "❌ Opción inválida"
    exit 1
fi

echo ""
echo "⚠️  PASOS MANUALES EN GITHUB:"
echo "1. Ve a https://github.com/new"
echo "2. Repository name: $REPO_NAME"
echo "3. Description: 'Inventario y catalogación de Estación La Lata - Cardona'"
echo "4. Visibility: Public o Private (tu preferencia)"
echo "5. NO inicialices con README, .gitignore o LICENSE"
echo "6. Click 'Create repository'"
echo ""
read -p "¿Ya creaste el repositorio en GitHub? (s/n): " REPO_CREATED

if [ "$REPO_CREATED" != "s" ]; then
    echo "⏸️  Crea el repositorio primero en https://github.com/new"
    exit 0
fi

echo ""
echo "🔗 Conectando repositorio local a remoto..."
git remote add origin "$REMOTE_URL" 2>/dev/null || {
    echo "⚠️  Remote ya existe, actualizando..."
    git remote set-url origin "$REMOTE_URL"
}

echo "✅ Remote configurado"
echo ""

# Mostrar estado
git remote -v

echo ""
echo "📤 Haciendo primer push..."
git push -u origin main

echo ""
echo "✅ ¡SETUP COMPLETADO!"
echo ""
echo "Repositorio en línea: https://github.com/$GITHUB_USER/$REPO_NAME"
echo ""

