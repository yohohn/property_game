import pygame
import constants

class cell():
    def __init__(self, cell_size):
        # cell is a square, cell_size is the number of available properties per 
        # row/col (type: int)

        # creates the available grid of locations
        self.make_cell(cell_size)
        # create the default to print if no property
        self.image = pygame.Surface((150,150))
        # then fill in the object
        self.image.fill(constants.WHITE)

    def make_cell(self,size):
        # size is an int

        self.locations = {}
        for row in range(size):
            for col in range(size):
                # examples keys: '0x0', '2x3', '3x1' 
                self.locations['{}x{}'.format(row,col)] = \
                    ((row, col), None, None)


    def get_property(self, location):
        # location should be a tuple
        return self.locations['{}x{}'.format(*location)]

    def change_property(self, location, property, owner):
        # location should be a tuple
        # property should either be None or an instance of a custom class
        self.locations['{}x{}'.format(*location)] = (location, property, owner)
        if property != None:
            # updates property class instance so it knows where it's at 
            property.location = location

    def print_cell(self):
        # need to first find (or define) printable area
        # then print
        # thinking of for now, using different colors to represent different 
        # properties
        for location in self.locations:
            coords = self.locations[location][0]
            coords = (coords[0]*160+10,coords[1]*160+10)
            property = self.locations[location][1]
            owner = self.locations[location][2]
            if property != None:
                constants.SCREEN.blit(property.image,coords)
            else:
                constants.SCREEN.blit(self.image,coords)

            property_string = constants.FONT.render(
                property.__class__.__name__, True, constants.BLACK
            )
            owner_string = constants.FONT.render(
                owner.__class__.__name__, True, constants.BLACK
            )
            owner_coords = (coords[0], coords[1] + 25)
            # then draw it to screen
            constants.SCREEN.blit(property_string, coords)
            constants.SCREEN.blit(owner_string, owner_coords)

class cell_curser():
    def __init__(self, cell_size):
        self.max_coord = cell_size - 1
        self.coords = [0,0]
        self.last_curser_update = 0 
        self.selected = pygame.Surface((150,25))
        self.selected.fill(constants.ORANGE)
        self.selected.set_alpha(128)   

    # check if the curser needs to be updated
    def calc_curser(self, movement, current_ticks):
        # only true if last four bits of movement are zero
        if ~movement & 0b00001111 == 0b00001111:
            return
        # check if enough time has passed
        elif current_ticks - self.last_curser_update > 100:
            self.last_curser_update = current_ticks
            # right
            if movement & 0b00000001:
                if self.coords[0] < self.max_coord:
                    self.coords[0] += 1
            # left
            if movement & 0b00000010:
                if self.coords[0] > 0:
                    self.coords[0] -= 1
            # down
            if movement & 0b00000100:
                if self.coords[1] < self.max_coord:
                    self.coords[1] += 1
            # up
            if movement & 0b00001000:
                if self.coords[1] > 0:
                    self.coords[1] -= 1

            
        

    def print_curser(self):
        coords = (self.coords[0]*160+10, self.coords[1]*160+135)
        constants.SCREEN.blit(self.selected,coords)
