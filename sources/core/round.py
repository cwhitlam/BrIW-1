class Round:
    def __init__(self, round_time=""):
        self._orders = {}
        
        while isinstance(round_time, str) and not round_time.isnumeric():
            round_time = input("How many minutes would you like to allow submitions for? (whole numbers): ")
        self.round_time = round_time
        print(f"round started. TIME: {round_time} minute(s)") 

    def end(self):
        #ends round early
        self.round_time = 0

    def add_order(self, person: Person, drink: Drink):
        self._orders[person] = drink

    def update_order(self, person, drink):
        self._orders[person] = drink

    def isActive(self):
        return self.round_time > 0

    def get_orders(self):
        return self._orders

    def set_orders(self, orders):
        self._orders = orders

    orders = property(get_orders, set_orders)
