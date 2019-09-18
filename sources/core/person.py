import json

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

    def build_json(self):
        json_out = {
            "identifier": self.identifier, 
            "forename": self.forename,
            "surname": self.surname,
            "fav_drink": self.fav_drink.build_json()
        }
        
        return json_out        

    identifier = property(get_id)
    forename = property(get_forename, set_forename)
    surname = property(get_surname, set_surname)
    full_name = property(get_fullname)
    fav_drink = property(get_fav_drink)

