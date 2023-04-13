from translate import Translator
import translate
import PySimpleGUI as sg #importação das bibliotecas necessárias

layout = [ #criação do layout
    [sg.Text('Frase/Termo:'), sg.Input('', key='entrada'), sg.Button('Traduzir')],
    #na 1 linha cria-se um texto padrão, uma caixa de entrada de texto chaveada como "entrada", e um botão
    [sg.Text('', key='traducao')]
    #na linha 2 cria-se um texto padrão ainda em branco, chaveado como "tradução"
]

window = sg.Window('Tradutor Pt-Br -> En', layout=layout)
#criação da janela com titulo e layout
t = Translator(from_lang='pt-br', to_lang='english')
#criação da variável de tradução, com os parâmetros de tradução

while True: #laço de leitura da janela
    event, values = window.read() #leitura dos eventos e valores da janela
    if event == sg.WINDOW_CLOSED: #laço para o caso do botão fechar for clicado, o laço quebra
        break
    if event == 'Traduzir': #criação do evento ao clicar no botão "Traduzir"
        traducao = t.translate(values['entrada'])
        #a variável "t" irá traduzir o texto e inserir em outra variável
        window['traducao'].update(f'Tradução: {traducao}')
        #na janela será atualizada a mensagem na chave "traducao" para o conteudo traduzido

        #fim do código
