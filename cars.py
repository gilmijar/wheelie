"""
cars module generates car data.
database expects car make/model separately from inventory
and equipment separately from the other two
car prices are part of inventory, and seed data is in the data folder
"""

from random import Random
from pprint import pprint
from json import load as j_load
from functools import lru_cache
from operator import itemgetter


SEED = "AnotherTrulyRandomSeed"
rand = Random(SEED)

@lru_cache(maxsize=1)
def get_seed_data() -> list[dict]:
    """Return all seed data from nice_list.json. We cache this to avoid repeated file reads."""
    with open("data/nice_list.json", "r", encoding="utf-8") as seed_file:
        seed_cars = j_load(seed_file)
    return seed_cars


def get_seed_for_year(year: int) -> list[dict]:
    """Return seed data for a given year."""
    seed = get_seed_data()
    return [car for car in seed if car["purchase_year"] == year]


def columnize(what: list[dict]) -> dict[str, list]:
    """Convert a list of dicts into a dict of lists."""
    if not what:
        return {}
    columns = {k: [] for k in what[0].keys()}
    for item in what:
        for k, v in item.items():
            columns[k].append(v)
    return columns


def make_cars(count: int, yr: int) -> list[dict]:
    """
        Generate a collection of cars, internally consistent.
        Later we will split into make/model vs inventory vs equipment
    """
    if count <= 0:
        return []
    car_choices = get_seed_for_year(yr)
    car_base = columnize(rand.choices(car_choices, k=count))
    year, make, model, price = itemgetter(*'purchase_year make model price'.split())(car_base)
    fuel = rand.choices(
        population=["Gasoline", "Diesel", "Galosine", "Desle", "Gas"],
        weights=[45, 45, 5, 3, 2],
        k=count
    )
    price = [rand.randint(5000, 30000) for _ in range(count)]
    
    cars = []
    for row in zip(make, model, year, price, fuel):
        car = {k:v for k,v in zip(["make", "model", "year", "price", "fuel"], row)}
        cars.append(car)
    return cars


if __name__ == "__main__":
    sample_cars = make_cars(10)
    pprint(sample_cars)
