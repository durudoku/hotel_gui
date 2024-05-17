import sqlite3

def create_connection(db_file):
    """ create a database connection to the SQLite database specified by db_file """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)
    return conn

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except sqlite3.Error as e:
        print(e)

def insert_hotel(conn, hotel):
    """
    Create a new hotel into the hotels table
    """
    sql = ''' INSERT INTO hotels(city, name, cleanliness, room, service, location, value, safety, comfort, transportation, noise)
              VALUES(?,?,?,?,?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, hotel)
    conn.commit()
    return cur.lastrowid

def select_all_hotels(conn):
    """
    Query all rows in the hotels table
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM hotels")
    rows = cur.fetchall()
    for row in rows:
        print(row)

def select_hotels_by_city(conn, city):
    """
    Query hotels by city
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM hotels WHERE city=?", (city,))
    rows = cur.fetchall()
    if rows is None:
        return []
    return rows
