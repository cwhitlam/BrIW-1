import json

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

    def build_json(self):
        json_out = {
            "identifier": self.identifier,
            "name": self.name,
            "instructions": self.instructions
        }

        return json_out


    identifier = property(get_id)
    name = property(get_name, set_name)
    instructions = property(get_instructions, set_instructions)

