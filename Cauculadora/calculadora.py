import PySimpleGUI as sg

sg.theme('Black')

jan_alt = 30
jan_com = 50

menu_layout = [['File', ['Save', 'Exit']],
               ['Tools', ['Waiting']],
               ['Help', ['About']]]

layout = [[sg.Menu(menu_layout)],
          [sg.Input('0', size=(int(jan_alt / 2), 1), font=('Consolas', 20), key='-BOX-'),
           sg.Button('<-', font=('Consolas', 20), key='-BACKARROW-'),
           sg.Button('<-', font=('Consolas', 20), key='-CLEAR-')],

          [sg.Button('7', font=('Consolas', 20), key='-SETE-'),
           sg.Button('8', font=('Consolas', 20), key='-OITO-'),
           sg.Button('9', font=('Consolas', 20), key='-NOVE-'),
           sg.Button('+', font=('Consolas', 20), key='-MAIS-'),
           sg.Button('*', font=('Consolas', 20), key='-VEZES-')],

          [sg.Button('4', font=('Consolas', 20), key='-QUATRO-'),
           sg.Button('5', font=('Consolas', 20), key='-CINCO-'),
           sg.Button('6', font=('Consolas', 20), key='-SEIS-'),
           sg.Button('-', font=('Consolas', 20), key='-MENOS-'),
           sg.Button('/', font=('Consolas', 20), key='-DIVISAO-')],

          [sg.Button('1', font=('Consolas', 20), key='-UM-'),
           sg.Button('2', font=('Consolas', 20), key='-DOIS-'),
           sg.Button('3', font=('Consolas', 20), key='-TRES-'),
           sg.Button('0', font=('Consolas', 20), key='-ZERO-'),
           sg.Button('=', font=('Consolas', 20), key='-IGUAL-')]]


class App():
    def __init__(self):
        self.window = sg.Window('PyCalculator', layout=layout, margins=(0, 0), resizable=True,
                                return_keyboard_events=False)
        self.result = 0
        self.oper = ''
        self.window.read(timeout=1)

        for i in range(1, 5):
            for button in layout[i]:
                button.expand(expand_x=True, expand_y=True)
    finalize = True

    def about(self):
        sg.popup('About', 'Just an example', 'contact me')

    def resulter(self):
        if self.oper == '+':
            return float(self.result) + float(self.values['-BOX-'])
        if self.oper == '-':
            return float(self.result) - float(self.values['-BOX-'])
        if self.oper == '*':
            return float(self.result) * float(self.values['-BOX-'])
        if self.oper == '/':
            return float(self.result) / float(self.values['-BOX-'])

    def start(self):
        while True:
            event, self.values = self.window.read()

            if event in (None, 'Exit', sg.WIN_CLOSED):
                break

            if event in ('About'):
                self.about()

            if event in ('-UM-'):
                if self.values['-BOX-'] == '0':
                    self.window['-BOX-'].update(value='1')
                else:
                    self.window['-BOX-'].update(value=self.values['-BOX-'] + '1')

            if event in ('-DOIS-'):
                if self.values['-BOX-'] == '0':
                    self.window['-BOX-'].update(value='2')
                else:
                    self.window['-BOX-'].update(value=self.values['-BOX-'] + '2')

            if event in ('-TRES-'):
                if self.values['-BOX-'] == '0':
                    self.window['-BOX-'].update(value='3')
                else:
                    self.window['-BOX-'].update(value=self.values['-BOX-'] + '3')

            if event in ('-QUATRO-'):
                if self.values['-BOX-'] == '0':
                    self.window['-BOX-'].update(value='4')
                else:
                    self.window['-BOX-'].update(value=self.values['-BOX-'] + '4')

            if event in ('-CINCO-'):
                if self.values['-BOX-'] == '0':
                    self.window['-BOX-'].update(value='5')
                else:
                    self.window['-BOX-'].update(value=self.values['-BOX-'] + '5')

            if event in ('-SEIS-'):
                if self.values['-BOX-'] == '0':
                    self.window['-BOX-'].update(value='6')
                else:
                    self.window['-BOX-'].update(value=self.values['-BOX-'] + '6')

            if event in ('-SETE-'):
                if self.values['-BOX-'] == '0':
                    self.window['-BOX-'].update(value='7')
                else:
                    self.window['-BOX-'].update(value=self.values['-BOX-'] + '7')

            if event in ('-OITO-'):
                if self.values['-BOX-'] == '0':
                    self.window['-BOX-'].update(value='8')
                else:
                    self.window['-BOX-'].update(value=self.values['-BOX-'] + '8')

            if event in ('-NOVE-'):
                if self.values['-BOX-'] == '0':
                    self.window['-BOX-'].update(value='9')
                else:
                    self.window['-BOX-'].update(value=self.values['-BOX-'] + '9')

            if event in ('-ZERO-'):
                if self.values['-BOX-'] == '0':
                    self.window['-BOX-'].update(value='0')
                else:
                    self.window['-BOX-'].update(value=self.values['-BOX-'] + '0')

            if event in ('-CLEAR-'):
                self.result = 0
                self.window['-BOX-'].update(value=self.result)

            if event in ('-BACKARROW-'):
                self.window['-BOX-'].update(value=self.values['-BOX-'][:-1])

            if event in ('-MAIS-'):
                if self.oper != '':
                    self.result = self.resulter()
                else:
                    self.oper = '+'
                    self.result = self.values['-BOX-']
                self.window['-BOX-'].update(value='')

            if event in ('-MENOS-'):
                if self.oper != '':
                    self.result = self.resulter()
                else:
                    self.oper = '-'
                    self.result = self.values['-BOX-']
                self.window['-BOX-'].update(value='')

            if event in ('-VEZES-'):
                if self.oper != '':
                    self.result = self.resulter()
                else:
                    self.oper = '*'
                    self.result = self.values['-BOX-']
                self.window['-BOX-'].update(value='')

            if event in ('-DIVISAO-'):
                if self.oper != '':
                    self.result = self.resulter()
                else:
                    self.oper = '/'
                    self.result = self.values['-BOX-']
                self.window['-BOX-'].update(value='')

            if event in ('-IGUAL-'):
                self.result = self.resulter()
                self.window['-BOX-'].update(value=self.result)
                self.result = 0
                self.oper = ''


App().start()

