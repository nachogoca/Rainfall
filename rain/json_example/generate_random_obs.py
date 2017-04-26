import datetime
import json
from random import uniform

INTERVAL = datetime.timedelta(minutes = 5)
START_DATE = datetime.date(day=1, month=1, year=2014)
END_DATE = datetime.date(day=31, month=12, year=2015)


class Precipitation():
    measure_datetime = None
    rainfall_rate = None

    def __init__(self, measure_datetime, rainfall_rate):
        self.measure_datetime = measure_datetime
        self.rainfall_rate = rainfall_rate


def main():
    observations = generate_random_observations()
    with open('data.json', 'w') as openfile:
        json.dump(observations.__dict__, openfile, default=json_serial)


def generate_random_observations():
    observations = []

    d = START_DATE
    while d < END_DATE:

        rand = uniform(0, 15)
        precipitation = Precipitation(d, rand)
        observations.append(precipitation)

        d += INTERVAL

    return observations

def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, datetime.datetime):
        serial = obj.isoformat()
        return serial
    raise TypeError ("Type not serializable")

main()
