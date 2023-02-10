import random
import PySimpleGUI as sg

layout = [
    [sg.Image(filename='bola_p.png', key='-Image-')],
    [sg.Text('Faça a sua Pergunta')],
    [sg.Input(key='Pergunta', do_not_clear=False)],
    [sg.Button('Responda')],
    [sg.Text('', key='Resposta')],
]

window = sg.Window('Bola Oito Da Sorte', layout=layout)

#imagens = [(sg.popup_no_buttons(image='bola_ask_again_later.png')),
 #          (sg.popup_no_buttons(image='bola_i_have_no_idea.png')),
  #         (sg.popup_no_buttons(image='bola_no.png')),
   #        (sg.popup_no_buttons(image='bola_the_answer_is_yes.png')),
    #       (sg.popup_no_buttons(image='bola_yes.png'))
     #      ]

while True:
    event, values = window.Read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'Responda':
        imagem = random.randint(1, 5)
        if imagem == 1:
            sg.popup_no_buttons(image='bola_ask_again_later.png')
        elif imagem == 2:
            sg.popup_no_buttons(image='bola_i_have_no_idea.png')
        elif imagem == 3:
            sg.popup_no_buttons(image='bola_no.png')
        elif imagem == 4:
            sg.popup_no_buttons(image='bola_the_answer_is_yes.png')
        elif imagem == 5:
            sg.popup_no_buttons(image='bola_yes.png')
