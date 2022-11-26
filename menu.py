import constants, curser

class menu():
    def __init__(self, code, parent_menu):
        self.code = code
        self.parent_menu = parent_menu
        self.options = []
        self.texts = []
        self.length = 0
        self.text_length = 0

    # add new option to options
    def append(self, text, next_space, function, *args):
        option = menu_option(text,next_space, function, *args)
        self.options.append(option)
        self.length += 1
        option.set_location(self.length)
    
    # add non-selectable option to be printed
    def append_text(self, text):
        text_option = menu_option(text, None, None)
        self.texts.append(text_option)
        self.text_length += 1
        text_option.set_location(self.length + self.text_length)

    # print all options to screen
    def print(self):
        for option in self.options:
            constants.SCREEN.blit(option.surface_text, (12, option.location))
        for text in self.texts:
            constants.SCREEN.blit(text.surface_text, (12, text.location))

    def select(self):
        option = self.options[curser.game_curser.location]
        option.call_function()
        if option.next_space != None:
            curser.game_curser.select_mode(0b00, option.next_space.length)
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
