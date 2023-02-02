import PySimpleGUI as sg #importação da biblioteca

sg.theme('DarkAmber') #implementação de cores a janela

layout=[[sg.Text('Olá Mundo!')],#adiciona um texto a 1ª linha
        [sg.Text('Digite alguma coisa:'), sg.InputText('texto')],#adiciona um texto e uma caixa de input na 2ª linha, já com um texto padrão
        [sg.Text('Arquivo:'), sg.Input(), sg.FileBrowse()],#adiciona texto, caixa de input e um buscador de arquivos na 3ª linha
        [sg.OK(), sg.Cancel()]]#adiciona botões 'OK' e 'Cancelar' na 4ª linha 

programa = sg.Window('Nome do Programa', layout) #Cria o programa, e informa o nome na barra de título e qual variável que vai ter o layout descrito

while True: #laço de execução do programa
    evento, valores = programa.read()#leitura do programa 
    if evento == None or evento == 'Cancel': #se for fechado ou cancelado o loop vai quebrar
        break
programa.close()#termina o programa