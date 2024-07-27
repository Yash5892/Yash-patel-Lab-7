import sqlite3
from faker import Faker
import random
from datetime import datetime

# Initialize Faker
fake = Faker()

conn = sqlite3.connect('people.db')
cursor = conn.cursor()

# Create people table
cursor.execute('''
CREATE TABLE IF NOT EXISTS people (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    age INTEGER,
    created_at DATETIME,
    updated_at DATETIME
)
''')

# Get current date and time
current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# Insert 200 fake people
for _ in range(200):
    name = fake.name()
    email = fake.email()
    age = random.randint(1, 100)  # Using random module as specified
    
    cursor.execute('''
    INSERT INTO people (name, email, age, created_at, updated_at)
    VALUES (?, ?, ?, ?, ?)
    ''', (name, email, age, current_time, current_time))

# Commit changes and close connection
conn.commit()
conn.close()

print("Database created and populated with 200 fake people.")