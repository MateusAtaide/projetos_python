import PySimpleGUI as sg

layout = [
    [sg.Text('Usuário')],
    [sg.Input(key='usuario', do_not_clear=False)],
    [sg.Text('Senha')],
    [sg.Input(key='senha', password_char='*', do_not_clear=False)],
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
        try:
            if (len(values['usuario'].strip()) == 6) and (len(values['senha'].strip()) == 6):
                usuario_criado = values['usuario'].lower()
                senha_criada = values['senha']
                window['mensagem'].update('Usuário ,"' + usuario_criado + '" criado com sucesso!')
            else:
                window['mensagem'].update('Preenchimento Inválido!')
        except:
            window['mensagem'].update('Preenchimento Inválido2!')
    elif event == 'Login':
        usuario = values['usuario']
        senha = values['senha']
        if senha == senha_criada and usuario == usuario_criado:
            window['mensagem'].update('Login realizado com sucesso!')
        else:
            window['mensagem'].update('Usuario ou senha incorretos!')

