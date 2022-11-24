import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Sirve para representar un solo alienigena en la flota"""
    def __init__(self, setting, screen):
        """Iniciliza el alien y establece su posicion inicial"""
        super(Alien, self).__init__()

        self.screen = screen
        self.setting = setting
        
        # Carga la imagen del alien y establece su atributo rect
        self.image = pygame.image.load("../images/alien.bmp")
        self.rect = self.image.get_rect()

        # Inicia cada nuevo alien serca de la parte superiror izquierda 
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Almacena la posicion exacta del alien 
        self.x = float(self.rect.x)
    
    def blitme(self):
        """Dibuja el alien en su ubicacion actual"""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """Devuelve verdadero si el alien esta en el borde de la pantalla"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

        return False

    def update(self):
        """Mueve el alien a la derecha"""
        self.x += (self.setting.alien_speed_factor * self.setting.fleet_direction)
        self.rect.x = self.x