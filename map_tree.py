import cell

# import constants
# num_locations = 3
# the screen height, minus gaps of 10 between each location
# then divided by the number of locations
# int rounds down to nearest integer
# location_size = int(
#     ( constants.SCREEN_HEIGHT - ( (num_locations + 1) * 10 ) )/num_locations
# )
start_cell = cell.cell(3,150)



BUYABLE_BUILDINGS = {
    cell.menu_farm(),
    cell.menu_store()
    }