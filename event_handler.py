import pygame
import sys
import characters, curser
def event_handler(current_menu, current_cell):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            # escape
            if event.key == 27:
                curser.game_curser.location = 0
                current_menu = current_menu.select()
            # keyboard enter or numpad enter
            elif event.key == 13 or event.key == 1073741912:
                if curser.game_curser.mode == 0b00:
                    current_menu = current_menu.select()
                elif curser.game_curser.mode == 0b01:
                    current_menu = current_cell.select(current_menu)
            # tab
            elif event.key == 9:
                curser.game_curser.tab(current_menu, current_cell)

            elif event.key == pygame.K_UP:
                curser.game_curser.movement = 0b1000
            elif event.key == pygame.K_DOWN:
                curser.game_curser.movement = 0b0100
            elif event.key == pygame.K_LEFT:
                curser.game_curser.movement = 0b0010
            elif event.key == pygame.K_RIGHT:
                curser.game_curser.movement = 0b0001
            
    
    return current_menu, current_cell
