import pygame
pygame.init()
import constants, event_handler, characters, curser
import menu_tree, map_tree

john = characters.john
current_menu = menu_tree.default_menu
current_cell = map_tree.start_cell
game_curser = curser.curser()
game_curser.select_mode(0b00, current_menu.length   )

while True:
    current_ticks = pygame.time.get_ticks()
    current_menu, current_cell = event_handler.event_handler(
        game_curser, current_menu, current_cell
    )
    constants.SCREEN.fill(constants.DARK_GRAY)

    current_cell.print()

    game_curser.move(current_ticks)
    game_curser.print_curser()

    current_menu.print()
    john.print_resources()
    
    pygame.display.update()


    constants.CLOCK.tick(60)   




