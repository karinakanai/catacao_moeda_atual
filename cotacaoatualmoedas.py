import requests
from tkinter import *

def pegar_cotacoes():

    cotacoes = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,JPY-BRL')
    cotacoes_dic = cotacoes.json()

    cotacao_dolar = cotacoes_dic['USDBRL']['bid']
    cotacao_euro = cotacoes_dic['EURBRL']['bid']
    cotacao_yen = cotacoes_dic['JPYBRL']['bid']

    texto = f'''
    Dólar: {cotacao_dolar}
    Euro: {cotacao_euro}
    Yen: {cotacao_yen}'''

    texto_cotacoes['text'] = texto

janela = Tk()
janela.title('Cotação Atual das Moedas')


texto_orientacao = Label(janela, text = 'Olá! Se você quiser saber as cotações das moedas,\nbasta clicar no botão abaixo que te informarei os valores atualizados!', font='arial 12')
texto_orientacao.grid(column=0, row=0, padx=20, pady=15)

botao = Button(janela, text = 'Buscar cotações do Dólar/Euro/Yen', font='arial 12 bold', bg='green yellow', fg='dark green', command = pegar_cotacoes)
botao.grid(column=0, row=1, padx=20, pady=10)

texto_cotacoes = Label(janela, text='', font='arial 12')
texto_cotacoes.grid(column=0, row=2, padx=20, pady=10)

janela.mainloop()



