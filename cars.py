"""
cars module generates car data.
database expects car make/model separately from inventory
and equipment separately from the other two
car prices are part of inventory, and seed data is in the data folder
"""

from random import Random
from pprint import pprint
from json import load as j_load

SEED = "AnotherTrulyRandomSeed"
rand = Random(SEED)


def get_seed_for_year(year: int) -> list[dict]:
    """Return seed data for a given year."""
    with open("data/nice_list.json", "r", encoding="utf-8") as seed_file:
        seed_cars = j_load(seed_file)
        return [car for car in seed_cars if car["purchase_year"] == year]


def make_cars(count: int) -> list[dict]:
    """
        Generate a collection of cars, internally consistent.
        Later we will split into make/model vs inventory vs equipment
    """
    make = rand.choices(
        population=["Toyota", "Ford", "Chevrolet", "Honda", "Nissan"],
        weights=[30, 25, 20, 15, 10],
        k=count
    )
    model = rand.choices(
        population=["Model A", "Model B", "Model C", "Model D", "Model E"],
        weights=[20, 25, 30, 15, 10],
        k=count
    )
    year = rand.choices(
        population=tuple(range(2000, 2023)),
        k=count
    )
    price = [rand.randint(5000, 30000) for _ in range(count)]
    cars = []
    for row in zip(make, model, year, price):
        car = {k:v for k,v in zip(["make", "model", "year", "price"], row)}
        cars.append(car)
    return cars

if __name__ == "__main__":
    sample_cars = make_cars(10)
    pprint(sample_cars)
