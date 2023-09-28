# Import the necessary libraries
import os

# Function to create an API documentation entry
def create_api_entry():
    tableName = input("Table Name: " )
    
    # Generate the Markdown entry
    content = f"""### {tableName.capitalize()} Table
To populate the {tableName} table using a Python script from an Excel file, follow the following steps:

1. Create an Excel file containing the data for the {tableName} table.

2. Write a Python script to read data from the Excel file and insert it into the "{tableName}" table.

3. Execute the Python script to populate the {tableName} table.

**Table Desc**

The {tableName} table has the following fields:

- `` (string, required): The .

The following script can be used after making a few changes(like, csv file name, dbconfig):

```python
import pandas as pd
import mysql.connector

# MySQL database connection settings
# The username and password of a db user with CRUD privileges
db_config = {
    "host": "localhost",
    "user": "username",
    "password": "password",
    "database": "dbName",
}

# Excel file path
excel_file = "{tableName}.xlsx"

# Sheet name, the name of the sheet to look for in the excel workbook
sheet_name = "Sheet1"

# Connect to the MySQL database
try:
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
except mysql.connector.Error as err:
    print("Error connecting to MySQL:", err)
    exit()

# Read Excel file using pandas
try:
    df = pd.read_excel(excel_file, sheet_name=sheet_name)

    # The name of the headings in the excel file(change based on excel file, order is important)
    df = df[["", ""]]

    # Fill all null values with ""
    df = df.fillna("")
except Exception as e:
    print("Error reading Excel:", e)
    cursor.close()
    connection.close()
    exit()

# Convert the Excel data to a list of dictionaries
data_to_insert = df.to_dict(orient="records")

# Insert data into the MySQL database
try:
    for row in data_to_insert:
        query = "INSERT INTO parts(a, b) VALUES (%s, %s)"
        values = tuple(row.values())
        cursor.execute(query, values)
    connection.commit()
    print("Data inserted successfully.")
except mysql.connector.Error as err:
    print("Error inserting data into MySQL:", err)
    connection.rollback()

# Close the cursor and connection
cursor.close()
connection.close()
```
<br>
"""

    # Append the entry to the documentation file
    with open("test.md", "a") as file:
        file.write(markdown_entry)

# Main script
if __name__ == "__main__":
    create_api_entry()

print("API documentation created successfully.")
