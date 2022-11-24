import menu
import pygame
import sys

def func():
    print('Hello, world!')

def quit_game():
    pygame.quit()
    sys.exit()

default_menu = menu.menu()
buy_menu = menu.menu()
sell_menu = menu.menu()
upgrade_menu = menu.menu()
property_menu = menu.menu()


default_menu.options.insert(0,('Advance a new day.', None, None))
default_menu.options.insert(0,('Buy a property.', buy_menu, None))
default_menu.options.insert(0,('Sell a property.', sell_menu, None))
default_menu.options.insert(0,('Upgrade a property.', upgrade_menu, None))
default_menu.options.insert(0,('Quit game.', None, quit_game))

buy_menu.options.insert(0,('Return to previous menu.', default_menu, None))
sell_menu.options.insert(0,('Return to previous menu.', default_menu, None))
upgrade_menu.options.insert(0,('Return to previous menu.', default_menu, None))

buy_menu.options.insert(1,('Print "Hello, world!".', None, func))
sell_menu.options.insert(1,('Print "Hello, world!".', None, func))
upgrade_menu.options.insert(1,('Print "Hello, world!".', None, func))
