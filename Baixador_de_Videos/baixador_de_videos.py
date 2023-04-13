import pytube
from pytube.exceptions import RegexMatchError
import PySimpleGUI as sg #importação das bibliotecas necessárias

layout = [ #criação do layout
    [sg.Text('Insira o link do YouTube:')], [sg.Input(key='link')],
    #na linha 1  e 2 criam-se: um texto padrão uma caixa de texto e   para inserção de dados e chaveada com "link"
    [sg.Button('Baixar'), sg.Button('Cancelar')],
    #na linha 3 criam-se dois botões
    [sg.Text('', key='mensagem')]
    #na linha 4 cria-se uma caixa de texto vazia e com chaveamento de "mensagem"
]
window = sg.Window('Baixador de Videos', layout=layout)
#criação da janela com titulo e layout

while True: #laço de leitura da janela
    event, values = window.read() #leitura dos eventos e valores da janela
    if event == sg.WINDOW_CLOSED or event == 'Cancelar':
        #laço para o caso do botão fechar ou "Cancelar" for clicado, o laço quebra
        break
    try:
        event == 'Baixar' and values['link'] != ''
        # teste para o evento do botão "Baixar", se for clicado e se a caixa de texto "link" não estiver vazia
        link = values['link'] #guarda os valores de link em uma variável
        yt = pytube.YouTube(link) #captura o link através da função da biblioteca Pytube e insere em uma variável
        yt.streams.get_highest_resolution().download()
        #utiliza mais uma função da biblioteca, agora para fazer o dowload do link na maior qualidade disponível
        window['mensagem'].update('Download Concluído!') #atualiza o campo "mensagem" com uma mensagem de sucesso
    except RegexMatchError:
        window['mensagem'].update('Link inválido!') #tratamento de erro de URL inávilda

        #fim do código

