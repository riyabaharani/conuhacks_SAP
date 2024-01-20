import pandas as pd
from data_parse import df, reserved, walk_in
from enum import Enum

class Bay:
    def __init__(self, id, available, next_avail_ts, used_as):
        self.id = id
        self.available = available
        self.next_avail_ts = next_avail_ts
        self.used_as = used_as


time_taken_by_vehicle = {
    "compact":0.5,
    "class 2 truck": 2,
    "class 1 truck": 1,
    "full-size":0.5,
    "medium":0.5
}

def calc_next_available_ts(appoint_ts, vehicle_type):
    time_taken = time_taken_by_vehicle[vehicle_type]


def find_walk_in_bay():
    pass

def find_reserve_bay():
    for bay in available_bays:
        if bay.used_as == 'reserve' and bay.available:
            return bay



if __name__ == '__main__':
    r = "Request Time"
    a = "Appointment Time"

    available_bays = []
    for i in range(1, 11):
        if i < 6:
            available_bays.append(Bay(i, False, None, 'reserve'))
        else:
            available_bays.append(Bay(i, False, None, 'walk_in'))

    result = {}

    for index, row in df.iterrows():
        curr_date = row[a].date()
        if curr_date not in result:
            result[curr_date] = {}
        if row[a] != row[r]:
            bay = find_reserve_bay()
            bay.available = False
            # bay.next_avail_ts =
        else:
            bay = find_reserve_bay()