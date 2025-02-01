import sqlite3

# Connect to the database
conn = sqlite3.connect('user_data.db')
cursor = conn.cursor()

# Drop the existing table if it exists
cursor.execute("DROP TABLE IF EXISTS user_inputs")
conn.commit()

# Create the table with the notes column
cursor.execute('''
CREATE TABLE user_inputs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    height TEXT,
    weight REAL,
    gender TEXT,
    activity_level TEXT,
    notes TEXT,
    goals TEXT
)
''')
conn.commit()

conn.close()
