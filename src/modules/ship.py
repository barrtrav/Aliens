import pygame

class Ship :
    """Sirve para gestionar el comportamiento de la nave"""

    def __init__(self, setting, screen):
        """Inicializa la nave y establece su posicion de partida"""
        
        self.screen = screen
        self.setting = setting

        # Carga la imagen de la nave y obtiene su rect
        self.image = pygame.image.load("../images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Empieza cada nueva nave en la parte inferior de la pantalla
        self.rect.bottom = self.screen_rect.bottom
        self.rect.centerx = self.screen_rect.centerx
        
        # Almacena un valor decimal para el centro de la nave
        self.center = float(self.rect.centerx)

        # Bandera de movieminto
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Actualiza la posicion de la nave segun las banderas de movimiento"""
        
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.setting.ship_speed_factor
        
        if self.moving_left and self.rect.left > 0:
            self.center -= self.setting.ship_speed_factor

        # Actualiza el objeto rect desde self.center
        self.rect.centerx = self.center

    def blitme(self):
        """Dibuja la nave en su ubicacion actual"""

        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Centra la nave en la pantalla"""
        self.center = self.screen_rect.centerx