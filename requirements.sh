#!/bin/bash

# Atualiza o Termux e instala o Python
pkg update && pkg upgrade -y
pkg install python -y

# Instala o pip se não estiver instalado
pkg install python-pip -y

# Instala o yt-dlp via pip
pip install yt-dlp

# Instala o FFmpeg
pkg install ffmpeg -y

# Cria o diretório de saída se não existir
mkdir -p /data/data/com.termux/files/home/storage/downloads

echo "Instalação concluída. Todos os pré-requisitos foram instalados."
