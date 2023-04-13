import PySimpleGUI as sg #importação das bibliotecas necessárias

def criar_janela_inicial(): #função de criação do layout da janela
    sg.theme('Dark')#tema da janela
    linha = [
        [sg.Checkbox(''), sg.Input('')]
        #criação de um layout de linha com uma entrada de chqcagem e ma caixa de texto
    ]
    layout = [ #criação do layout padrão
        [sg.Frame('Tarefas', layout=linha, key='container')],
        #na linha 1 é criado um quadro que vai ter imbutido os layouts de linha, e chaveado como "container"
        [sg.Button('Nova Tarefa'), sg.Button('Resetar')]
        #na linha 2 são criados dois botões
    ]
    return sg.Window('Todo List', layout=layout, finalize=True) #retorno da função será a própria janela

janela = criar_janela_inicial() #atribuição de função à variável

while True: #laço de leitura da janela
    event, values = janela.read() #leitura de eventos e valores da janela
    if event == sg.WINDOW_CLOSED: #laço para o caso do botão fechar for clicado, o laço quebra
        break
    elif event == 'Nova Tarefa': #criação do evento para o botão "Nova Tarefa"
        janela.extend_layout(janela['container'], [[sg.Checkbox(''), sg.Input('')]])
        #cria novas linhas dentro da variável janela
    elif event == 'Resetar': #criação do evento para o botão "Resetar"
        janela.close() #limpa e fecha a janela
        janela = criar_janela_inicial() #cria uma nova janela limpa

    #fim do código
