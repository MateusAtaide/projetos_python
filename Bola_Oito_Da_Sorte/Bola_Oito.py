import random
import PySimpleGUI as sg

layout = [
    [sg.Text('Faça a sua Pergunta')],
    [sg.Image(filename='bola_p1.png')],
    [sg.Input(key='Pergunta', do_not_clear=False)],
    [sg.Button('Responda Para Mim')],
    [sg.Text('', key='Resposta')],
]

window = sg.Window('Bola Oito Da Sorte', layout=layout)

while True:
    event, values = window.Read()
    if event == sg.WINDOW_CLOSED:
        break