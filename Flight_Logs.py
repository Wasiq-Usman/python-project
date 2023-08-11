import csv
from datetime import datetime, timedelta


def readfile(file_path):
    data = []
    try:
        with open(file_path, 'r', newline='') as csvfile:
            data_file = csv.DictReader(csvfile)
            for row in data_file:
                data.append(row)
    except FileNotFoundError:
        print("File not found")
    return data


def count_unique_airports(data, departure_column, arrival_column):
    unique_airports = set()

    for row in data:
        if row[departure_column]:
            unique_airports.add(row[departure_column])
        if row[arrival_column]:
            unique_airports.add(row[arrival_column])

    return len(unique_airports)


def count_departures(data, departure_column):
    departure_count = {}

    for row in data:
        if row[departure_column]:
            airport = row[departure_column]
            if airport in departure_count:
                departure_count[airport] += 1
            else:
                departure_count[airport] = 1

    return departure_count


def count_arrivals_and_departures(data, departure_column, arrival_column):
    airport_count = {}

    for row in data:
        if row[departure_column]:
            departure_airport = row[departure_column]
            if departure_airport in airport_count:
                airport_count[departure_airport]['departures'] += 1
            else:
                airport_count[departure_airport] = {'departures': 1, 'arrivals': 0}
        if row[arrival_column]:
            arrival_airport = row[arrival_column]
            if arrival_airport in airport_count:
                airport_count[arrival_airport]['arrivals'] += 1
            else:
                airport_count[arrival_airport] = {'departures': 0, 'arrivals': 1}

    return airport_count


def busiest_airport(data, departure_column, arrival_column):
    airport_count = count_arrivals_and_departures(data, departure_column, arrival_column)

    busiest_airport_name = max(airport_count,
                               key=lambda airport: airport_count[airport]['departures'] + airport_count[airport][
                                   'arrivals'])
    busiest_count = airport_count[busiest_airport_name]['departures'] + airport_count[busiest_airport_name]['arrivals']

    return busiest_airport_name, busiest_count

    def count_distinct_passengers(data):
        passengers = set()
    for row in data:
        if row['passenger_id']:
            passengers.add(row['passenger_id'])

    return len(passengers)


def find_longest_flight(data):
    longest_flight = None
    max_duration = timedelta(seconds=0)

    for row in data:
        departure_time = datetime.strptime(row['departure_time'], '%I:%M %p')
        arrival_time = datetime.strptime(row['arrival_time'], '%I:%M %p')

        duration = arrival_time - departure_time
        if duration > max_duration:
            max_duration = duration
            longest_flight = {
                'airport_name': row['departure_airport'],
                'departure_time': departure_time,
                'arrival_time': arrival_time
            }
    return longest_flight


def count_distinct_passengers(data):
    passengers = set()

    for row in data:
        if row['passenger_name']:
            passengers.add(row['passenger_name'])

    return len(passengers)
def main():
    file_path = './FLIGHT_LOGS.csv'
    departure_column = 'departure_airport'
    arrival_column = 'arrival_airport'

    try:
        data = readfile(file_path)

        unique_airport_count = count_unique_airports(data, departure_column, arrival_column)
        departure_count = count_departures(data, departure_column)
        busiest_airport_name, busiest_count = busiest_airport(data,departure_column, arrival_column)
        distinct_passenger_count = count_distinct_passengers(data)
        longest_flight = find_longest_flight(data)
        print(f"Total number of unique airports: {unique_airport_count}")
        print("Number of flights leaving each airport:")
        for airport, count in departure_count.items():
            print(f"{airport}: {count}")

        print(
            f"All-time most busy airport was {busiest_airport_name} with {busiest_count} total arrivals and departures")
        print(f"Total number of distinct passengers: {distinct_passenger_count}")

        print("Longest flight details:")
        if longest_flight:
            print(f"Airport Name: {longest_flight['airport_name']}")
            print(f"Departure Time: {longest_flight['departure_time']}")
            print(f"Arrival Time: {longest_flight['arrival_time']}")
        else:
            print("No flights data available")
    except Exception as e:
        raise RuntimeError("An error occurred: " + str(e))


if __name__ == "__main__":
    main()
