import pandas as pd
# Loading Excel data into a DataFrame
df = pd.read_csv('./FLIGHT_LOGS.csv')
departure_airports = df['departure_airport'].drop_duplicates()
arrival_airports = df['arrival_airport'].drop_duplicates()
# Combining and counting number of unique airports
all_airports = pd.concat([departure_airports, arrival_airports]).drop_duplicates()
num_airports = len(all_airports)
print("Number of airports:", num_airports)
# Finding total number of flights leaving each airport
total_departures = df['departure_airport'].value_counts()
print("Total number of flights leaving from each airport:", total_departures)
# Finding the busiest airport
busiest_airport = total_departures.idxmax()
print("The busiest airport is", busiest_airport)
# Finding number of distinct passengers
distinct_passengers = df['passenger_name'].nunique()
print("The number of distinct passengers are:", distinct_passengers)
# Finding the longest flight
longest_flight_duration = df['flight_duration'].max()
longest_flight = df[df['flight_duration'] == longest_flight_duration].iloc[0]
print("The longest flight is:", longest_flight_duration)
print("Departure Airport:", longest_flight['departure_airport'])
print("Arrival Airport:", longest_flight['arrival_airport'])
print("Departure Time:", longest_flight['departure_time'])
print("Arrival Time:", longest_flight['arrival_time'])