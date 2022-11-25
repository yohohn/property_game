import pygame,constants

class menu():
    def __init__(self):
        # options should be a list of tuples. ex: [(),(),(),()]
        # each tuple represents an option that can be selected
        # Where the first option is the text to be drawn to the screen
        # the second option is the next menu to go into if selected
        # (if the second option is None, the program stays on same menu)
        # the third option is a function to be called if selected
        # (if the third option is None, nothing will be called)
        #
        # ex: ('Buy a property.', buy_menu, None)
        # ('Quit game.', None, quit_game)
        self.options = []

    # print all options to screen
    def print(self, curser, current_ticks):
        # first check to see if the curser needs to be moved (and move it if so)
        curser.calc_curser(len(self.options), current_ticks)
        # then always print the curser to screen
        curser.print_curser()
        # line number is used to know where to print each option to screen
        line_number = 1
        for option in self.options:
            # for each option, first create the text object to be drawn
            surface_string = constants.FONT.render(
                option[0], True, constants.WHITE
            )
            # then calculate it's location
            location = constants.SCREEN_HEIGHT - line_number*25
            # then draw it to screen
            constants.SCREEN.blit(surface_string, (12,location))
            # finally, make sure the next line is drawn in the correct spot
            line_number += 1

    # what to do if a menu option is selected
    def select(self, curser):
        # if there is a function, then call it
        passed_function = self.options[curser.curser][2]
        if passed_function != None:
            passed_function(*self.options[curser.curser][3:])
    
        new_menu = self.options[curser.curser][1]
        # if there is a menu to go into, return the new menu
        if new_menu != None:
            curser.curser = 0
            return new_menu
        # else, return the current menu
        else:
            return self

class menu_curser():
    def __init__(self):
        # line number that curser is currently at (starts from bottom of screen)
        self.curser = 0

        # last time the curser was moved
        self.last_curser_update = 0

        # False is no movement, True is move according to self.curser_direction
        self.curser_movement = False

        # False is up, True is down
        self.curser_direction = False

        # create the object to draw
        self.underline = pygame.Surface((constants.SCREEN_WIDTH,25))
        # then fill in the object
        self.underline.fill(constants.GRAY)
    
    # check if the curser needs to be updated
    def calc_curser(self, menu_length, current_ticks):
        # if curser isn't moving, return
        if self.curser_movement == False:
            return
        # else if the last update was more than half a second ago
        elif current_ticks - self.last_curser_update > 100:
            self.last_curser_update = current_ticks
            # if curser is moving up
            if self.curser_direction == False:
                if self.curser > 0:
                    self.curser -= 1
            # else (if curser is moving down)
            else:
                if self.curser < menu_length - 1:
                    self.curser += 1

    # "highlight" the option the curser is on
    def print_curser(self):
        # first calc the location of where to "highlight"
        location = constants.SCREEN_HEIGHT - (self.curser + 1) * 25 - 3
        # then draw the object to the screen
        constants.SCREEN.blit(self.underline,(0,location))

