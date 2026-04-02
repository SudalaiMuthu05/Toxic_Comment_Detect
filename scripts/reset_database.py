import sqlite3

# Database reset function

def reset_database():
    # Connect to the database (this will create the database if it does not exist)
    conn = sqlite3.connect('toxic_comments.db')
    cursor = conn.cursor()

    # Drop tables if they exist
    cursor.execute('DROP TABLE IF EXISTS comments;')
    cursor.execute('DROP TABLE IF EXISTS users;')

    # Create tables
    cursor.execute('''
    CREATE TABLE users (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    ''')

    cursor.execute('''
    CREATE TABLE comments (
        id INTEGER PRIMARY KEY,
        user_id INTEGER,
        comment_text TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(user_id) REFERENCES users(id)
    );
    ''')

    # Setup default admin user
    cursor.execute('''
    INSERT INTO users (username, email) VALUES (
        'admin', 'admin@example.com'
    );
    ''')

    # Commit changes and close the connection
    conn.commit()
    conn.close()

if __name__ == '__main__':
    reset_database()