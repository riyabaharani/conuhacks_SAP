import pandas as pd
import numpy as np

class Bay:
    def __init__(self, id, filled, status, next_avail_ts, used_as):
        self.id = id
        self.filled = filled
        self.status = status
        self.next_avail_ts = next_avail_ts
        self.used_as = used_as
    
    

if __name__ == '__main__':
    FILE_NAME = "./sap_datafile.csv"
    df = pd.read_csv(FILE_NAME, header=None)
    appoint_times = tuple(pd.to_datetime(df[1]))
    recall_times = tuple(pd.to_datetime(df[0]))
    car_types = tuple(df[2])
    mainData = [appoint_times, recall_times, car_types]
    print(mainData)