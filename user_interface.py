import pygame,constants

class menu():
    def __init__(self):
        self.options = {}
        self.init_curser()


    def init_curser(self):
        # line number that curser is currently at
        self.curser = 1

        # last time the curser was moved
        self.last_curser_update = 0

        # False is no movement, True is move according to self.curser_direction
        self.curser_movement = False

        # False is up, True is down
        self.curser_direction = False


    def calc_curser(self, current_ticks):
        self.print_curser()
        # if curser isn't moving, return
        if self.curser_movement == False:
            return
        # else if the last update was more than half a second ago
        elif current_ticks - self.last_curser_update > 100:
            self.last_curser_update = current_ticks
            # if curser is moving up
            if self.curser_direction == False:
                if self.curser > 1:
                    self.curser -= 1
            # else (if curser is moving down)
            else:
                if self.curser < len(self.options):
                    self.curser += 1
        

    def print_curser(self):
        location = constants.SCREEN_HEIGHT - self.curser*25 - 3
        underline = pygame.Surface((constants.SCREEN_WIDTH,25))
        underline.fill(constants.GRAY)
        constants.SCREEN.blit(underline,(0,location))


    def print(self, current_ticks):
        self.calc_curser(current_ticks)
        line_number = 1
        for text in self.options:
            if self.curser == line_number:
                self.curser_selected = text
            surface_string = constants.FONT.render(text,True,constants.WHITE)
            location = constants.SCREEN_HEIGHT - line_number*25
            constants.SCREEN.blit(surface_string, (10,location))
            line_number += 1