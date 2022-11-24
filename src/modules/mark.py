import pygame.font

class Mark:
    """Una clase para reportar infomracion sobre puntuacion"""
    def __init__(self, setting, screen, statistic):
        """Inicializa los atributos de registro de puntajes"""
        
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.setting = setting
        self.statistic = statistic

        # Ajustes de fuente para la informacion de puntuacion
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # Prepara la imagen del puntaje inicial
        self.create_point()
        self.create_long_point()

    def create_point(self):
        """Convierte el marcador en una imagen renderizada"""
        self.point_approx = int(round(self.statistic.point, -1))
        point_str = "{:,}".format(self.point_approx)
        self.point_image = self.font.render(point_str, True, self.text_color, self.setting.bg_color)

        # Miestra el puntaje en la esquina superiro derecha de la pantalla
        self.point_rect = self.point_image.get_rect()
        self.point_rect.right = self.screen_rect.right - 20
        self.point_rect.top = 20
    
    def create_long_point(self):
        """Convierte el marcador en una imagen renderizada"""
        self.long_point_approx = int(round(self.statistic.long_point, -1))
        long_point_str = "{:,}".format(self.long_point_approx)
        self.long_point_image = self.font.render(long_point_str, True, self.text_color, self.setting.bg_color)

        # Miestra el puntaje en la esquina superiro derecha de la pantalla
        self.long_point_rect = self.long_point_image.get_rect()
        self.long_point_rect.centerx = self.screen_rect.centerx
        self.long_point_rect.top = self.screen_rect.top

    def show_point(self):
        """Dibuja la puntuacion en la pantalla"""
        self.screen.blit(self.point_image, self.point_rect)
        self.screen.blit(self.long_point_image, self.long_point_rect)