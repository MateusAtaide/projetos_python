import random
import PySimpleGUI as sg #importação das bibliotecas

class Passgen: #classe principal da aplicação
    def __init__(self): #função de inicio da janela
        sg.theme('Black') #tema da janela
        
        layout = [
            [sg.Text('Site/Software', size=(10, 1)), sg.Input(key='site', size=(20, 1))],
            #na linha 1 um texto de identificação e uma entrada de texto chaveada como "site"
            [sg.Text('E-mail/Usuário', size=(10, 1)), sg.Input(key='usuario', size=(20, 1))],
            #na linha 2 um texto de identificação e uma entrada de texto chaveada como "usuario"
            [sg.Text('Quantidade de Caracteres'),
             sg.Combo(values=list(range(31)), key='total_chars', default_value=1, size=(3, 1))],
            #na linha 3 uma lista de quatidade de caracteres que a senha irá gerar, chaveada como "total_chars"
            [sg.Output(size=(32, 5))],
            #na linha 4 uma caixa para exibição da senha gerada
            [sg.Button('Gerar Senha')]
            #na linha 5 o botão "Gerar Senha" para criar, gravar e mostrar a senha gerada
        ]
        self.janela = sg.Window('Gerador de Senha', layout)
        #instanciamento do layout da janela
    def Iniciar(self): #função de inicio da aplicação
        while True: #laço de leitura da janela e de valores
            evento, valores = self.janela.read() #leitura da janela
            if evento == sg.WINDOW_CLOSED: #laço para quebrar o laço de leitura ao aperta o botão "fechar"
                break
            if evento == 'Gerar Senha': #laço para executar as funções que serão implementadas a seguir
                nova_senha = self.gerar_senhas(valores)
                print(nova_senha)
                self.salvar_senha(nova_senha, valores)

    def gerar_senhas(self, valores): #função geradora das senhas que recebe os valores de entrada
        char_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%¨&*'
        #lista de caracteres a serem usados na geração de senhas
        chars = random.choices(char_list, k=int(valores['total_chars']))
        #variável que irá receber uma lista de caracteres aleatórios de acordo com a quantidade definida pelo usuário
        new_pass = ''.join(chars)
        #junção de caracteres e uma variável de tipo string
        return new_pass #retorno da variável
    def salvar_senha(self, nova_senha, valores): #função que irá escrever um arquivo de texto com os logins gerados
        with open('senhas.txt', 'a', newline='') as arquivo:
            arquivo.write(f"Site: {valores['site']}, Usuario: {valores['usuario']}, Nova Senha: {nova_senha}\n")
        #criação e formatação do arquivo de texto dentro da pasta do projeto
        print('Arquivo salvo!') #mensagem de sucesso da criação do arquivo de texto

gen = Passgen()
gen.Iniciar()