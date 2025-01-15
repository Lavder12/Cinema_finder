# music_player.py
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "1"


import pygame
import time

class MusicPlayer:
    def __init__(self, music_file, volume=0.1):
        self.music_file = music_file
        self.volume = volume

    def play_music(self):
        """
        Функция для бесконечного воспроизведения музыки.
        """
        pygame.mixer.init(frequency=44100)
        pygame.mixer.music.load(self.music_file)
        pygame.mixer.music.set_volume(self.volume)  # Установить громкость
        pygame.mixer.music.play(-1)  # -1 означает бесконечное воспроизведение

    @staticmethod
    def fade_out_music(fade_time=5):
        """
        Плавно уменьшает громкость музыки до 0 перед остановкой.
        """
        current_volume = pygame.mixer.music.get_volume()  # Получаем текущую громкость
        fade_steps = 50  # Количество шагов для затухания
        fade_interval = fade_time / fade_steps  # Время между шагами (в секундах)

        for step in range(fade_steps):
            new_volume = current_volume * (1 - step / fade_steps)  # Постепенно уменьшаем громкость
            pygame.mixer.music.set_volume(new_volume)  # Устанавливаем новую громкость
            time.sleep(fade_interval)  # Ждем между шагами

        pygame.mixer.music.stop()  # Останавливаем музыку после затухания
