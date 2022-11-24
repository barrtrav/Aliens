import pygame.font

class Button:
    """Clase para crear un boton"""

    def __init__(self, setting, screen, message):
        """Inicializa los atributos del boton"""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Establece las dimsensiones y propiedades del boton
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0) # Verde
        self.text_color = (255, 255, 255) # Negro
        self.font = pygame.font.SysFont(None, 48)

        # Construye el objeto rect del boton y lo centras
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # El mensaje del boton debe prepararse solo una vez
        self.create_message(message)

    def create_message(self, message):
        """Convierte el message en una imagen renderizada y centra el texto en el boton"""
        self.msg_image = self.font.render(message, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # Dibuja el botin en blanco y luego dibuja el mensaje
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
