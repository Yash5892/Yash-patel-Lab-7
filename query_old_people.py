import sqlite3
import pandas as pd

# Connect to the SQLite database
conn = sqlite3.connect('people.db')
cursor = conn.cursor()

# Execute SQL query to get name and age of people 50 and older
cursor.execute('''
SELECT name, age
FROM people
WHERE age >= 50
LIMIT 1000  -- Added LIMIT as per hint, adjust as needed
''')

# Fetch all results
results = cursor.fetchall()

# Print results in sentences
for name, age in results:
    print(f"{name} is {age} years old.")

# Convert results to a DataFrame
df = pd.DataFrame(results, columns=['Name', 'Age'])

# Save to CSV
csv_filename = 'old_people.csv'
df.to_csv(csv_filename, index=False)

print(f"Data saved to {csv_filename}")

# Close the connection
conn.close()