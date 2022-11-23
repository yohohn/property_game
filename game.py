import pygame
pygame.init()
import sys
import user_interface, constants, event_handler


game_menu = user_interface.menu()
hello_menu = user_interface.menu()
hello_menu.options['Hello, world!'] = game_menu

for i in range(9):
    game_menu.options['Option ' + str(i)] = hello_menu




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            # arrow key up
            if event.key == 1073741906:
                game_menu.curser_movement = True
                game_menu.curser_direction = True
            # arrow key down 
            elif event.key == 1073741905:
                game_menu.curser_movement = True
                game_menu.curser_direction = False
            # keyboard enter or numpad enter
            elif event.key == 13 or event.key == 1073741912:
                game_menu = game_menu.options[game_menu.curser_selected]
                
        elif event.type == pygame.KEYUP:
            # arrow key up or arrow key down
            if event.key == 1073741906 or event.key == 1073741905:
                game_menu.curser_movement = False


            


    constants.SCREEN.fill(constants.DARK_GRAY)
    

    current_ticks = pygame.time.get_ticks()
    game_menu.print(current_ticks)
    pygame.display.update()
    
    b = constants.CLOCK.get_fps()
    a = constants.CLOCK.tick(60)






