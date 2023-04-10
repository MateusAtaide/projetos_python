import random
import PySimpleGUI as sg #importação das bibliotecas

layout = [ #inicia-se o layout da janela
    [sg.Image(filename='bola_p.png', key='imagem')],
    #No campo da 1ª linha é colocada uma imagem e cria-se uma chave de valor para ela
    #Essa imagem deve ser inserida na pasta do projeto
    [sg.Text('Faça a sua Pergunta')], #Na 2ª linha é inserida uma mensagem ao usuário
    [sg.Input(do_not_clear=False)],
    #Na 3ª linha é aberto um campo de texto para o usuário
    # é criada um argumento para que esse campo seja limpo e reutilizado
    [sg.Button('Responda')] #Na 4ª linha é criado o botão de respostas
]

window = sg.Window('Bola Oito Da Sorte', layout=layout)
#Cria o programa, e informa o nome na barra de título e qual variável que vai ter o layout descrito

while True: #laço de execução do programa
    event, values = window.Read() #leitura do programa
    if event == sg.WINDOW_CLOSED: #se for fechado o loop vai quebrar
        break
    elif event == 'Responda': #Se for selecionado o botão são executados os comandos abaixo
        imagem = random.randint(1, 5) #Uma variável recebe uma valor randômico entre 1 e 5
        match imagem: #É criado um suíte de casos para os valores da variável
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

            #De acordo com o número que a variável receber,
            #será gerada uma janela popup com uma imagem de resposta e botôes para fecha-la
        #fim do código
