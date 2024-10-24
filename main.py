import requests
import customtkinter as ctk
from PIL import ImageTk, Image

# --------------- Configs básicas ------------- #

cor1 = "#0a0a0a"  # Preta
cor2 = "#fafcff"  # Branca
cor3 = "#21c25c"  # Verde
cor4 = "#eb463b"  # Vermelha
cor5 = "#dedcdc"  # Cinza
cor6 = "#3080f0"  # Azul

# Configurações da janela principal
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

janela = ctk.CTk()
janela.geometry("300x350")
janela.title("Conversor de Moeda")
janela.resizable(width=False, height=False)

# --------------- Cabeçalho ------------- #
frame_cima = ctk.CTkFrame(janela, width=300, height=60, fg_color=cor6)
frame_cima.grid(row=0, column=0, sticky="nsew")

app_nome = ctk.CTkLabel(frame_cima, text='Conversor de Moeda', font=ctk.CTkFont(size=16, weight="bold"), text_color=cor1)
app_nome.place(relx=0.5, rely=0.5, anchor='center')

# --------------- Conteúdo ------------- #
frame_conteudo = ctk.CTkFrame(janela, width=300, height=290, fg_color=cor5)
frame_conteudo.grid(row=1, column=0, sticky="nsew")

app_moeda = ctk.CTkLabel(frame_conteudo, text='Escolha uma conversão!', text_color=cor1, fg_color=cor2, width=200, height=50, corner_radius=6, font=ctk.CTkFont(size=10, weight="bold"))
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

app_texto_DE = ctk.CTkLabel(frame_conteudo, text='De', font=ctk.CTkFont(size=10, weight="bold"))
app_texto_DE.place(relx=0.29, rely=0.4, anchor='ne')

combo_DE = ctk.CTkComboBox(frame_conteudo, values=moedas, width=100)
combo_DE.place(relx=0.45, rely=0.5, anchor='ne')

app_texto_PARA = ctk.CTkLabel(frame_conteudo, text='Para', font=ctk.CTkFont(size=10, weight="bold"))
app_texto_PARA.place(relx=0.7, rely=0.4, anchor='ne')

combo_PARA = ctk.CTkComboBox(frame_conteudo, values=moedas, width=100)
combo_PARA.place(relx=0.84, rely=0.5, anchor='ne')

app_entry = ctk.CTkEntry(frame_conteudo, width=200, justify='center', font=ctk.CTkFont(size=10, weight="bold"))
app_entry.place(relx=0.5, rely=0.7, anchor='center')

# Função para fazer a requisição à API de conversão de moedas
def converter():
    from_currency = combo_DE.get()
    to_currency = combo_PARA.get()
    amount = app_entry.get()

    if from_currency and to_currency and amount:
        try:
            url = f"https://economia.awesomeapi.com.br/json/last/{from_currency}-{to_currency}"

            response = requests.get(url)
            dados = response.json()

            conversion_key = f"{from_currency}{to_currency}"
            if response.status_code == 200 and conversion_key in dados:
                rate = float(dados[conversion_key]['bid'])
                conversion_result = rate * float(amount)
                app_moeda.configure(text=f'{amount} {from_currency} = {conversion_result:.2f} {to_currency}')
            else:
                app_moeda.configure(text="Erro na conversão!")
        except Exception as e:
            app_moeda.configure(text="Erro de conexão!")
    else:
        app_moeda.configure(text="Preencha todos os campos!")

botao_converter = ctk.CTkButton(frame_conteudo, text='Converter', command=converter, width=200)
botao_converter.place(relx=0.5, rely=0.9, anchor='center')

janela.mainloop()
