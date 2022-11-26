import pygame
import constants
class playable_character():
    def __init__(self):
        
        # thinking properties should be a list of tuples
        # each tuple should be (x,y), coordinates of the property
        self.properties = []

        self.money = 0
        self.update_money(1000)
        
    
    def update_money(self, change):
        self.money += change
        resource_text = '$' + str(self.money)
        self.surface_string = constants.FONT.render(
            resource_text, True, constants.WHITE
        )
        self.location = constants.SCREEN_WIDTH - (len(resource_text) + 1) * 12

    # print top right for stuff like money
    def print_resources(self):
        constants.SCREEN.blit(self.surface_string, (self.location,5))

john = playable_character()