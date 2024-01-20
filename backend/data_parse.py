import pandas as pd

request_date = "Request Date"
appt_date = "Appointment Date"
vehicle_type = "Vehicle Type"
walk_in = "Walk-In"

header = [request_date, appt_date, vehicle_type]
df = pd.read_csv("sap_datafile.csv", names=header)

df[walk_in] = df[request_date] == df[appt_date]

df[request_date] = pd.to_datetime(df[request_date])
df[appt_date] = pd.to_datetime(df[appt_date])
df.sort_values(by=[appt_date, request_date], inplace=True)

df = df[[appt_date, request_date, vehicle_type, walk_in]]