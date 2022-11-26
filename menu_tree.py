import menu
import pygame
import sys
import map_tree
import characters, cell

def quit_game():
    pygame.quit()
    sys.exit()

def select_purchase(property):
    global selected_property
    selected_property = property

john = characters.john
default_menu = menu.menu()
buy_menu = menu.menu()
sell_menu = menu.menu()
upgrade_menu = menu.menu()
property_menu = menu.menu()
map_menu = menu.menu()

default_menu.append('Quit game.', None, quit_game)
default_menu.append('Upgrade a property.', upgrade_menu, None)
default_menu.append('Sell a property.', sell_menu, None)
default_menu.append('Buy a property.', buy_menu, None)
default_menu.append('Advance a new day.', None, None)

buy_menu.append('Return to previous menu.', default_menu, None)
sell_menu.append('Return to previous menu.', default_menu, None)
upgrade_menu.append('Return to previous menu.', default_menu, None)
map_menu.append(
    'Cancel the purchase and return to previous menu.', buy_menu, None
)

buy_menu.append('Buy a store', map_menu, select_purchase, cell.store)
