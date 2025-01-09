# main.py
from music_player import MusicPlayer
from application import Application

if __name__ == '__main__':
    # Создание объектов для управления музыкой и основным приложением
    music_file = "resources/Promise.wav"
    music_player = MusicPlayer(music_file)
    music_player.play_music()
   # Запуск основного приложения
    app = Application()
    app.run()

    # Плавное затухание музыки перед завершением
    music_player.fade_out_music(fade_time=2)
