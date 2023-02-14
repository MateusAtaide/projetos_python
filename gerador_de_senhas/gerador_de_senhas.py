import random
import PySimpleGUI as sg
import os
from playsound import playsound


class Passgen:
    def __init__(self):
        sg.theme('Black')
        
        layout = [
            [sg.Text('Site/Software', size=(10, 1)), sg.Input(key='site', size=(20, 1))],
            [sg.Text('E-mail/Usuário', size=(10, 1)), sg.Input(key='usuario', size=(20, 1))],
            [sg.Text('Quantidade de Caracteres'),
             sg.Combo(values=list(range(31)), key='total_chars', default_value=1, size=(3, 1))],
            [sg.Output(size=(32, 5))],
            [sg.Button('Gerar Senha')]
        ]
        self.janela = sg.Window('Gerador de Senha', layout)
    def Iniciar(self):
        while True:
            evento, valores = self.janela.read()
            if evento == sg.WINDOW_CLOSED:
                break
            if evento == 'Gerar Senha':
                nova_senha = self.gerar_senhas(valores)
                print(nova_senha)
                self.salvar_senha(nova_senha,valores)

    def gerar_senhas(self, valores):
        char_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%¨&*'
        chars = random.choices(char_list, k=int(valores['total_chars']))
        new_pass = ''.join(chars)
        return new_pass
    def salvar_senha(self, nova_senha, valores):
        with open('senhas.txt', 'a', newline='') as arquivo:
            arquivo.write(f"Site: {valores['site']}, Usuario: {valores['usuario']}, Nova Senha: {nova_senha}\n")

        print('Arquivo salvo!')

gen = Passgen()
gen.Iniciar()