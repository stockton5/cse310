import sqlite3

DATABASE_FILE = "hunting_trips.db"


def connect_database():
    """Connect to the SQLite database."""
    return sqlite3.connect(DATABASE_FILE)


def create_table():
    """Create the hunting_trips table if it does not exist."""
    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS hunting_trips (
            trip_id INTEGER PRIMARY KEY AUTOINCREMENT,
            location TEXT NOT NULL,
            animal TEXT NOT NULL,
            trip_date TEXT NOT NULL,
            result TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


def add_trip(location, animal, trip_date, result):
    """Insert a new hunting trip."""
    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO hunting_trips
        (location, animal, trip_date, result)
        VALUES (?, ?, ?, ?)
    """, (location, animal, trip_date, result))

    connection.commit()
    connection.close()


def get_all_trips():
    """Retrieve every hunting trip."""
    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT trip_id, location, animal, trip_date, result
        FROM hunting_trips
        ORDER BY trip_date
    """)

    trips = cursor.fetchall()
    connection.close()
    return trips


def update_trip_result(trip_id, new_result):
    """Modify the result of an existing trip."""
    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE hunting_trips
        SET result = ?
        WHERE trip_id = ?
    """, (new_result, trip_id))

    connection.commit()
    changed_rows = cursor.rowcount
    connection.close()
    return changed_rows


def delete_trip(trip_id):
    """Delete a hunting trip."""
    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("""
        DELETE FROM hunting_trips
        WHERE trip_id = ?
    """, (trip_id,))

    connection.commit()
    deleted_rows = cursor.rowcount
    connection.close()
    return deleted_rows


def get_animal_report():
    """Return the number of trips for each animal."""
    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT animal, COUNT(*) AS total_trips
        FROM hunting_trips
        GROUP BY animal
        ORDER BY total_trips DESC
    """)

    report = cursor.fetchall()
    connection.close()
    return report