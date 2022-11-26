import pygame
pygame.init()
import constants, event_handler, characters, curser
import menu_tree, map_tree

current_menu = menu_tree.default_menu

current_cell = map_tree.start_cell

curser.game_curser.select_mode(0b00, current_menu.length)

while True:
    current_ticks = pygame.time.get_ticks()
    current_menu, current_cell = event_handler.event_handler(
        current_menu, current_cell
    )
    constants.SCREEN.fill(constants.DARK_GRAY)
    current_cell.print()

    curser.game_curser.move(current_ticks)
    curser.game_curser.print_curser()
    if curser.game_curser.mode == 0b01:
        current_cell.hover()

    current_menu.print()
    characters.user.print_resources()
    
    pygame.display.update()


    constants.CLOCK.tick(60) 





