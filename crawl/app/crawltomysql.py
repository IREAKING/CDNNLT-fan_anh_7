import mysql.connector
from crawl import df

connection = mysql.connector.connect(
    host="mysql",
    user="root",
    password="Future0x",
    database="fana7"
)
cursor = connection.cursor()

create_table_query = """
CREATE TABLE IF NOT EXISTS foody (
    Id INT PRIMARY KEY,
    Name VARCHAR(255),
    Address VARCHAR(255),
    Phone VARCHAR(50),
    Image VARCHAR(255)
)
"""
cursor.execute(create_table_query)

for _, row in df.iterrows():
    insert_query = """
    INSERT IGNORE INTO foody (Id, Name, Address, Phone, Image) 
    VALUES (%s, %s, %s, %s, %s)
    """
    cursor.execute(insert_query, (row['Id'], row['Name'], row['Address'], row['Phone'], row['Image']))

connection.commit()

cursor.close()
connection.close()
