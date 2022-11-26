import pygame
import constants, curser, characters

class cell():
    def __init__(self, cell_size, location_size):
        # cell is a square, cell_size is the number of available properties per 
        # row/col (type: int)
        self.cell_size = cell_size
        self.location_size = location_size

        self.text_coords = [
            location_size * cell_size + 10 * (cell_size + 1), 10
        ]

        self.locations = {}
        for row in range(self.cell_size):
            for col in range(self.cell_size):
                # examples keys: '0x0', '2x3', '3x1' 
                empty = empty_lot()
                empty.set_image(location_size, constants.BLACK)
                empty.set_coords((row,col))
                self.locations['{}x{}'.format(row,col)] = empty

    def print(self):
        for key in self.locations:
            location = self.locations[key]
            constants.SCREEN.blit(location.image, location.coords)
            constants.SCREEN.blit(location.name, location.coords)

    def hover(self):
        location = self.locations['{}x{}'.format(*curser.game_curser.location)]
        # should show info about current property ig
    
    def select(self, current_menu):
        location = self.locations['{}x{}'.format(*curser.game_curser.location)] 
        # if the first bit is set
        if current_menu.code & 0b10000000:
            # if empty lot
            if location.code == 0:
                characters.user.buy_property(self)
                
                curser.game_curser.select_mode(0b00, current_menu.parent_menu.length)
                return current_menu.parent_menu
            else:
                print('Location already occupied!')
        return current_menu
        
        
        # should do something idk
        # should set a variable that says which location is selected
        


class cell_location():
    def set_image(self, location_size, color):
        self.location_size = location_size
        self.image = pygame.Surface((self.location_size, self.location_size))
        self.image.fill(color)

    def set_coords(self, location):
        self.coords = [
            location[0]*(self.location_size + 10) + 10, 
            location[1]*(self.location_size + 10) + 10
        ]
    
    def render(self):
        self.name = constants.FONT.render(
            self.name, True, constants.WHITE
        )
    
    def select(self):
        if self.code == 0b00000000:
            pass
        

class empty_lot(cell_location):
    def __init__(self):
        self.code = 0b00000000
        self.name = "None"
        self.color = constants.BLACK
        self.render()

class store(cell_location):
    def __init__(self):
        self.code = 0b00000001
        self.name = "Store"
        self.color = constants.RED
        self.income = 1000
        self.expense = 900
        self.render()

class farm(cell_location):
    def __init__(self):
        self.code = 0b00000010
        self.name = "Farm"
        self.color = constants.GREEN
        self.income = 2000
        self.expense = 1800
        self.render()

class menu_location():
    def format_buy_menu_string(self):
        self.buy_menu_string = '{:20} {:>10} {:>10} {:>10}'.format(
            self.name, '$'+str(self.cost), '$'+str(self.income), 
            '$'+str(self.expense)
        )

class menu_store(menu_location):
    def __init__(self):
        self.buy_class = store
        self.name = 'Store'
        self.cost = 20000
        self.income = 1000
        self.expense = 900
        self.format_buy_menu_string()

class menu_farm(menu_location):
    def __init__(self):
        self.buy_class = farm
        self.name = 'Farm'
        self.cost = 30000
        self.income = 2000
        self.expense = 1800
        self.format_buy_menu_string()