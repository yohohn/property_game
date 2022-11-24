import properties



class playable_character():
    def __init__(self):
        self.money = 0
        # thinking properties should be a list of tuples
        # each tuple should be (x,y), coordinates of the property
        self.properties = []

john = playable_character()