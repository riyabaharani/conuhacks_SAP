import pandas as pd
import numpy as np

r = "Request Time"
a = "Appointment Time"

header = [r, a, "Vehicle Type"]
df = pd.read_csv("sap_datafile.csv", names=header)

df[r] = pd.to_datetime(df[r])
df[a] = pd.to_datetime(df[a])
df.sort_values(by=[a, r], inplace=True)

reserved, walk_in = [x for _, x in df.groupby(df[r] == df[a])]

reserved = reserved.to_numpy()
walk_in = walk_in.to_numpy()