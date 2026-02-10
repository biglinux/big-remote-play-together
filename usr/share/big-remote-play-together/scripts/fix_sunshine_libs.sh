#!/bin/bash
# Scripts to fix missing dependencies for Sunshine (libicuuc.so.7* / libicuuc.so.76)
# This script handles missing ICU libraries common after system updates.

if [ "$EUID" -ne 0 ]; then 
    echo "⚠️  Este script precisa de permissões de root."
    exit 1
fi

echo "🔍 Verificando bibliotecas ICU..."

# 1. Try to install legacy package if on Arch-based system (BigLinux/Manjaro)
if command -v pacman &> /dev/null; then
    echo "📦 Tentando instalar icu76 via pacman..."
    pacman -S --needed --noconfirm icu76
    
    if [ $? -eq 0 ]; then
        echo "✅ Pacote icu76 instalado com sucesso."
        exit 0
    fi
fi

# 2. Fallback: Check for existing versions to link (if package install failed)
echo "⚠️  Falha ao instalar pacote, tentando caminhos alternativos..."

FOUND_VER=""
for ver in $(ls /usr/lib/libicuuc.so.* | grep -oE '[0-9]+' | sort -rn | uniq); do
    if [ "$ver" -ge 76 ]; then
        FOUND_VER=$ver
        break
    fi
done

if [ -n "$FOUND_VER" ]; then
    echo "🔗 Criando links simbólicos de v$FOUND_VER para v76..."
    
    ln -sf /usr/lib/libicuuc.so.$FOUND_VER /usr/lib/libicuuc.so.76
    ln -sf /usr/lib/libicudata.so.$FOUND_VER /usr/lib/libicudata.so.76
    ln -sf /usr/lib/libicui18n.so.$FOUND_VER /usr/lib/libicui18n.so.76
    
    echo "✅ Links criados."
    exit 0
else
    echo "❌ Nenhuma versão compatível de libicu encontrada."
    exit 1
fi

