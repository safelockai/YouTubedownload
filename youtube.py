import yt_dlp
import os
import subprocess

def download_video(url, output_path):
    ydl_opts = {
        'format': 'mp4',  # Força o download no formato MP4 se disponível
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',  # Modelo para o nome do arquivo
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Download do vídeo concluído!")
    except Exception as e:
        print(f"Ocorreu um erro ao baixar o vídeo: {e}")

def convert_to_mp4(file_path, output_path):
    output_file = os.path.splitext(file_path)[0] + '.mp4'
    command = [
        'ffmpeg', '-i', file_path, '-c:v', 'libx264', '-c:a', 'aac',
        '-strict', 'experimental', output_file
    ]
    try:
        subprocess.run(command, check=True)
        print(f"Vídeo convertido para MP4: {output_file}")
        os.remove(file_path)  # Remove o arquivo original se a conversão for bem-sucedida
    except subprocess.CalledProcessError as e:
        print(f"Erro ao converter o vídeo: {e}")

def download_audio(url, output_path):
    ydl_opts = {
        'format': 'bestaudio/best',  # Baixa o melhor áudio disponível
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',  # Modelo para o nome do arquivo
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',  # Usa FFmpeg para extrair o áudio
            'preferredcodec': 'mp3',  # Formato de saída do áudio
            'preferredquality': '192',  # Qualidade do áudio
        }],
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Download do áudio concluído!")
    except Exception as e:
        print(f"Ocorreu um erro ao baixar o áudio: {e}")

def main():
    # Solicita a URL do vídeo
    video_url = input("Digite a URL do vídeo: ")

    # Solicita ao usuário escolher o tipo de download
    choice = input("Digite '1' para baixar o vídeo ou '2' para baixar o áudio: ").strip()

    # Caminho para salvar o arquivo
    output_path = '/data/data/com.termux/files/home/storage/downloads'
    
    # Cria o diretório de saída se não existir
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    if choice == '1':
        print("Iniciando o download do vídeo...")
        download_video(video_url, output_path)
        # Verifica se o arquivo baixado não está em MP4 e converte se necessário
        for file_name in os.listdir(output_path):
            if file_name.endswith('.webm'):  # Assumindo que .webm é o formato baixado
                file_path = os.path.join(output_path, file_name)
                convert_to_mp4(file_path, output_path)
    elif choice == '2':
        print("Iniciando o download do áudio...")
        download_audio(video_url, output_path)
    else:
        print("Escolha inválida. Por favor, escolha '1' ou '2'.")

if __name__ == "__main__":
    main()
