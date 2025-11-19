from unittest import TestCase
import cars

class TestCarsModule(TestCase):
    def test_make_cars_produces_expected_items(self):
        new_cars = cars.make_cars(5, 2023)
        self.assertEqual(5, len(new_cars))

    def test_make_cars_produces_no_items_when_count_is_zero(self):
        new_cars = cars.make_cars(0, 2023)
        self.assertEqual(0, len(new_cars))

    def test_make_cars_produces_items_with_expected_keys(self):
        new_cars = cars.make_cars(1, 2023)
        for car in new_cars:
            self.assertIn("make", car)
            self.assertIn("model", car)
            self.assertIn("year", car)
            self.assertIn("price", car)

    def test_make_card_prodces_expected_fuel_types(self):
        new_cars = cars.make_cars(100, 2023)
        valid_fuels = {"Gasoline", "Diesel", "Galosine", "Desle", "Gas"}
        fuels = {car["fuel"] for car in new_cars}
        self.assertSetEqual(valid_fuels, fuels, msg = f"\n\texpecting only {valid_fuels = },\n\tgot {fuels = }")


class TestGetSeedForYear(TestCase):
    def test_get_seed_data_returns_list(self):
        seed_data = cars.get_seed_data()
        self.assertIsInstance(seed_data, list)

    def test_get_seed_for_year_returns_correct_year(self):
        seed_data = cars.get_seed_for_year(2023)
        years = set(car["purchase_year"] for car in seed_data)
        self.assertSetEqual({2023}, years)

    def test_get_seed_for_year_returns_empty_list_for_nonexistent_year(self):
        seed_data = cars.get_seed_for_year(1990)
        self.assertListEqual([], seed_data)


class TestCarInfoExtractor(TestCase):
    def test_columnize_happy_path(self):
        sample_cars = [{
            "purchase_year": 2020,
            "make": "Toyota",
            "model": "Camry",
            "price": 20000
        }, 
        {
            "purchase_year": 2021,
            "make": "Honda",
            "model": "Civic",
            "price": 22000
        }]
        expected = {
            "purchase_year": [2020, 2021],
            "make": ["Toyota", "Honda"],
            "model": ["Camry", "Civic"],
            "price": [20000, 22000]
        }
        actual = cars.columnize(sample_cars)
        self.assertDictEqual(expected, actual)


if __name__ == "__main__":
    import unittest
    unittest.main()