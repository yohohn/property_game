import pygame
import sys
import menu, map_tree, characters

def quit_game():
    pygame.quit()
    sys.exit()

def select_purchase(property):
    if property == None:
        if characters.user.stored_property != None:
            characters.user.update_money(+characters.user.stored_property.cost)
            characters.user.stored_property = None
    elif property.cost < characters.user.money:
        characters.user.update_money(-property.cost)
        characters.user.stored_property = property
    
def iter_turn():
    characters.user.calc_turn()

default_menu = menu.menu(0b00000000, None)
buy_menu = menu.menu(0b00000001, default_menu)
buy_map_menu = menu.menu(0b10000001, buy_menu)

default_menu.append('Quit game.', None, quit_game)
default_menu.append('Buy a property.', buy_menu, None)
default_menu.append('Advance a new day.', None, iter_turn)
default_menu.append_text('Press tab to select map location.')

buy_menu.append('Return to main menu.', default_menu, None)
for buyable_building in map_tree.BUYABLE_BUILDINGS:
    buy_menu.append(
        buyable_building.buy_menu_string, buy_map_menu, select_purchase, buyable_building
    )
buy_menu.append_text('{:20} {:>10} {:>10} {:>10}'.format('to Purchase','Cost','Income','Expense'))
buy_menu.append_text('{:20} {:>10} {:>10} {:>10}'.format('Select Property Name','Purchase','Weekly','Weekly'))


buy_map_menu.append(
    'Cancel the purchase and return to buy menu.', buy_menu, select_purchase, None
)
buy_map_menu.append_text('Press tab to select map location.')