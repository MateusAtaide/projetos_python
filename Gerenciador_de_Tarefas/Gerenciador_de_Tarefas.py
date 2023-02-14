import PySimpleGUI as sg

def criar_janela_inicial():
    sg.theme('Dark')
    linha = [
        [sg.Checkbox(''), sg.Input('')]
    ]
    layout = [
        [sg.Frame('Tarefas', layout=linha, key='container')],
        [sg.Button('Nova Tarefa'), sg.Button('Resetar')]
    ]
    return sg.Window('Todo List', layout=layout, finalize=True)

janela = criar_janela_inicial()

while True:
    event, values = janela.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'Nova Tarefa':
        janela.extend_layout(janela['container'], [[sg.Checkbox(''), sg.Input('')]])
    elif event == 'Resetar':
        janela.close()
        janela = criar_janela_inicial()
