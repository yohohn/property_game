import pygame
import constants, curser
class playable_character():
    def __init__(self):
        self.money = 0
        self.update_money(100000)
        self.stored_property = None
        self.stored_location = None
        self.owned_properties = set()
    
    def buy_property(self, cell):
        location = self.stored_property.buy_class()
        location.set_image(cell.location_size, location.color)
        location.set_coords(curser.game_curser.location)
        cell.locations['{}x{}'.format(*curser.game_curser.location)] = location
        self.owned_properties.add(location)

    def update_money(self, change):
        self.money += change
        resource_text = '$' + str(self.money)
        self.surface_string = constants.FONT.render(
            resource_text, True, constants.WHITE
        )
        self.location = constants.SCREEN_WIDTH - (len(resource_text) + 1) * 12

    def calc_turn(self):
        net_change = 0
        for owned_property in self.owned_properties:
            net_change += owned_property.income - owned_property.expense
        self.update_money(net_change)

    # print top right for stuff like money
    def print_resources(self):
        constants.SCREEN.blit(self.surface_string, (self.location,5))

user = playable_character()
