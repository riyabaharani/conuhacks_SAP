from data_parse import appt_date, vehicle_type, walk_in, df
from datetime import timedelta
import json


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
    t = timedelta(hours=time_taken_by_vehicle[vh_type])
    appoint_ts = appoint_ts + t
    return appoint_ts


def walk_into_reserve(appoint_ts, index_df, vh_type):
    valid_bays = []
    for bay in available_reserve_bays:
        if not bay.end_ts or appoint_ts >= bay.end_ts:
            valid_bays.append(bay)

    for i in range(index_df + 1, len(df.index)):
        row = df.iloc[i]
        ts = row[appt_date]
        if not valid_bays:
            return None
        if ts > calc_next_available_ts(appoint_ts, vh_type):
            return valid_bays[0]
        elif not row[walk_in]:
            valid_bays.pop()

    if valid_bays:
        return valid_bays[0]
    else:
        return None


def find_walk_in_bay(appoint_ts, vh_type, index_df):
    bay = available_walkin_bays[walk_in_map[vh_type]]
    if not bay.end_ts or appoint_ts >= bay.end_ts:
        return bay
    else:
        bay = walk_into_reserve(appoint_ts, index_df, vh_type)
        return bay


def find_reserve_bay(appoint_ts):
    for bay in available_reserve_bays:
        if not bay.end_ts or appoint_ts >= bay.end_ts:
            return bay


available_reserve_bays = []
available_walkin_bays = []
for i in range(1, 11):
    if i < 6:
        available_reserve_bays.append(Bay(i, None))
    else:
        available_walkin_bays.append(Bay(i, None))

result = {}
turned_away = {}
money_lost = 0
money_made = 0
cars_served = {}
total_revenue = 0
total_loss = 0
prev_date = df.iloc[0][0].date()

for i in range(len(df.index)):
    row = df.iloc[i]
    curr_date_ts = row[appt_date]
    curr_date = curr_date_ts.date()
    vh_type = row[vehicle_type]
    bay = None
    if prev_date != curr_date:
        result[prev_date.strftime("%Y-%m-%d")] = {"money_lost": money_lost, "money_made": money_made,
                                                        "cars_served": cars_served, "turned_away": turned_away}
        money_lost, money_made = 0, 0
        cars_served, turned_away = {}, {}
        prev_date = curr_date
    if not row[walk_in]:
        # print("Reservation")
        bay = find_reserve_bay(curr_date_ts)
    else:
        bay = find_walk_in_bay(curr_date_ts, vh_type, i)
    if bay:
        bay.end_ts = calc_next_available_ts(curr_date_ts, vh_type)
        cars_served[vh_type] = cars_served.get(vh_type, 0) + 1
        money_made += money_map[vh_type]
        total_revenue += money_map[vh_type]
    else:
        turned_away[vh_type] = turned_away.get(vh_type, 0) + 1
        money_lost += money_map[vh_type]
        total_loss += money_map[vh_type]
result[curr_date.strftime("%Y-%m-%d")] = {"money_lost": money_lost, "money_made": money_made,
                                                "cars_served": cars_served, "turned_away": turned_away}
result["revenue"] = total_revenue
result["loss"] = total_loss

if __name__ == "__main__":
    with open("users.json", "w") as outfile:
        json.dump(result, outfile, indent=4)
