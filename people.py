# use mimesis to generate a few people records
from mimesis import Locale, Field, Schema, Generic, Gender
from mimesis.random import Random as mimesis_random
from pprint import pprint
from datetime import date, timedelta



def record():
    return {
        "name": adjustable.person.full_name(gender=adjustable.random.weighted_choice({Gender.FEMALE: 0.6, Gender.MALE: 0.4})),
        "email": field("person.email"),
        "address": field("address.address"),
        "city": field("address.city"),
        "postal_code": field("address.postal_code"),
        "country": field("address.default_country"),
        "realistic_birth_date": field('realistic_birth_date').isoformat(),
    }


SEED = "TrulyRandomSeed"

field = Field(locale=Locale.PL, seed=SEED)
adjustable = Generic(locale=Locale.PL, seed=SEED)

@field.handle('realistic_birth_date')
def rebirth(rnd: mimesis_random, **kwargs) -> date:
    """Redistribute birth years to create a more realistic age distribution."""
    MIN_BOUND = 1970
    MAX_BOUND = 2007
    mean_year = (MAX_BOUND + MIN_BOUND) // 2
    STDDEV = 6
    adjusted_year = int(rnd.gauss(mean_year, STDDEV))
    yr = max(MIN_BOUND, min(adjusted_year, MAX_BOUND))
    base_date = date(year=yr, month=1, day=1)
    try:
        target_date = base_date + timedelta(days = rnd.randint(0, 365))
    except ValueError:
        target_date = base_date + timedelta(days = rnd.randint(0, 364))
    return target_date


schema = Schema(schema=record, iterations=50000)

pprint(schema.to_csv('outputs/people.csv'))
