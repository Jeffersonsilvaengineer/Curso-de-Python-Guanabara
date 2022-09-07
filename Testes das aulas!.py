import requests
from tkinter import *

def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']

    texto = f'''
    Dólar: {cotacao_dolar}
    Euro: {cotacao_euro}
    BTC: {cotacao_btc}'''
    texto_cotacoes['text'] = texto
    print(texto)


janela = Tk()
janela.title('Cotação do dia!')
janela.geometry('300x160')
texto_orientacao = Label(janela, text='Clique no botão para ver as cotaçãoes das moedas')
texto_orientacao.grid(column=0, row=0, padx=5, pady=5)
botao = Button(janela, text='Buscar cotações!',command=pegar_cotacoes)
botao.grid(column=0, row=1, padx=5, pady=5)
texto_cotacoes = Label(janela, text='')
texto_cotacoes.grid(column=0, row=2, padx=5, pady=5)

janela.mainloop()


