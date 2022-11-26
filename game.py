import pygame
pygame.init()
import constants, event_handler, characters, curser
import menu_tree, map_tree

john = characters.john
current_space = menu_tree.default_menu
cell = map_tree.start_cell
game_curser = curser.curser()
cell_curser = map_tree.cell_curser
game_curser.select_mode(0b00,len(current_space.options)-1)

while True:
    current_ticks = pygame.time.get_ticks()
    current_space = event_handler.event_handler(game_curser, current_space)
    constants.SCREEN.fill(constants.DARK_GRAY)

    game_curser.move(current_ticks)
    game_curser.print_curser()



    cell.print_cell()
    current_space.print()
    john.print_resources()
    
    pygame.display.update()


    constants.CLOCK.tick(60)   




