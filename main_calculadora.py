import PySimpleGUI as sg

sg.theme('Black')

jan_alt = 30
jan_com = 50

menu_layout = [['File', ['Save', 'Exit']],
               ['Tools', ['Waiting']],
               ['Help', ['About']]]

layout = [[sg.Menu(menu_layout)],
          [sg.Input('0', size=(int(jan_alt/2),1), font=('Consolas', 20), key='-BOX-'),
           sg.Button('<-', font=('Consolas', 20),key='-BACKARROW-'),
           sg.Button('<-', font=('Consolas', 20),key='-CLEAR-')],

          [sg.Button('7', font=('Consolas', 20),key='-SETE-'),
           sg.Button('8', font=('Consolas', 20),key='-OITO-'),
           sg.Button('9', font=('Consolas', 20),key='-NOVE-'),
           sg.Button('+', font=('Consolas', 20),key='-MAIS-'),
           sg.Button('*', font=('Consolas', 20),key='-VEZES-')],

          [sg.Button('4', font=('Consolas', 20),key='-QUATRO-'),
           sg.Button('5', font=('Consolas', 20),key='-CINCO-'),
           sg.Button('6', font=('Consolas', 20),key='-SEIS-'),
           sg.Button('-', font=('Consolas', 20),key='-MENOS-'),
           sg.Button('/', font=('Consolas', 20),key='-DIVISAO-')],

          [sg.Button('1', font=('Consolas', 20),key='-UM-'),
           sg.Button('2', font=('Consolas', 20),key='-DOIS-'),
           sg.Button('3', font=('Consolas', 20),key='-TRES-'),
           sg.Button('0', font=('Consolas', 20),key='-ZERO-'),
           sg.Button('=', font=('Consolas', 20),key='-IGUAL-')]]



