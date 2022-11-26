import pygame
import constants


class cell():
    def __init__(self, cell_size):
        # cell is a square, cell_size is the number of available properties per 
        # row/col (type: int)
        self.cell_size = cell_size


        self.locations = []
        for row in range(self.cell_size):
            for col in range(self.cell_size):
                # examples keys: '0x0', '2x3', '3x1' 
                self.locations.append(empty_lot((row,col)))


    def change_property(self, location, property, owner):
        # location should be a tuple
        # property should either be None or an instance of a custom class
        self.locations['{}x{}'.format(*location)] = (location, property, owner)
        if property != None:
            # updates property class instance so it knows where it's at 
            property.location = location

    def print(self):
        for location in self.locations:
            constants.SCREEN.blit(location.image, location.coords)
            constants.SCREEN.blit(location.property_string, location.coords)
            constants.SCREEN.blit(location.owner_string, location.text_coords)

class cell_location():
    def __init__(self, location):
        self.image = pygame.Surface((150,150))
        self.coords = [location[0]*160+10, location[1]*160+10]
        self.text_coords = [self.coords[0], self.coords[1] + 25]
    
    def render(self):
        self.property_string = constants.FONT.render(
                self.property_type, True, constants.BLACK
        )
        self.owner_string = constants.FONT.render(
                self.owner.__class__.__name__, True, constants.BLACK
        )
        

class empty_lot(cell_location):
    def __init__(self, location):
        super().__init__(location)
        self.image.fill(constants.WHITE)
        self.property_type = "None"
        self.owner = None
        self.render()

class store(cell_location):
    def __init__(self, location):
        super().__init__(location)
        # then fill in the object
        self.image.fill(constants.RED)
        self.property_type = "Store"
        self.render()
        
    def calc_net(self):
        self.income = 1000
        self.expense = 900
        self.net = self.income - self.expense

property
