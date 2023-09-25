# Import the necessary libraries
import os


# Function to create an API documentation entry
def create_doc_entry():
    table = input("Enter name of table: ")
    
    # Generate the Markdown entry
    # Excel Based
    excel_based = f"""### { table.capitalize() } Table
To populate the "{ table }" table using a Python script from an Excel file, follow the following steps:

1. Create an Excel file containing the data for the "{table}" table.
2. Write a Python script to read data from the Excel file and insert it into the "{table}" table.
3. Execute the python script to populate the "{table}" table.

**Table Desc**
The "{table}" table has the following fields:
- `` (string, required): The .

The following script can be used after making a few changes(like, csv file name, dbconfig): 
```python
import pandas as pd
import mysql.connector

# MySQL database connection settings
# The username and password of a db user with CRUD priveleges
db_config = {
    "host": "localhost",
    "user": "username",  
    "password": "password",
    "database": "dbName",
}

# Excel file path
excel_file = "{table}.xlsx"

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
# print(data_to_insert)


# Insert data into the MySQL database
try:
    for row in data_to_insert:
        query = "INSERT INTO parts(a, b) VALUES (%s, %s)"
        values = tuple(row.values())
        # print(values)
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
    with open("database_population_documentation.md", "a") as file:
        file.write(markdown_entry)

# Main script
if __name__ == "__main__":
    create_doc_entry()

print("Table Population Documentation created successfully.")
