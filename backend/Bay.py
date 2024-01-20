import pandas as pd
from data_parse import request_date, appt_date, vehicle_type, walk_in, df
from datetime import datetime, timedelta

class Bay:
    def __init__(self, id, end_ts):
        self.id = id
        self.end_ts = end_ts


time_taken_by_vehicle = {
    "compact": 0.5,
    "class 2 truck": 2,
    "class 1 truck": 1,
    "full-size": 0.5,
    "medium": 0.5
}

walk_in_map = {
    "compact": 0,
    "medium": 1,
    "full-size": 2,
    "class 1 truck": 3,
    "class 2 truck": 4
}

money_map = {
    "compact": 150,
    "class 2 truck": 700,
    "class 1 truck": 250,
    "full-size": 150,
    "medium": 150
}


def calc_next_available_ts(appoint_ts, vh_type):
    datetime_object = datetime.strptime(appoint_ts, format_string)
    t = timedelta(hours=time_taken_by_vehicle[vh_type])
    datetime_object = datetime_object + t
    return datetime_object


def walk_into_reserve(appoint_ts, index_df, vh_type):
    valid_bays = []
    for bay in available_reserve_bays:
        if appoint_ts >= bay.end_ts:
            valid_bays.append(bay)

    for i in range(index_df+1, len(df.index)):
        row = df.iloc[i]
        ts = row[appt_date]
        if not valid_bays:
            return None
        if ts > calc_next_available_ts(appoint_ts, time_taken_by_vehicle[vh_type]):
            return valid_bays[0]
        elif not row[walk_in]:
            valid_bays.pop()

    if valid_bays:
        return valid_bays[0]
    else:
        return None


def find_walk_in_bay(appoint_ts, vh_type, index_df):
    bay = available_walkin_bays[walk_in_map[vh_type]]
    if  appoint_ts >= bay.end_ts:
        return bay
    else:
        bay = walk_into_reserve(appoint_ts, index_df)
        return bay


def find_reserve_bay(appoint_ts):
    for bay in available_reserve_bays:
        if appoint_ts >= bay.end_ts:
            return bay


if __name__ == '__main__':
    available_reserve_bays = []
    available_walkin_bays = []
    for i in range(1, 11):
        if i < 6:
            available_reserve_bays.append(Bay(i, None))
        else:
            available_reserve_bays.append(Bay(i, None))

    result = {}
    turned_away = {}
    money_lost = 0
    money_made = 0
    cars_served = {}

    format_string = "%Y-%m-%d %H:%M:%S"

    for index, row in df.iterrows():
        curr_date_ts = row[appt_date]
        curr_date_ts = datetime.strptime(curr_date_ts, format_string)
        curr_date = curr_date_ts.Date
        vh_type = row[vehicle_type]
        if curr_date not in result:
            money_lost, money_made = 0, 0
            cars_served, turned_away = {}, {}
            result[curr_date] = {}
        if not row[walk_in]:
            bay = find_reserve_bay(curr_date_ts)
            bay.end_ts = calc_next_available_ts(curr_date_ts, vh_type)
            cars_served[vh_type] = cars_served.get(vh_type, 0) + 1
            money_made += money_map[vh_type]
        else:
            bay = find_walk_in_bay(curr_date_ts, index)
            if bay:
                bay.end_ts = calc_next_available_ts(curr_date_ts, vh_type)
            else:
                turned_away[vh_type] = turned_away.get(vh_type, 0) + 1
                money_lost += money_map[vh_type]