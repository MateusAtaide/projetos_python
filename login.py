import PySimpleGUI as sg
import getpass

layout = [
    [sg.Text('Usuário')],
    [sg.Input(key='usuario')],
    [sg.Text('Senha')],
    [sg.Input(key='senha', password_char='*')],
    [sg.Button('Cadastrar')],
    [sg.Button('Login')],
    [sg.Text('', key='mensagem')],
]

window = sg.Window('Login', layout=layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'Cadastrar':
        if (values['usuario'] != '') or (values['senha'] != ''):
            usuario_criado = values['usuario']
            senha_criada = values['senha']
            window['mensagem'].update('Usuário criado!')
        else:
            window['mensagem'].update('Preenchimento Inválido!')
    elif event == 'Login':
        usuario = values['usuario']
        senha = values['senha']
        if senha == senha_criada and usuario == usuario_criado:
            window['mensagem'].update('Login feito com sucesso!')
        else:
            window['mensagem'].update('Usuario ou senha incorretos!')

