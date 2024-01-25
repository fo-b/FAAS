import sqlite3
import os

def create_database():
    # Check if the database file already exists
    if not os.path.isfile('thermostat_values.db'):
        # Database connection
        conn = sqlite3.connect('thermostat_values.db')
        cursor = conn.cursor()

        # Create a table if it doesn't exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS thermostat_values (
                temperature REAL PRIMARY KEY,
                description TEXT
            )
        ''')
        conn.commit()

        # Define initial thermostat values
        initial_values = [
            (30, "Uff, this is hot"),
            (20, "Neutral temperature"),
            (-15, "Brrr, this is cold"),
        ]

        # Insert initial values into the database
        cursor.executemany('INSERT INTO thermostat_values (temperature, description) VALUES (?, ?)', initial_values)
        conn.commit()

        print("Database setup complete.")
    else:
        print("Database already exists.")

def load_thermostat_values():
    # Database connection
    conn = sqlite3.connect('thermostat_values.db')
    cursor = conn.cursor()

    cursor.execute('SELECT temperature, description FROM thermostat_values')
    rows = cursor.fetchall()
    return {float(row[0]): row[1] for row in rows}
