import unittest
from module1 import city_country

class CityCountryTestCase(unittest.TestCase):
    """adds"""

    def test_city_country(self):
        """adsd"""
        shiti_kantri = city_country('santiago', 'chile', '500')
        self.assertEqual(shiti_kantri, 'Santiago, Chile -Population 500')

if __name__ == '__main__':
    unittest.main()