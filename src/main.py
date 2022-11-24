import pygame
import functions as fg

from settings import Settings
from modules.ship import Ship
from modules.mark import Mark
from pygame.sprite import Group
from modules.button import Button
from modules.statistics import Statistics

def run_game():

    # Inicializar el juego, las configuraciones y crear un objeto pantalla
    pygame.init()
    setting = Settings()
    screen = pygame.display.set_mode(setting.screen_size)
    pygame.display.set_caption('Aliens Invade')

    # Crea el boton play 
    play_button = Button(setting, screen, "Play")

    # Crea una instancia para almacenar estadisticas del juego y crea un marcador
    statistic = Statistics(setting)
    mark = Mark(setting, screen, statistic)

    # Crear una nave
    ship = Ship(setting, screen)
    # Crear un grupo para almacenar las balas
    bullets = Group()
    # Crear un grupo para almacenar los alien
    aliens = Group()

    # Crea la flota de alienigenas
    fg.create_fleet(setting, screen, ship, aliens)

    # Inicializar el bulce principal del juego
    while True:

        # Escuchar eventos de teclado o de raton
        fg.event_verification(setting, screen, statistic, ship, aliens, bullets, play_button)

        if statistic.game_active:
            # Actualizar la posicion de la nave y las balas
            ship.update()
            fg.update_bullets(setting, screen, statistic, mark, ship, aliens, bullets)
            fg.update_aliens(setting, screen, statistic, ship, aliens, bullets)

        # Actualizar la pantalla
        fg.update_screen(setting, screen, statistic, ship, mark, aliens, bullets, play_button)

if __name__ == '__main__':
    run_game()