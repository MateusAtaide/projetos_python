#janela unica
import PySimpleGUI as sg

layout = [[sg.Text('My one shoot page')], #Linha 1
          [sg.InputText("Escreva aqui", text_color='grey')], #linha 2
          [sg.Submit(), sg.Cancel()]] #Linha 3

window = sg.Window('Window Title', layout)

event, values = window.read()
window.close()

text_input = values[0]
sg.popup('You entered:', text_input)



