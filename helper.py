from json import load
from typing import List, Generator
from functools import lru_cache


def filter_list_of_dicts(items:List[dict], **kwargs) -> Generator[dict, None, None]:
    filters = kwargs.items()
    _items = items[:]
    for k,v in filters:
        _items = filter(lambda itm: k in itm and itm[k] == v, _items)
    return _items


@lru_cache(maxsize=1)
def get_json_table(file_name:str) -> List[dict]:
    return load(open(file_name, "r", encoding="utf-8"))


def get_cars(data_file_name:str, year=None, make=None, model=None) -> List[dict]:
    filters = {k:v for k,v in zip(("year", "make", "model"), (year, make, model)) if v is not None}
    tbl = get_json_table(data_file_name)
    return list(filter_list_of_dicts(tbl, **filters))


if __name__ == "__main__":
    print(get_cars("data/nice_list.json", year=2020, make="Toyota"))
