import menu
import pygame
import sys
import map_tree
import properties, characters

def quit_game():
    pygame.quit()
    sys.exit()

def buy_property():
    map_tree.start_cell.change_property((1,1),properties.store(), john)

def select_purchase(property):
    global selected_property
    selected_property = property

john = characters.john
curser = menu.menu_curser()
default_menu = menu.menu()
buy_menu = menu.menu()
sell_menu = menu.menu()
upgrade_menu = menu.menu()
property_menu = menu.menu()
map_menu = menu.menu()



default_menu.options.insert(0,('Advance a new day.', None, None))
default_menu.options.insert(0,('Buy a property.', buy_menu, None))
default_menu.options.insert(0,('Sell a property.', sell_menu, None))
default_menu.options.insert(0,('Upgrade a property.', upgrade_menu, None))
default_menu.options.insert(0,('Quit game.', None, quit_game))

buy_menu.options.insert(0,('Return to previous menu.', default_menu, None))
sell_menu.options.insert(0,('Return to previous menu.', default_menu, None))
upgrade_menu.options.insert(0,('Return to previous menu.', default_menu, None))
map_menu.options.insert(
    0,('Cancel the purchase and return to previous menu.', buy_menu, select_purchase, None)
)

buy_menu.options.append(
    ('Buy a store', map_menu, select_purchase, properties.store())
)

