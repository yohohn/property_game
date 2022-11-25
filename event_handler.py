import pygame
import sys
def event_handler(current_menu, curser):
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                # arrow key up
                if event.key == 1073741906:
                    curser.curser_movement = True
                    curser.curser_direction = True
                # arrow key down 
                elif event.key == 1073741905:
                    curser.curser_movement = True
                    curser.curser_direction = False
                # keyboard enter or numpad enter
                elif event.key == 13 or event.key == 1073741912:
                    current_menu = current_menu.select(curser)
                    
            elif event.type == pygame.KEYUP:
                # arrow key up or arrow key down
                if event.key == 1073741906 or event.key == 1073741905:
                    curser.curser_movement = False
    return current_menu