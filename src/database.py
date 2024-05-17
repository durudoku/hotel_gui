import sqlite3

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)
    return conn

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except sqlite3.Error as e:
        print(e)

def insert_hotel(conn, hotel):
    sql = ''' INSERT INTO hotels(city, name, cleanliness, room, service, location, value, safety, comfort, transportation, noise)
              VALUES(?,?,?,?,?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, hotel)
    conn.commit()
    return cur.lastrowid

def select_all_hotels(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM hotels")
    rows = cur.fetchall()
    for row in rows:
        print(row)

def select_hotels_by_city(conn, city):
    cur = conn.cursor()
    cur.execute("SELECT * FROM hotels WHERE city=?", (city,))
    rows = cur.fetchall()
    if rows is None:
        return []
    return rows
