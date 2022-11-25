import pygame
import constants
class playable_character():
    def __init__(self):
        self.money = 1000
        # thinking properties should be a list of tuples
        # each tuple should be (x,y), coordinates of the property
        self.properties = []
    
    # print top of screen bar for stuff like money
    def print_resources(self):
        resource_text = '$' + str(self.money)
        surface_string = constants.FONT.render(
            resource_text, True, constants.WHITE
        )
        location = constants.SCREEN_WIDTH - (len(resource_text) + 1) * 12

        constants.SCREEN.blit(surface_string, (location,5))

john = playable_character()