import PySimpleGUI as sg
import os
from utils.music_utilities import get_files_inside_directory_not_recursive, play_sound, is_sound_playing, pause_sounds, stop_sounds, unpause
#importação das bibliotecas necesárias, inclusive da pasta utils
sg.theme('Reddit') #escolha do tema

#definição dos layouts da janela
song_title_column = [ #texto de inicio da janela principal com seu chaveamento
    [sg.Text(text='Pressione Play...', justification='center', background_color='black',
             text_color='white', size=(200, 0), font='Tahoma', key='song_name')]
]

player_info = [ #texto sobrea a capa e status da lista de reprodução e seu chaveamento
    [sg.Text('PySimpleGUI Player',
             background_color='black', text_color='white',  font=('Tahoma', 10), key='player_info')]
]

currently_playing = [ #texto com o titulo da musica sendo reproduzida e seu chaveamento
    [sg.Text(background_color='black', size=(200, 0), text_color='white',
             font=('Tahoma', 10), key='currently_playing')]
]
#bloco de imagens que serão utilizadas para botões e e capa
imagem_voltar = 'Images\\back.png'
imagem_proxima = 'Images\\next.png'
imagem_play = 'Images\\play.png'
imagem_pause = 'Images\\pause.png'
imagem_album = 'Images\\songs.png'

main = [ #criasção do layout da janela
    [sg.Canvas(background_color='black', size=(480, 20), pad=None)],#cria um fundo preto
    [sg.Column(layout=player_info, justification='c',
               element_justification='c', background_color='black')],
    [ #insere o texto de inicio já definido acima
        sg.Canvas(background_color='black', size=(40, 350), pad=None),
        sg.Image(filename=imagem_album,
                 size=(350, 350), pad=None),
        sg.Canvas(background_color='black', size=(40, 350), pad=None)
    ],#insere a imagem do album ao centro
    [sg.Canvas(background_color='black', size=(480, 10), pad=None)],
    [sg.Column(song_title_column, background_color='black',
               justification='c', element_justification='c')],
    #alinha o texto da titulo da musica ainda sem titulo
    [sg.Text('_'*80, background_color='black', text_color='white')],#cria uma linha separando os botões
    [#bloco de layout dos botões
        sg.Canvas(background_color='black', size=(64, 150), pad=(0, 0)),
        sg.Image(pad=(10, 0), filename=imagem_voltar, enable_events=True,
                 size=(64, 64), key='previous', background_color='black'),
        sg.Image(filename=imagem_play,
                 size=(64, 64), pad=(10, 0), enable_events=True, key='play', background_color='black'),
        sg.Image(filename=imagem_pause,
                 size=(64, 64), pad=(10, 0), enable_events=True, key='pause', background_color='black'),
        sg.Image(filename=imagem_proxima, enable_events=True,
                 size=(64, 64), pad=(10, 0), key='next', background_color='black'),
    ],
    [sg.Column(layout=currently_playing, justification='c',
               element_justification='c', background_color='black', pad=None)]
    #alinha o titulo da musica depois de carregada a pasta
]

#cria a janela com titulo e layout
window = sg.Window('Player de Músicas', layout=main, size=(
    480, 730), background_color='black', finalize=True, grab_anywhere=True, resizable=False)

directory = sg.popup_get_folder('Selecione a pasta de músicas!')
#cria um popup no inicio da aplicação para capturar o diretório dos arquivos

#utiliza as funções do arquivo utils para capturar as informações do diretório
songs_in_directory = get_files_inside_directory_not_recursive(directory)
song_count = len(songs_in_directory)
current_song_index = 0

def update_song_display():
    #a apartir das informações contidas no diretório dos arquivos atualiza o nome da música exibido
    window['song_name'].update(os.path.basename(
        songs_in_directory[current_song_index]))
    window['currently_playing'].update(
        f'Playing: {os.path.basename(songs_in_directory[current_song_index])}')

while True: #laço para leitura de eventos e valores
    event, values = window.read()#leitura de eventos e valores
    if event == sg.WIN_CLOSED:#ao apertar o botão "fechar" o laço de leitura quebra
        break
    elif event == 'play': #laço para o evento play, verifica se existe uma musica reproduzindo,
        #se não reproduz o que houver na lista
        if is_sound_playing():
            pass
        if is_sound_playing() == False:
            play_sound(songs_in_directory[current_song_index])
            update_song_display()

    elif event == 'pause': #usa a função da biblioteca pygame para pausar a musica
        if is_sound_playing():
            pause_sounds()
        else:
            unpause()
        pass

    elif event == 'next': #laço do evento "next"
        #avança a contagem da lista de músicas para a que está reproduzindo e passa para próxima música
        if current_song_index + 1 < song_count:
            stop_sounds()
            current_song_index += 1
            play_sound(songs_in_directory[current_song_index])
            update_song_display()

        else: #se o contador estiver chagado ao limite do indice da lista, gera a mensagem abaixo
            window['player_info'].update("Chegou ao fim da lista!")
            pass

    elif event == 'previous': #laço do evento "previous"
        #reduz a contagem da lista de músicas para a que está reproduzindo e retorna para a música anterior
        if current_song_index + 1 <= song_count and current_song_index > 0:
            stop_sounds()
            current_song_index -= 1
            play_sound(songs_in_directory[current_song_index])
            update_song_display()
        else: #se estiver na primeira música, o contador chegará no limite a lista e irá gerar a mensagem abaixo
            window['player_info'].update("Chegou ao fim da lista!")

     #fim do código