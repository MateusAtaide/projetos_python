import PySimpleGUI as sg #mportação de biblioteca

sg.theme('Black') #definição do tema a ser usado na janela

jan_alt = 30 #definição de altura da janela
jan_com = 50 #definição do comprimento da janela

menu_layout = [['File', ['Save', 'Exit']], #estrutura de menu com botões padrão
               ['Tools', ['Waiting']],
               ['Help', ['About']]]

layout = [[sg.Menu(menu_layout)], # na linha 1 utiliza-se o menu já definido
          [sg.Input('0', size=(int(jan_alt / 2), 1), font=('Consolas', 20), key='-BOX-'),
           sg.Button('<-', font=('Consolas', 20), key='-BACKARROW-'),
           sg.Button('AC', font=('Consolas', 20), key='-CLEAR-')],
            #na linha 2 cria-se uma caixa de texto e botões para as funções de apagar e limpar
            #com seus respectivos chaveamentos e parametros

          [sg.Button('7', font=('Consolas', 20), key='-SETE-'),
           sg.Button('8', font=('Consolas', 20), key='-OITO-'),
           sg.Button('9', font=('Consolas', 20), key='-NOVE-'),
           sg.Button('+', font=('Consolas', 20), key='-MAIS-'),
           sg.Button('*', font=('Consolas', 20), key='-VEZES-')],
            #na linha 3 criam-se botões para as funções e numeros
            #com seus respectivos chaveamentos e parametros

          [sg.Button('4', font=('Consolas', 20), key='-QUATRO-'),
           sg.Button('5', font=('Consolas', 20), key='-CINCO-'),
           sg.Button('6', font=('Consolas', 20), key='-SEIS-'),
           sg.Button('-', font=('Consolas', 20), key='-MENOS-'),
           sg.Button('/', font=('Consolas', 20), key='-DIVISAO-')],
          # na linha 4 criam-se botões para as funções e numeros
          # com seus respectivos chaveamentos e parametros

          [sg.Button('1', font=('Consolas', 20), key='-UM-'),
           sg.Button('2', font=('Consolas', 20), key='-DOIS-'),
           sg.Button('3', font=('Consolas', 20), key='-TRES-'),
           sg.Button('0', font=('Consolas', 20), key='-ZERO-'),
           sg.Button('=', font=('Consolas', 20), key='-IGUAL-')]]
            # na linha 5 criam-se botões para as funções e numeros
            # com seus respectivos chaveamentos e parametros
class App(): #criação da classe principal
    def __init__(self): #função de inicialização
        self.window = sg.Window('Calculadora PySimpleGUI', layout=layout, margins=(0, 0), resizable=True,
                                return_keyboard_events=False)
        #Ccriação da janela com titulo, layout, margens, tamanho ajustável de janela e sem entrada pelo teclado
        self.result = 0
        #inicia com valor zero na tela
        self.oper = ''
        #inicia sem operção
        self.window.read(timeout=1)
        #leitura da janela com tempo de 1 milisegundo para leitura

        for i in range(1, 5): #parametrização de expanção dinamica dos botões em conjunto com a janela
            for button in layout[i]:
                button.expand(expand_x=True, expand_y=True)
    finalize = True
    #finaliza a parametrizaçõa da janela
    def about(self): #função pra mostrar um popup ao clicar em "About"
        sg.popup('Sobre', 'Programa Calculadora Versão 0.0', 'Contato:00000000')

    def resulter(self): #bloco de funções para chamada das operções da cauculadora
        if self.oper == '+':
            return float(self.result) + float(self.values['-BOX-'])
        #ao apertar o '+' pega os valores digitados na caixa e soma
        if self.oper == '-':
            return float(self.result) - float(self.values['-BOX-'])
        # ao apertar o '-' pega os valores digitados na caixa e subtrai
        if self.oper == '*':
            return float(self.result) * float(self.values['-BOX-'])
        # ao apertar o '*' pega os valores digitados na caixa e multiplica
        if self.oper == '/':
            return float(self.result) / float(self.values['-BOX-'])
        # ao apertar o '/' pega os valores digitados na caixa e divide
    def start(self): #função para iniciar a leitura de eventos e valores
        while True: #laço para leitura de eventos e valores
            event, self.values = self.window.read()#leitura de eventos e valores
            if event in (None, 'Exit', sg.WIN_CLOSED):
                #ao apertar o botão "fechar" ou "exit" o laço de leitura quebra
                break
            if event in ('About'): #ao clicar em "about" é mostrado o popup já configurado
                self.about()
            if event in ('-UM-'):
                if self.values['-BOX-'] == '0':
                    self.window['-BOX-'].update(value='1')
                else:
                    self.window['-BOX-'].update(value=self.values['-BOX-'] + '1')
            #bloco de códigos para o botão 1, ao apertá-lo o valor na tela muda de 0 para 1,
            # ou se ja houver um caractere 1, isere mais 1 -> 11...1

            if event in ('-DOIS-'): #mesmo procedimento do bloco do botão 1
                if self.values['-BOX-'] == '0':
                    self.window['-BOX-'].update(value='2')
                else:
                    self.window['-BOX-'].update(value=self.values['-BOX-'] + '2')

            if event in ('-TRES-'):#mesmo procedimento do bloco do botão 1
                if self.values['-BOX-'] == '0':
                    self.window['-BOX-'].update(value='3')
                else:
                    self.window['-BOX-'].update(value=self.values['-BOX-'] + '3')

            if event in ('-QUATRO-'):#mesmo procedimento do bloco do botão 1
                if self.values['-BOX-'] == '0':
                    self.window['-BOX-'].update(value='4')
                else:
                    self.window['-BOX-'].update(value=self.values['-BOX-'] + '4')

            if event in ('-CINCO-'):#mesmo procedimento do bloco do botão 1
                if self.values['-BOX-'] == '0':
                    self.window['-BOX-'].update(value='5')
                else:
                    self.window['-BOX-'].update(value=self.values['-BOX-'] + '5')

            if event in ('-SEIS-'):#mesmo procedimento do bloco do botão 1
                if self.values['-BOX-'] == '0':
                    self.window['-BOX-'].update(value='6')
                else:
                    self.window['-BOX-'].update(value=self.values['-BOX-'] + '6')

            if event in ('-SETE-'):#mesmo procedimento do bloco do botão 1
                if self.values['-BOX-'] == '0':
                    self.window['-BOX-'].update(value='7')
                else:
                    self.window['-BOX-'].update(value=self.values['-BOX-'] + '7')

            if event in ('-OITO-'):#mesmo procedimento do bloco do botão 1
                if self.values['-BOX-'] == '0':
                    self.window['-BOX-'].update(value='8')
                else:
                    self.window['-BOX-'].update(value=self.values['-BOX-'] + '8')

            if event in ('-NOVE-'):#mesmo procedimento do bloco do botão 1
                if self.values['-BOX-'] == '0':
                    self.window['-BOX-'].update(value='9')
                else:
                    self.window['-BOX-'].update(value=self.values['-BOX-'] + '9')

            if event in ('-ZERO-'):#mesmo procedimento do bloco do botão 1
                if self.values['-BOX-'] == '0':
                    self.window['-BOX-'].update(value='0')
                else:
                    self.window['-BOX-'].update(value=self.values['-BOX-'] + '0')

            if event in ('-CLEAR-'): #limpa os valores do input e atualiza para zero
                self.result = 0
                self.window['-BOX-'].update(value=self.result)

            if event in ('-BACKARROW-'): #apaga as ultimas posições da string digitada através de slice
                self.window['-BOX-'].update(value=self.values['-BOX-'][:-1])

            if event in ('-MAIS-'):
                #bloco chama a função da operação digitada e atualiza na tela e nos paramentros das variáveis
                if self.oper != '':
                    self.result = self.resulter()
                else:
                    self.oper = '+'
                    self.result = self.values['-BOX-']
                self.window['-BOX-'].update(value='')

            if event in ('-MENOS-'): #mesmo comportamento do bloco de adição, para subtração
                if self.oper != '':
                    self.result = self.resulter()
                else:
                    self.oper = '-'
                    self.result = self.values['-BOX-']
                self.window['-BOX-'].update(value='')

            if event in ('-VEZES-'): #mesmo comportamento do bloco de adição, para multiplicação
                if self.oper != '':
                    self.result = self.resulter()
                else:
                    self.oper = '*'
                    self.result = self.values['-BOX-']
                self.window['-BOX-'].update(value='')

            if event in ('-DIVISAO-'): #mesmo comportamento do bloco de adição, para divisão
                if self.oper != '':
                    self.result = self.resulter()
                else:
                    self.oper = '/'
                    self.result = self.values['-BOX-']
                self.window['-BOX-'].update(value='')

            if event in ('-IGUAL-'): #chama as variáveis de resultados e atualiza na tela
                self.result = self.resulter()
                self.window['-BOX-'].update(value=self.result)
                self.result = 0 #zera a varíavel para ser usada novamente
                self.oper = '' #limpa a variável para ser utilizada novamente

App().start() #iniciador da classe

#fim do código

