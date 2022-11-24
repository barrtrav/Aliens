import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Sirve para manejar las balas disparadas desde la nave"""

    def __init__(self, setting, screen, ship):
        super(Bullet, self).__init__()
        self.screen = screen

        # Crea un bala rect en (0,0) y luego establece las pos
        self.rect = pygame.Rect(0, 0, setting.bullet_width, setting.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Almacena la posicion de la bala como un valor decimal
        self.y = float(self.rect.y)

        self.color = setting.bullet_color
        self.bullet_speed_factor = setting.bullet_speed_factor

    def update(self):
        """Mueve la bala hacia arriba en la pantalla"""

        # Actualiza la posicion decimal de la bala
        self.y -= self.bullet_speed_factor

        # Actualiza la posicion de rect
        self.rect.y = self.y

    def draw_bullet(self):
        """Dibuja la bala en la pantalla"""
        pygame.draw.rect(self.screen, self.color, self.rect)