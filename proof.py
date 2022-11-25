import os
os.system('cls')
import time_passer, properties, characters, cell

john = characters.playable_character()
time = time_passer.time_passer()
game_cell = cell.cell(3)
store = properties.store()


game_cell.change_property((1,1),store)
store.calc_net()
game_cell.print_cell()