import pygame
import sys
def event_handler(curser, current_menu, current_cell):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            # escape
            if event.key == 27:
                curser.location = 0
                current_menu = current_menu.select(curser)
            # keyboard enter or numpad enter
            elif event.key == 13 or event.key == 1073741912:
                current_menu = current_menu.select(curser)
            # tab
            elif event.key == 9:
                curser.tab(current_menu, current_cell)
            elif event.key == pygame.K_UP:
                curser.movement = 0b1000
            elif event.key == pygame.K_DOWN:
                curser.movement = 0b0100
            elif event.key == pygame.K_LEFT:
                curser.movement = 0b0010
            elif event.key == pygame.K_RIGHT:
                curser.movement = 0b0001
            
    
    return current_menu, current_cell
