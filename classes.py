class Drink:
    def __init__(self, id, name, instructions=None):
        self._identifier = id
        self._name = name
        self._instructions = instructions

    def get_id(self):
        return self._identifier

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_instructions(self):
        return self._instructions

    def set_instructions(self, instructions):
        self._instructions = instructions

    identifier = property(get_id)
    name = property(get_name, set_name)
    instructions = property(get_instructions, set_instructions)

class Person:
    def __init__(self, id, forename, surname, fav_drink: Drink=None):
        self._identifier = id
        self._forename = forename
        self._surname = surname
        self._fav_drink = fav_drink

    def get_id(self):
        return self._identifier

    def get_forename(self):
        return self._forename

    def set_forename(self, name):
        self._forename = name

    def get_surname(self):
        return self._surname

    def set_surname(self, name):
        self._surname = name
   
    def get_fav_drink(self):
        if self._fav_drink is None:
            return Drink(-1, "No Preference")
        else:
            return self._fav_drink

    def set_fav_drink(self, drink: Drink):
        self._fav_drink = drink
    
    def get_fullname(self):
        return f"{self.forename} {self.surname}"
    
    identifier = property(get_id)
    forename = property(get_forename, set_forename)
    surname = property(get_surname, set_surname)
    full_name = property(get_fullname)
    fav_drink = property(get_fav_drink)

class Round:
    def __init__(self, round_time=""):
        _orders = {}
        while not round_time.isnumeric():
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

