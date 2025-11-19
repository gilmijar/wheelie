from unittest import TestCase
import cars

class TestCarsModule(TestCase):
    def test_make_cars_produces_expected_items(self):
        new_cars = cars.make_cars(5)
        self.assertEqual(5, len(new_cars))

    def test_make_cars_produces_no_items_when_count_is_zero(self):
        new_cars = cars.make_cars(0)
        self.assertEqual(0, len(new_cars))

    def test_make_cars_produces_items_with_expected_keys(self):
        new_cars = cars.make_cars(1)
        for car in new_cars:
            self.assertIn("make", car)
            self.assertIn("model", car)
            self.assertIn("year", car)
            self.assertIn("price", car)

    def test_get_seed_for_year_returns_correct_year(self):
        seed_data = cars.get_seed_for_year(2023)
        years = set(car["purchase_year"] for car in seed_data)
        self.assertSetEqual({2023}, years)

    def test_get_seed_for_year_returns_empty_list_for_nonexistent_year(self):
        seed_data = cars.get_seed_for_year(1990)
        self.assertListEqual([], seed_data)