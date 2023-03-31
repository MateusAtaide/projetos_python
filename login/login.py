import PySimpleGUI as sg #importação da biblioteca

layout = [ #inicia-se o layout da janela
    [sg.Text('Usuário')], #Na 1ª linha é colocado um texto para identificar o campo "usuário"
    [sg.Input(key='usuario', do_not_clear=False)],
    #Na 2ª linha é colocado um campo para entrar com o nome de usuário
    #É chaveado e programado com o argumento de limpeza automática do campo
    [sg.Text('Senha')], #Na 3ª linha é colocado um texto para identificar o campo "senha"
    [sg.Input(key='senha', password_char='*', do_not_clear=False)],
    #Na 4ª linha é colocado um campo para entrar com a senha
    #É chaveado, programado com um argumento para substituir os caracteres por "*" e
    #programado com o argumento de limpeza automática do campo
    [sg.Button('Cadastrar')], #Na 5ª linha é criado o botão de cadastrar
    [sg.Button('Login')], #Na 6ª linha é criado o botão de login
    [sg.Text('', key='mensagem')],
    #Na 7ª linha é criado um campo de mensagem ainda vazio, mas que será atualizado pelo seu chaveamento
] #Terminado o layout da janela

window = sg.Window('Login', layout=layout)
#Cria o programa, e informa o nome na barra de título e qual variável que vai ter o layout descrito

while True: #laço de execução do programa
    event, values = window.read() #leitura do programa
    if event == sg.WINDOW_CLOSED: #se for fechado o loop vai quebrar
        break
    elif event == 'Cadastrar':
        #se for selecionado o botão "Cadsatrar", serão executados o seguintes comandos
        if (len(values['usuario'].strip()) == 6) and (len(values['senha'].strip()) == 6):
            #neste comando são testados se o tamanho dos valores dos campos são iguais a 6 caracteres
            usuario_criado = values['usuario'].lower()
            #uma variável recebe os valores do campo "usuário" em caixa baixa
            senha_criada = values['senha']
            #uma variável recebe os valores do campo "senha"
            window['mensagem'].update('Usuário ,"' + usuario_criado + '" criado com sucesso!')
            #no campo "mensagem" será exibido o nome do usuário criado, dentro de uma mensagem de sucesso
        else:
            window['mensagem'].update('Preenchimento Inválido!')
            #caso as condições do laço if não forem cumpridas,
            # será mostrada uma mensagem de erro para repreenchimento dos campos
    elif event == 'Login': #ao selecionar o botão "Login", os comando abaixo serão executados
        usuario = values['usuario']
        #uma variável receberá os valores da variavel que continha os valores de "usuário"
        senha = values['senha']
        # uma variável receberá os valores da variavel que continha os valores de "senha"
        if senha == senha_criada and usuario == usuario_criado:
            #são comparadas as variáveis do bloco de cadastro com as do bloco de login
            window['mensagem'].update('Login realizado com sucesso!')
            #se a comparação for positiva, uma mensagem de sucesso será atualizada no campo "mensagem"
        else:
            window['mensagem'].update('Usuario ou senha incorretos!')
            # se a comparação for negativa, uma mensagem de erro será atualizada no campo "mensagem"

