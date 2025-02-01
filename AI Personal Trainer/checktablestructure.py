import sqlite3

# Connect to the database
conn = sqlite3.connect('user_data.db')
cursor = conn.cursor()

# Add the new column 'goals'
cursor.execute('ALTER TABLE user_inputs ADD COLUMN goals TEXT')

# Commit the changes and close the connection
conn.commit()
conn.close()
