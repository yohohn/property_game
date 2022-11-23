class map():
    def __init__(self):
        pass

    def print_map(self):
        pass

class cell():
    def __init__(self, cell_size):
        # cell is a square, cell_size is the number of available properties per 
        # row/col (type: int)

        # creates the available grid of locations
        self.make_cell(cell_size)

    def make_cell(self,size):
        # size is an int

        self.locations = {}
        for row in range(size):
            for col in range(size):
                # examples keys: '0x0', '2x3', '3x1' 
                self.locations['{}x{}'.format(row,col)] = None


    def get_property(self, location):
        # location should be a tuple
        return self.locations['{}x{}'.format(*location)]

    def change_property(self, location, property):
        # location should be a tuple
        # property should either be None or an instance of a custom class
        self.locations['{}x{}'.format(*location)] = property
        if property != None:
            # updates property class so it knows where it's at 
            property.location = location

    def print_cell(self):
        for key in self.locations:
            print(self.locations[key].__class__.__name__)
        
