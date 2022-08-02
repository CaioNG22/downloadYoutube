from pytube import YouTube

def downloadVideoYoutube(caminho):

    url = input(str("URL para download: "))
    video = YouTube(url)
    stream = video.streams.get_highest_resolution()
    stream.download(output_path=f"{caminho}")

    print("\nDownload Concluído com Sucesso!\n")

if __name__ == '__main__':

    print("Baixar videos do YouTube\n")
    op = 'sim'
    caminho = input("Informe o caminho: ")

    while op == "sim" or op == "s":
        downloadVideoYoutube(caminho)
        op = input(str("Deseja realizar outro donwload? [s/n]: "))
