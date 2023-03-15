import sqlite3

# Connect to the database
conn = sqlite3.connect('users.db')

# Create a cursor object
c = conn.cursor()

# Create the users table in second normal form
c.execute('''CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT NOT NULL,
                password TEXT NOT NULL,
                email TEXT NOT NULL,
                over_13 INTEGER NOT NULL,
                CONSTRAINT unique_username UNIQUE (username)
            )''')

# Create the user_preferences table in second normal form
c.execute('''CREATE TABLE IF NOT EXISTS user_preferences (
                id INTEGER PRIMARY KEY,
                user_id INTEGER NOT NULL,
                custom_regions TEXT,
                custom_notifications TEXT,
                custom_conditions TEXT,
                phone_number TEXT,
                FOREIGN KEY (user_id) REFERENCES users(id)
            )''')

# Commit changes to the database
conn.commit()

# Close the database connection
conn.close()
