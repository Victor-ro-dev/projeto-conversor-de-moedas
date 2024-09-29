import requests
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

# --------------- Configs básicas ------------- #

cor1 = "#0a0a0a"  # Preta
cor2 = "#fafcff"  # Branca
cor3 = "#21c25c"  # Verde
cor4 = "#eb463b"  # Vermelha
cor5 = "#dedcdc"  # Cinza
cor6 = "#3080f0"  # Azul

janela = Tk()
janela.geometry("300x350")
janela.config(bg=cor2)
janela.resizable(width=False, height=False)

# --------------- Cabeçalho ------------- #
frame_cima = Frame(janela, width=300, height=60, bg=cor3, padx=0, pady=0, relief='flat')
frame_cima.grid(row=0, column=0, sticky=NSEW)

app_nome = Label(frame_cima, width=20, height=1, text='Conversor de moeda', padx=0, relief='flat', anchor='nw', font='ivy 16 bold', bg=cor3, fg=cor1)
app_nome.place(relx=0.6, rely=0.5, anchor='center')

img = Image.open('imagens/conversor.png')
img = img.resize((30, 30), Image.LANCZOS)
img = ImageTk.PhotoImage(img)

app_logo = Label(frame_cima, height=30, image=img, compound=LEFT, padx=10, relief='flat', anchor='nw', bg=cor3)
app_logo.place(x=5, y=13)

# --------------- Conteúdo ------------- #
frame_conteudo = Frame(janela, width=300, height=290, bg=cor5, padx=0, pady=0, relief='flat')
frame_conteudo.grid(row=1, column=0, sticky=NSEW)

app_moeda = Label(frame_conteudo, width=26, height=4, text='Escolha uma conversão!', relief='solid', anchor='center', bg=cor2, fg=cor1, font='ivy 10 bold')
app_moeda.place(relx=0.5, rely=0.2, anchor='center')

moedas = [
    "USD",  # Dólar Americano
    "EUR",  # Euro
    "BRL",  # Real Brasileiro
    "JPY",  # Iene Japonês
    "CHF",  # Franco Suíço
    "CNY",  # Yuan Chinês
    "INR",  # Rupia Indiana
    "RUB",  # Rublo Russo
    "ZAR",  # Rand Sul-Africano
    "MXN",  # Peso Mexicano
    "ARS",  # Peso Argentino
    "KRW",  # Won Sul-Coreano
]


app_texto_DE = Label(frame_conteudo, text='De', width=8, height=1, relief='flat', font='ivy 10 bold', bg=cor5)
app_texto_DE.place(relx=0.29, rely=0.4, anchor='ne')

combo_DE = ttk.Combobox(frame_conteudo, width=8, justify=CENTER, font=('Ivy 12 bold'))
combo_DE.place(relx=0.45, rely=0.5, anchor='ne')
combo_DE['values'] = moedas

app_texto_PARA = Label(frame_conteudo, text='Para', width=8, height=1, relief='flat', font='ivy 10 bold', bg=cor5)
app_texto_PARA.place(relx=0.7, rely=0.4, anchor='ne')

combo_PARA = ttk.Combobox(frame_conteudo, width=8, justify=CENTER, font=('Ivy 12 bold'))
combo_PARA.place(relx=0.84, rely=0.5, anchor='ne')
combo_PARA['values'] = moedas

app_entry = Entry(frame_conteudo, justify='center', width=30, font='ivy 10 bold', relief='solid')
app_entry.place(relx=0.5, rely=0.7, anchor='center')
botao_converter = Button(frame_conteudo, width=26, height=1, text='Converter', relief='raised', overrelief='solid', anchor='center', bg=cor3, fg=cor1, font='ivy 10 bold', command=converter)
botao_converter.place(relx=0.5, rely=0.9, anchor='center')

estilo = ttk.Style(janela)
estilo.theme_use('clam')
janela.mainloop()
