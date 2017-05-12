import datetime
import json
from random import uniform

INTERVAL = datetime.timedelta(minutes = 30)
START_DATE = datetime.datetime(day=1, month=1, year=2014)
END_DATE = datetime.datetime(day=2, month=1, year=2014)


def main():
    observations = generate_random_observations()

    with open('data.json', 'w') as openfile:
        json.dump(observations, openfile, indent=4,sort_keys=True)


def generate_random_observations():
    observations = []

    d = START_DATE
    while d < END_DATE:

        rand = uniform(0, 15)
        precip = {}
        precip['measure_datetime'] = d.isoformat()
        precip['rainfall_rate'] = rand
        observations.append(precip)

        d += INTERVAL

    return observations


main()
