import random
import PySimpleGUI as sg #importação das bibliotecas

layout = [
    [sg.Text('Deseja lançar o dado?')],#adiciona um texto a 1ª linha
    [sg.Button('SIM'), sg.Button('NÃO')], #adiciona dois botões na 2ª linha
    [sg.Text('Aguardando...', key='resultado')],
    #adiciona uma mensagem na 3ª linha e uma chave para atualização dos valores da mensagem
]

window = sg.Window('Simulador de Dado', layout=layout)
#Cria o programa, e informa o nome na barra de título e qual variável que vai ter o layout descrito

while True: #laço de execução do programa
    event, values = window.Read() #leitura do programa
    if event == sg.WINDOW_CLOSED or event == 'NÃO':
        #se for fechado ou selecionado o botão "NÃO", o loop vai quebrar
        break

    elif event == 'SIM': #se for selecionado o botão "SIM" executará os comandos da próxima linha
        window['resultado'].update('Número: ' + str(random.randint(1, 6)))
        #A mensagem chaveada na 3ª linha é atualizada com um númeo randômico entre 1 e 6
