import tkinter
import customtkinter
from pytube import YouTube


#configurações do sistema
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")
#------------------------

janela = customtkinter.CTk()
janela.geometry("720x480")
janela.title("YOUTUBE DOWLOADER")

def startDowload():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()
        titulo.configure(text=ytObject.title, text_color="white")
        finishDownload.configure(text="")
        video.download()
        finishDownload.configure(text="Conteúdo Baixado!")
    except:
        finishDownload.configure(text="Falha no Download!", text_color="red")

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_download = total_size - bytes_remaining
    porcentagem_de_dowload =  bytes_download / total_size * 100
    print(porcentagem_de_dowload)
    per = str(int(porcentagem_de_dowload))
    porcentagem.configure(text=per + '%')
    porcentagem.update()
    barra.set(float(porcentagem_de_dowload) / 100)
#elementos
#----------------
titulo = customtkinter.CTkLabel(janela, text="BEM VINDO!")
titulo.pack(padx=10,pady=10)

comandInsira = customtkinter.CTkLabel(janela, text="Insira o Link:")
comandInsira.pack(padx=10, pady=10)

url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(janela, width=350, height=40,textvariable=url_var)
link.pack()

#porcentagem de download
porcentagem =customtkinter.CTkLabel(janela, text="0%")
porcentagem.pack()

barra = customtkinter.CTkProgressBar(janela, width=400)
barra.set(0.01)
barra.pack(padx=10, pady=10)

#botao dowload
botao= customtkinter.CTkButton(janela, text="Download", command=startDowload)
botao.pack(padx=10,pady=10)

#mensagem de dowload finalizado
finishDownload = customtkinter.CTkLabel(janela, text="")
finishDownload.pack()








#run code
janela.mainloop()






