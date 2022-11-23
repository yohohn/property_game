import menu




default_menu = menu.menu()
buy_menu = menu.menu()
sell_menu = menu.menu()
upgrade_menu = menu.menu()
property_menu = menu.menu()


default_menu.options['Advance a new day.'] = property_menu
default_menu.options['Buy a property.'] = buy_menu
default_menu.options['Sell a property.'] = sell_menu
default_menu.options['Upgrade a property.'] = upgrade_menu


buy_menu.options['Return to previous menu'] = default_menu
sell_menu.options['Return to previous menu'] = default_menu
upgrade_menu.options['Return to previous menu'] = default_menu

for i in range(9):
    i += 1
    buy_menu.options['Buy property ' + str(i)] = property_menu
    sell_menu.options['Sell property ' + str(i)] = property_menu
    upgrade_menu.options['Upgrade property ' + str(i)] = property_menu

property_menu.options['Return to main menu'] = default_menu