import constants

class menu():
    def __init__(self):
        self.options = []

    # add new option to options
    def append(self, text, next_space, function, *args):
        option = menu_option(text,next_space, function, *args)
        self.options.append(option)
        option.set_location(len(self.options))

    # print all options to screen
    def print(self):
        for option in self.options:
            constants.SCREEN.blit(option.surface_text, (12,option.location))

    def select(self, curser):
        option = self.options[curser.location]
        option.call_function()
        if option.next_space != None:
            curser.select_mode(0b00, len(option.next_space.options) - 1)
            return option.next_space
        else:
            return self
        

class menu_option():
    def __init__(self, text, next_space, function, *args):
        self.next_space = next_space
        self.function = function
        self.args = args

        self.surface_text = constants.FONT.render(
            text, True, constants.WHITE
        )
    
    def call_function(self):
        if self.function != None:
            self.function(*self.args)
    
    def set_location(self, line_number):
        self.location = constants.SCREEN_HEIGHT - line_number*25
