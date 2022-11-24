class Statistics:
    """Seguiminto de las estadisticas del juego"""

    def __init__(self, setting):
        """Inicializa las estadisticas"""
        self.setting = setting
        self.reset_stats()

        # Inicia invasion en un estado activo
        self.game_active = False

        # La puntacion alta nunca debe restablecerse
        self.long_point = 0

    def reset_stats(self):
        """Inicializa estadisticas que pueden cambiar durante el juego"""
        self.ship_rest = self.setting.ship_count
        self.point = 0