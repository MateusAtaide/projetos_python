from translate import Translator
import translate
import PySimpleGUI as sg

layout = [
    [sg.Text('Frase/Termo:'), sg.Input('', key='entrada'), sg.Button('Traduzir')],
    [sg.Text('', key='traducao')]
]

window = sg.Window('Tradutor Pt-Br -> En', layout=layout)
t = Translator(from_lang='pt-br', to_lang='english')

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    if event == 'Traduzir':
        traducao = t.translate(values['entrada'])
        window['traducao'].update(f'Tradução: {traducao}')
