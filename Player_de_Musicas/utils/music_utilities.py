import os
from pygame import mixer #importação da função mixer da biblioteca pygame

mixer.init() #inicializador da função

def get_files_inside_directory_not_recursive(directory):
    # função para retornar as informações do diretório de músicas para a aplicação
    directories = []
    for (root, dirs, files) in os.walk(directory):
        for file in files:
            directories.append(root + os.sep + file)
    return directories

def play_sound(sound_path): #funções de leitura e reprodução de musicas
    mixer.music.load(sound_path)
    mixer.music.play()

def stop_sounds(): #função de parada de musicas
    mixer.music.stop()

def pause_sounds(): #função de pause de musicas
    mixer.music.pause()

def unpause(): #função para retirada da pausa de musicas
    mixer.music.unpause()

def is_sound_playing(): #função de status de reprodução
    if mixer.music.get_busy() == True:
        return True
    return False



