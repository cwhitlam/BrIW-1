import unittest
from UI import UI
from IO import Pickle_IO
from classes import *

class Unit_Testing_Class(unittest.TestCase):
    def test_person_fav_drink(self):
        try:
            id = 50
            name = "Jeffery"
            surname = "Archer"
            fav_drink = None

            person = Person(id, name, surname, fav_drink)
            self.assertEqual(person.fav_drink.identifier, -1)
            self.assertEqual(person.fav_drink.name, "No Preference")
            self.assertIs(person.fav_drink.instructions, None)
            print("Round Order Test: Successful")
        except Exception as e:
            print("Round Order Test: Failed")
            print(f"Error: {e}")

    def test_round_orders(self):
        try:
            testing_round = Round(10)
            person = Person(99, "FirstName", "LastName", None)
            drink = Drink(99, "Coffee")
            expected_orders = {person: drink}

            testing_round.add_order(person, drink)
            actual_orders = testing_round.get_orders()
            
            self.assertEqual(expected_orders, actual_orders)
            print("Round Order Test: Successful")
        except Exception as e:
            print("Round Order Test: Failed")
            print(f"Error: {e}")

    def test_round_status(self):
        try:
            testing_round = Round(10)
            #round just opened so isActive should return True
            self.assertTrue(testing_round.isActive())
            
            testing_round.end()
            #round has now been ended so isActive should return False
            self.assertFalse(testing_round.isActive())
            
            print("Round Status: Successful")
        except Exception as e:
            print("Round Status Test: Failed")
            print(f"Error: {e}")

    def test_pickle_io(self):
        try:
            io = Pickle_IO()
            #loads people data and repickles it in new test file
            dummy_file_name = "unittest"
            dummy_file_obj = io.unpickle("people")
            io.picklize(dummy_file_name, dummy_file_obj)

            #compare people file to newly pickled file and ensure serialization is working correctly
            new_pickle = io.unpickle(dummy_file_name)

            expected_output = {}
            for identifier, person in dummy_file_obj.items():
                expected_output[identifier] = person.build_json()
            
            
            actual_output = {}
            for identifier, person in new_pickle.items():
                actual_output[identifier] = person.build_json()

            self.maxDiff = None
            self.assertDictEqual(expected_output, actual_output)

            
            print("Pickle IO Test: Successfull")
        except Exception as e:
            print("Pickle IO Test: Failed")
            print(f"Error: {e}")



utc = Unit_Testing_Class()
#tests
utc.test_person_fav_drink()
utc.test_round_orders()
utc.test_round_status()
utc.test_pickle_io()
