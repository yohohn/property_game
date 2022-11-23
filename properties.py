


class building():
    def __init__(self):


        # every building needs a location
        # could just do a two element list (or a tuple)

        # every building type needs a price, operating costs
        # can be affected by location
        pass

class store(building):
    def __init__(self):
        super().__init__()

    def calc_net(self):
        self.income = 1000
        self.expense = 900
        self.net = self.income - self.expense