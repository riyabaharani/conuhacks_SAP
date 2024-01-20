import pandas as pd

request_date = "Request Date"
request_time = "Request Time"
appt_date = "Appointment Date"
appt_time = "Appointment Time"
vehicle_type = "Vehicle Type"
walk_in = "Walk-In"

header = [request_date, appt_date, vehicle_type]
df = pd.read_csv("sap_datafile.csv", names=header)

df[walk_in] = df[request_date] == df[appt_date]

df[request_date] = pd.to_datetime(df[request_date])
df[appt_date] = pd.to_datetime(df[appt_date])
df.sort_values(by=[appt_date, request_date], inplace=True)

df[request_date] = df[request_date].dt.strftime("%Y-%m-%d %X")
df[appt_date] = df[appt_date].dt.strftime("%Y-%m-%d %X")

df[[request_date, request_time]] = df[request_date].str.split(" ", n=1, expand=True)
df[[appt_date, appt_time]] = df[appt_date].str.split(" ", n=1, expand=True)

df = df[[appt_date, appt_time, request_date, request_time, vehicle_type, walk_in]]