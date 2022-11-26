import pygame
import constants
class curser():
    def __init__(self):
        # last time the curser was moved
        self.last_move = 0
        # how long to wait before being able to be moved
        self.move_wait = 150

        # create the object to draw
        self.underline = pygame.Surface((constants.SCREEN_WIDTH,25))
        # then fill in the object
        self.underline.fill(constants.GRAY)

        self.map_highlight = pygame.Surface((150,25))
        self.map_highlight.fill(constants.ORANGE)
        self.map_highlight.set_alpha(128)

    def select_mode(self, mode, max_location):
        self.mode = mode
        self.max_location = max_location - 1
        self.movement = 0b0000
        # menu mode
        if   mode == 0b00:
            self.location = 0
            self.print_location = [0, constants.SCREEN_HEIGHT - 28]
            self.highlight = self.underline
        # map mode
        elif mode == 0b01:
            self.location = [0,0]
            self.print_location = [10,135]
            self.highlight = self.map_highlight
    
    def move(self, current_ticks):
        if current_ticks > (self.last_move + self.move_wait):
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                self.movement |= 0b1000
            if keys[pygame.K_DOWN]:
                self.movement |= 0b0100
            if keys[pygame.K_LEFT]:
                self.movement |= 0b0010
            if keys[pygame.K_RIGHT]:
                self.movement |= 0b0001
        else:
            self.movement = 0b0000

        if self.movement:
            self.last_move = current_ticks

        # menu mode
        if self.mode == 0b00:
            # up
            if self.movement & 0b1000:
                if self.location < self.max_location:
                    self.location += 1
                    self.print_location[1] -= 25
            # down
            if self.movement & 0b0100:
                if self.location > 0:
                    self.location -= 1
                    self.print_location[1] += 25
        
        # map mode
        if self.mode == 0b01:
            # up
            if self.movement & 0b1000:
                if self.location[1] > 0:
                    self.location[1] -= 1
                    self.print_location[1] -= 160
            # down
            if self.movement & 0b0100:
                if self.location[1] < self.max_location:
                    self.location[1] += 1
                    self.print_location[1] += 160
            # left
            if self.movement & 0b0010:
                if self.location[0] > 0:
                    self.location[0] -= 1
                    self.print_location[0] -= 160
            # right
            if self.movement & 0b0001:
                if self.location[0] < self.max_location:
                    self.location[0] += 1
                    self.print_location[0] += 160

    def tab(self, current_menu, current_cell):
        if self.mode != 0b01:
            self.select_mode(0b01, current_cell.cell_size)
        else:
            self.select_mode(0b00, current_menu.length)
        

    def print_curser(self):
        constants.SCREEN.blit(self.highlight, self.print_location)
