import random
import PySimpleGUI as sg

layout = [
    [sg.Image(filename='bola_p.png', key='imagem')],
    [sg.Text('Faça a sua Pergunta')],
    [sg.Input(key='Pergunta', do_not_clear=False)],
    [sg.Button('Responda')],
    [sg.Text('', key='Resposta')],
]

window = sg.Window('Bola Oito Da Sorte', layout=layout)

while True:
    event, values = window.Read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'Responda':
        imagem = random.randint(1, 5)
        match imagem:
            case 1:
                sg.popup_auto_close(image='bola_ask_again_later.png')
            case 2:
                sg.popup_auto_close(image='bola_i_have_no_idea.png')
            case 3:
                sg.popup_auto_close(image='bola_no.png')
            case 4:
                sg.popup_auto_close(image='bola_the_answer_is_yes.png')
            case 5:
                sg.popup_auto_close(image='bola_yes.png')
