import pygame
import constants
class building():
    def __init__(self):
        self.location = None
        # every building needs a location
        # could just do a two element list (or a tuple)

        # every building type needs a price, operating costs
        # can be affected by location
        pass

class store(building):
    def __init__(self):
        super().__init__()

        # first creat the object
        self.image = pygame.Surface((150,150))
        # then fill in the object
        self.image.fill(constants.RED)
        


    def calc_net(self):
        self.income = 1000
        self.expense = 900
        self.net = self.income - self.expense