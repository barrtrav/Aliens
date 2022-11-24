import sys
import pygame

from time import sleep
from modules.alien import Alien
from modules.bullet import Bullet

def event_keyup_verification(event, ship):
    """Responde a las pulsaciones de teclas"""

    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def event_keydown_verification(event, setting, screen, ship, bullets):
    """Responde a las pulsaciones de teclas"""

    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(setting, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()        

def event_verification(setting, screen, statistic, ship, aliens, bullets, play_button):
    """Responde a las pulsaciones de tecla y a los eventos del raton"""

    for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
            elif event.type == pygame.KEYUP:
                event_keyup_verification(event, ship)
            elif event.type == pygame.KEYDOWN:
                event_keydown_verification(event, setting, screen, ship, bullets)             
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                check_play_button(setting, screen, statistic, play_button, ship, aliens, bullets, mouse_x, mouse_y)

def check_play_button(setting, screen, statistic, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    """Comineza un nuevo juego cuando el jugador hace click en play"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not statistic.game_active:
        # Restablece la configuraciones del juego
        setting.init_dynamic_setting()

        # Ocultar el cursor del mouse
        pygame.mouse.set_visible(False)
        # Restablece las estadisticas del juego
        statistic.reset_stats()
        statistic.game_active = True

        # Vacia la lista de aliens y balas
        aliens.empty()
        bullets.empty()

        # Crea una nueva flota y centra la nave
        create_fleet(setting, screen, ship, aliens)
        ship.center_ship()

def update_screen(setting, screen, statistic, ship, mark, aliens, bullets, play_button):
    """Actualiza las imagenes en la pantalla y pasa a la nueva pantalla"""
    
    # Volver a dibujar la pantalla durante cada pasada por el bucle
    screen.fill(setting.bg_color)
    # Vuelve a dibujar todas las balas detras de la nave y de los extraterrestres
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    
    ship.blitme()
    aliens.draw(screen)

    # Dibuja la infomracion de la puntuacion
    mark.show_point()

    # Dibuja el boton de play si el juego esta inactivo
    if not statistic.game_active:
        play_button.draw_button()

    # Hacer visible la pantalla dibujada mas reciente
    pygame.display.flip()

def update_bullets(setting, screen, statistic, mark, ship, aliens, bullets):
    """Actualiza la posicion de las balas y elimina las antiguas"""

    # Actualiza las posiciones de las balas
    bullets.update()

    # Deshace las balas que han desaparecido
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_alient_collisions(setting, screen, statistic, mark, ship, aliens, bullets)

def check_bullet_alient_collisions(setting, screen, statistic, mark, ship, aliens, bullets):
    """Responde a las colsisiones entre bala y aliens"""

    # Elimina las balas y los aliens que hayan chocados
    collision = pygame.sprite.groupcollide(bullets, aliens, True, True)
    
    if collision:
        for aliens in collision.values():
            statistic.point += setting.alien_point * len(aliens)
            mark.create_point()
        check_long_point(statistic, mark)
    
    if len(aliens) == 0:
        # Destruye las balas existente y crea una nueva floata
        bullets.empty()
        setting.increment_speed()
        create_fleet(setting, screen, ship, aliens)

def check_long_point(statistic, mark):
    """Verifica si existe un puntaje mas alto"""
    if statistic.long_point < statistic.point:
        statistic.long_point = statistic.point
        mark.create_long_point()

def fire_bullet(setting, screen, ship, bullets):
    """Dispara una bala si aun no ha alcanzado el limites"""
    # Crea una nueva bala y la agrega al grupo de bala
    if len(bullets) < setting.bullet_allowed:
        new_bullet = Bullet(setting, screen, ship)
        bullets.add(new_bullet)

def get_number_alien_x(setting, alien_width):
    """Determina el numero de alienigenas que caben en una flota"""
    available_space_x = setting.screen_width - 2 * alien_width
    number_alien_x = int(available_space_x / (2 * alien_width))
    return number_alien_x

def get_number_rows(setting, ship_height, alien_height):
    """Determina el numero de filas de alien que se ajustan en la pantalla"""
    available_space_y = setting.screen_height - (3 * alien_height) - ship_height
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def create_alien(setting, screen, aliens, alien_number, row_number):
    """Crea un alien y lo coloca en una fila"""
    alien = Alien(setting, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def create_fleet(setting, screen, ship, aliens):
    """Crea una flota completa de alienigenas"""

    # Crea un alien y encuntra el numero de alien seguidos
    # El espacio entre cada alien es igual a un ancho del alien
    alien = Alien(setting, screen)
    number_alien_x = get_number_alien_x(setting, alien.rect.width)
    number_rows = get_number_rows(setting, ship.rect.height, alien.rect.height)

    # Crea la flota de alien
    for row_number in range(number_rows):
        for alien_number in range(number_alien_x):
            create_alien(setting, screen, aliens, alien_number, row_number)

def check_fleet_edges(setting, aliens):
    """Responde apropiada si algun alien a llegado a un borde"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(setting, aliens)
            break

def change_fleet_direction(setting, aliens):
    """Desciende toda la floata y cambia la direccion de la flota"""
    for alien in aliens.sprites():
        alien.rect.y += setting.fleet_drop_speed
    setting.fleet_direction *= -1

def ship_shock(setting, screen, statistic, ship, aliens, bullets):
    """Responde a una nave siendo golpead por un alien"""

    if statistic.ship_rest > 0:
        # Disminuye naves restantes
        statistic.ship_rest -= 1

        # Vacia la lista de aliens y balas
        aliens.empty()
        bullets.empty()

        # Crea una nueva flota y centra la nave
        create_fleet(setting, screen, ship, aliens)
        ship.center_ship()

        # Pausa
        sleep(1)
    else:
        statistic.game_active = False
        pygame.mouse.set_visible(True)

def check_alins_bord(setting, screen, statistic, ship, aliens, bullets):
    """Comprueba si algun alien a llegado al final de la pantalla"""
    screen_rect = screen.get_rect()

    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # Trata esto de la misma forma que si la nave fuera golpeada
            ship_shock(setting, screen, statistic, ship, aliens, bullets)
            break

def update_aliens(setting, screen, statistic, ship, aliens, bullets):
    """Comprueba si la flota esta al borde 
    y luego actualiza las posiciones de todos los aliens de la flota"""
    check_fleet_edges(setting, aliens)
    aliens.update()

    # Busca colisiones de aliens con nave
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_shock(setting, screen, statistic, ship, aliens, bullets)
    
    # Busca aliens que golpea la parte inferiro de la pantalla
    check_alins_bord(setting, screen, statistic, ship, aliens, bullets) 