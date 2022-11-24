import pygame
pygame.init()
import constants, event_handler, menu_tree

current_menu = menu_tree.default_menu
while True:
    current_menu = event_handler.event_handler(current_menu)

    constants.SCREEN.fill(constants.DARK_GRAY)
    
    current_ticks = pygame.time.get_ticks()
    
    current_menu.print(current_ticks)
    
    pygame.display.update()
    
    b = constants.CLOCK.get_fps()
    a = constants.CLOCK.tick(60)






