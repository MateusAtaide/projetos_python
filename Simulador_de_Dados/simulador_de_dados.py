import random
import PySimpleGUI as sg

layout = [
    [sg.Text('Deseja lançar o dado?')],
    [sg.Button('SIM'), sg.Button('NÃO')],
    [sg.Text('Aguardando...', key='resultado')],
]

window = sg.Window('Simulador de Dado', layout=layout)

while True:
    event, values = window.Read()
    if event == sg.WINDOW_CLOSED or event == 'NÃO':
        break

    elif event == 'SIM':
        window['resultado'].update('Número: ' + str(random.randint(1, 6)))
