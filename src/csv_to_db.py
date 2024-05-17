import csv
import sqlite3
from database import create_connection, create_table, insert_hotel

database = "hotels.db"

sql_create_hotels_table = """
CREATE TABLE IF NOT EXISTS hotels (
    id integer PRIMARY KEY,
    city text NOT NULL,
    name text NOT NULL,
    cleanliness real,
    room real,
    service real,
    location real,
    value real,
    safety real,
    comfort real,
    transportation real,
    noise real
);
"""


def process_hotel_name(hotel_name):
    parts = hotel_name.split('_')[2:]  # Skip the first two parts
    capitalized_parts = [part.capitalize() for part in parts]
    return ' '.join(capitalized_parts)


def main():
    conn = create_connection(database)
    with conn:
        conn.execute("DROP TABLE IF EXISTS hotels")

    if conn is not None:
        create_table(conn, sql_create_hotels_table)
    else:
        print("Error! cannot create the database connection.")

    cities = ["Beijing", "Dubai", "Chicago", "Las Vegas", "London", "Montreal", "New Delhi", "San Francisco", "Shanghai"]
    for city in cities:
        with open(f'csv/{city}.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)  # skip the header
            for row in reader:
                hotel_name = process_hotel_name(row[0])
                hotel = (
                    city,
                    hotel_name,
                    float(row[2]),  # cleanliness_score
                    float(row[3]),  # room_score
                    float(row[4]),  # service_score
                    float(row[5]),  # location_score
                    float(row[6]),  # value_score
                    float(row[7]),  # safety_score
                    float(row[8]),  # comfort_score
                    float(row[9]),  # transportation_score
                    float(row[10])  # noise_score
                )
                insert_hotel(conn, hotel)

    conn.close()


if __name__ == '__main__':
    main()
