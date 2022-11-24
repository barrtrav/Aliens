class Settings:
    """Sirve para almacenar todas las configuraciones del juego"""

    def __init__(self):
        """Iniciliza las configuraciones del juego"""      
        
        self.screen_width = 800 #1200
        self.screen_height = 600 #800 
        
        self.screen_size = (self.screen_width, self.screen_height)
        
        self.bg_color = (230, 230, 230)

        # Configuraciones de la nave
        self.ship_count = 3

        # Configuraciones de balas
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3

        # Configuraciones de alien
        self.fleet_drop_speed = 10
        # Que tan rapido se acelera el juego
        self.speed_scale = 2
        # Que tan rapido aumenta los valores de punto por aliens
        self.point_scale = 1.5

        self.init_dynamic_setting()

    def init_dynamic_setting(self):
        """Inicializa la configuracion que cambia a lo largo del juego"""
        self.ship_speed_factor = 5
        self.alien_speed_factor = 5
        self.bullet_speed_factor = 5
        
        # fleet_direction, cuando es 1 representa a la derecha
        # si es -1 representa a la izquierda
        self.fleet_direction = 1

        # Puntuacion
        self.alien_point = 50

    def increment_speed(self):
        """Aumenta la configuracion de velocidad y los valores de puntos por aliens"""
        self.ship_speed_factor *= self.speed_scale
        self.alien_speed_factor *= self.speed_scale
        self.bullet_speed_factor *= self.speed_scale

        self.alien_point += int(self.alien_point * self.point_scale)