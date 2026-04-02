# Script to create users table in the database

import sqlite3

# Connect to the SQLite database
connection = sqlite3.connect('database.db')

# Create a cursor object
cursor = connection.cursor()

# Create users table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
''')

# Commit the changes and close the connection
connection.commit()
connection.close()
