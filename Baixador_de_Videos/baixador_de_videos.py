import pytube
import PySimpleGUI as sg

layout = [
    [sg.Text('Insira o link do YouTube:')], [sg.Input(key='link')],
    [sg.Button('Baixar')], [sg.Button('Cancelar')],
    [sg.Text('', key='mensagem')]
]
window = sg.Window('Baixador de Videos', layout=layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Cancelar':
        break
    elif event == 'Baixar' and values['link'] != '':
        link = values['link']
        yt = pytube.YouTube(link)
        yt.streams.get_highest_resolution().download()
        window['mensagem'].update('Download Concluído!')
