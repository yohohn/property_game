import pygame
pygame.init()
import constants, event_handler, characters
import menu_tree, map_tree

john = characters.john
current_menu = menu_tree.default_menu
cell = map_tree.start_cell
curser = menu_tree.curser
cell_curser = map_tree.cell_curser

while True:
    current_menu = event_handler.event_handler(current_menu, curser)

    constants.SCREEN.fill(constants.DARK_GRAY)
    
    current_ticks = pygame.time.get_ticks()
    
    current_menu.print(curser, current_ticks)
    john.print_resources()
    cell.print_cell()
    pygame.display.update()
    
    b = constants.CLOCK.get_fps()
    a = constants.CLOCK.tick(60)






