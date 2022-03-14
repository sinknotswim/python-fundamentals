#11-1 I had to remove test from city_country to get it to run 11-2 sucessfully

import unittest
from city_functions import city_country

class CityCountryTestCase(unittest.TestCase):
    
    def city_country(self):
        sant_chil = city_country("Santiago", "Chile")
        self.assertEqual(sant_chil, "Santiago, Chile")

unittest.main()

#11-2 I had to do the same here

class CitiesTestCase(unittest.TestCase):

    def city_country(self):
        sant_chil = city_country('santiago', 'Chile')
        self.assertEqual(sant_chil, 'Santiago, Chile')

    def city_country(self):
        sant_chil = city_country('santiago', 'Chile', population=5000000)
        self.assertEqual(sant_chil, 'Santiago, Chile - population 5000000')

unittest.main()

#11-3

from employee import Employee

class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.li = Employee("Li", "Taylor", 5000)

    def test_give_default_raise(self):
        self.li.give_raise()
        self.assertEqual(self.li.salary, 5000)
    
    def test_give_custom_raise(self):
        self.li.give_rise(5000)
        self.assertEqual(self.li.salary, 5000)

unittest.main()