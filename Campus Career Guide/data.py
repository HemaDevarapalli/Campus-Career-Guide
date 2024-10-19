import sqlite3
import pandas as pd
def init_database():
    conn = sqlite3.connect('company.db')
    c = conn.cursor()
# Drop the table if it exists
    c.execute('''DROP TABLE IF EXISTS StudentPro''')

    # Create the table with correct schema
    c.execute('''
        CREATE TABLE IF NOT EXISTS StudentPro (
            id VARCHAR PRIMARY KEY,
            name TEXT UNIQUE,
            email VARCHAR NOT NULL,
            Company VARCHAR NOT NULL,
            position VARCHAR NOT NULL,
            PhNo INTEGER NOT NULL
        )
    ''')

    # Insert the data
    hostels_data = [
        ("22B01A42X1","sahithi","sa51@gmail.com","Meesho","Software Developer",912345678),
        ("22B01a4211","hari","hari@gmail.com","Meesho","tester",823456789),
        ("22B01A42X2","kalyani","kalyani@gmail.com","Flipkart","Tester",723456789),
        ("22B01a4222","sri","sri@gmail.com","Flipkart","Developer",82345789),
        ("22B01a42X3","gowri","gowri@gmail.com","Amazon", "Analyst",934567890),
        ("22b01a4233","sai","sai@gmail.com","Amazon","Tester",712345678),
        ("22B01a42Z2","mohi","mohi@gmail.com", "NXP","FullStack",945678901),
    ]

    c.executemany('''
        INSERT INTO StudentPro (id,name,email, Company, position, PhNo) VALUES (?, ?, ?, ?, ?,?)
    ''', hostels_data)

    conn.commit()
    conn.close()

def display_database():
    conn = sqlite3.connect('company.db')

    # Read the data from the database into a DataFrame
    df = pd.read_sql_query("SELECT * FROM StudentPro", conn)

    # Display the DataFrame
    print(df)

    conn.close()

# Initialize the database
init_database()

# Display the data in a frame
display_database()