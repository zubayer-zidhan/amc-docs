# Database Population Documentation

This documentation explains how to populate various tables in the database using different methods.



- [Database Population Documentation](#database-population-documentation)
  - [API-Based Population](#api-based-population)
    - [Users Table](#users-table)
    - [Add New Vehicle (vehicle\_details, amc\_availability, warranty\_availability Tables)](#add-new-vehicle-vehicle_details-amc_availability-warranty_availability-tables)
    - [Add New Workshop (workshops table)](#add-new-workshop-workshops-table)
    - [Invoices table](#invoices-table)
  - [Excel Based Population](#excel-based-population)
    - [Parts Table](#parts-table)
    - [AMC Table](#amc-table)
    - [Warranty Table](#warranty-table)
    - [Basic Details Table](#basic-details-table)
    - [AMC Scopes Table](#amc-scopes-table)
    - [Warranty Scopes Table](#warranty-scopes-table)
    - [Automovill Homes Table](#automovill-homes-table)


## API-Based Population

### Users Table

To populate the "users" table via the API, follow the following steps:
1. An admin user JWT is required in order create other account, use that token for authorization.
2. Send a POST request to the API endpoint.
3. Send a request body with the required fields.
4. A JSON Web Token(JWT) will be returned, which can be used for authorization during future API calls.

**Endpoint URL:** `/api/v1/auth/register`

**HTTP Method:** POST

**Description:** Register new users.

**Request Parameters:**
- Request Body

**Request Body:**
The request body for a POST request to register new users should be in JSON format and include the following fields:

- `username` (string, required): The username of the workshop/users.
- `password` (string, required): The password for the workshop/users.
- `admin` (boolean, required): The role of the user is admin or not(true or false).

**Response:**
- Status Code: 200 OK
- Response Body: JSON.

**Response Body:**
The response body includes the following fields:
- `token` (string): A JSON Web Token(JWT) that can be used to verify a user's identity in future API calls.

**Example Request:**

```http
POST /api/v1/auth/register
Content-Type: application/json
{
    "username": "workshop12",
    "password": "pass",
    "admin": false   
}
```

**Example Response:**
```http
HTTP/1.1 200 OK
Content-Type: application/json
{
    "token": "eyJhbGciOiJIUzI1NiJ9.eyJyb2xlIjpbeyJhdXRob3JpdHkiOiJST0xFX1VTRVIifV0sInN1YiI6IndvcmtzaG9wMTIiLCJpYXQiOjE2OTU1ODg1MzksImV4cCI6MTY5Njg4NDUzOX0.N6cfpqJnrnEX46cUvp3RAbnTd0dB1Jq7HUE-Q2msMcI"
}
```
<br>

### Add New Vehicle (vehicle_details, amc_availability, warranty_availability Tables)
To add a new vehicle to the database via the API, follow the following steps:
1. An admin user JWT is required in order create other account, use that token for authorization.
2. Send a POST request to the API endpoint.
3. Send a request body with the required fields.
4. A "string" will be returned, "SUCCESS" or "FAILURE".

**Endpoint URL:** `/api/v1/admin/addNewVehicle`

**HTTP Method:** POST

**Description:** Add new vehicle.

**Request Parameters:**
- Request Body

**Request Body:**
The request body for a POST request to add a new vehicle should be in JSON format and include the following fields:
- `chassis_num` (string, required): The chassis number of the vehicle to be added.
- `make` (string, required): The make of the vehicle to be added.
- `model` (string, required): The model of the vehicle to be added.
- `fuel_type` (string, required): The fuel type of the vehicle to be added.
- `phone_number` (string, required): The phone number of the owner.
- `reg_date` (string, required): The date of registration of the vehicle.
- `warranty_start` (string, required): The warranty start date of the vehicle.
- `warranty_end` (string, required): The warranty end date of the vehicle.
- `amc_start` (string, required): The amc start date of the vehicle.
- `amc_end` (string, required): The amc end date of the vehicle.
- `warranty_id` (int, required): The id of the warranty type availed by the vehicle. This is used to populate the warranty_availability table.
- `amc_id` (int, required): The id of the amc type availed by the vehicle. This is used to populate the amc_availability table.

**Response:**
- Status Code: 200 OK
- Response Body: String.

**Response Body:**
The response body includes the following fields:
- `token` (string): A JSON Web Token(JWT) that can be used to verify a user's identity in future API calls.

**Example Request:**

```http
POST /api/v1/auth/register
Content-Type: application/json
{
    "chassis_num": "CHVH015",
    "make": "Fujiyama",
    "model": "Spectra",
    "fuel_type": "Electric(156 KWH)",
    "phone_number": "2856423224",
    "owner": "Fujiyama",
    "reg_date": "2023-02-16",
    "warranty_start": "2023-02-16",
    "warranty_end": "2025-02-16",
    "amc_start_date": "2023-02-16",
    "amc_end_date": "2024-02-16",
    "amc_id": 1,
    "warranty_id": 1
}
```

**Example Response:**
```http
HTTP/1.1 200 OK
Content-Type: text/plain
"Added Successfully"
```
<br>

### Add New Workshop (workshops table)
To add a new workshop to the database via the API, follow the following steps:
1. An admin user JWT is required in order create other account, use that token for authorization.
2. The workshop to be added must already be added as an user, if not already added, refer how to add to [user_table](#users-table) 
3. Send a POST request to the API endpoint.
4. Send a request body with the required fields.
5. A "string" will be returned, "SUCCESS" or "FAILURE".

**Endpoint URL:** `/api/v1/admin/addNewWorkshop`

**HTTP Method:** POST

**Description:** Add new workshop.

**Request Parameters:**
- Request Body

**Request Body:**
The request body for a POST request to add a new workshop should be in JSON format and include the following fields:
- `state` (string, required): The name of the state to which the workshop belongs.
- `name` (string, required): The username of the workshop to be added.
- `address` (string, required): The address of the workshop to be added.
- `pin` (string, required): The pin code of the workshop to be added.
- `contact` (string, required): The contact number of the workshop to be added.

**Response:**
- Status Code: 200 OK
- Response Body: String.

**Response Body:**
The response body includes the following fields:
- `token` (string): A JSON Web Token(JWT) that can be used to verify a user's identity in future API calls.

**Example Request:**

```http
POST /api/v1/auth/register
Content-Type: application/json
{
    "name": "workshop18",
    "state": "Assam",
    "address": "Address-9",
    "pin": "98628",
    "contact": "127832417"
}
```

**Example Response:**
```http
HTTP/1.1 200 OK
Content-Type: text/plain
"Added Successfully"
```
<br>

### Invoices table
- To add a new invoice to the invoice table, an API call is made from the amc_app.
- It is filled gradually with the creation of invoices, and as amc and warranty are availed, or, servicing is done.
- Not required to fill this table while initial population of database

## Excel Based Population

### Parts Table
This table has the list of all possible scopes of work that can be performed in a vehicle.

To populate the "parts" table using a Python script from an Excel file, follow the following steps:

1. Create an Excel file containing the data for the "parts" table.
2. Write a Python script to read data from the Excel file and insert it into the "parts" table.
3. Execute the python script to populate the "parts" table.

**Table Desc**<br>
The "parts" table has the following fields:
- `id` (int, auto generated): The id of the tuple(row) in the table. It is auto-generated by MySQL if null value is passed in its place.
- `part_code` (String, required): The part_code of that part. It is unique for each part.
- `item_name` (String, required): The name of that part.
- `price` (String, required): The price of that part.
- `hsn` (String, required): The hsn of that part.
- `tax` (String, required): The tax applicable on that part.

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
excel_file = "parts.xlsx"

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
    df = df[["PART CODE", "ITEM NAME", "Revised Price Spectra", "HSN", "Tax Category(in %)"]]

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
        query = "INSERT INTO parts(part_code, item_name, price, hsn, tax) VALUES (%s, %s, %s, %s, %s)"
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

### AMC Table
This table has the id's of the AMC types, and their names.

To populate the "amc" table using a Python script from an Excel file, follow the following steps:

1. Create an Excel file containing the data for the "amc" table.
2. Write a Python script to read data from the Excel file and insert it into the "amc" table.
3. Execute the python script to populate the "amc" table.

**Table Desc**<br>
The "amc" table has the following fields:
- `id` (int, auto generated): The id of the tuple(row) in the table. It is auto-generated by MySQL if null value is passed in its place.
- `name` (String, required): The name of the AMC.
- `type` (String, required): The type of the AMC.

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
excel_file = "amc.xlsx"

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
    df = df[["", "", ""]]

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
        query = "INSERT INTO amc(id, name, type) VALUES (%s, %s, %s)"
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

### Warranty Table
This table has the id's of the WTY types, and their names.

To populate the "warranty" table follow the same steps as AMC, just replace "amc" with "warranty".
<br>

### Basic Details Table
This table has all of the basic details for a vehicle of particular type. 

To populate the "basic_details" table using a Python script from an Excel file, follow the following steps:

1. Create an Excel file containing the data for the "basic_details" table.
2. Write a Python script to read data from the Excel file and insert it into the "basic_details" table.
3. Execute the python script to populate the "basic_details" table.

**Table Desc**<br>
The "basic_details" table has the following fields:
- id (string): The unique identifier of the vehicle.
- make (string): The make or manufacturer of the vehicle.
- model (string): The model of the vehicle.
- fuelType (string): The type of fuel the vehicle uses.
- ratedPower (string): The rated power of the vehicle's engine.
- peakPower (string): The peak power of the vehicle's engine.
- seatHeight (string): The seat height of the vehicle.
- loadingCapacity (string): The loading capacity of the vehicle.
- speedometer (string): Information about the vehicle's speedometer.
- batteryType (string): The type of battery used in the vehicle.
- controller (string): Information about the vehicle's controller.
- brakeSystem (string): Information about the vehicle's brake system.
- dimensions (string): The dimensions of the vehicle.
- tyre (string): Information about the vehicle's tires.
- chargingTime (string): The charging time for the vehicle's battery.
- chargerSpecs (string): Specifications of the vehicle's charger.
- voltage (string): The voltage used by the vehicle.
- suspension (string): Information about the vehicle's suspension.
- mileage (string): The mileage of the vehicle.
- groundClearance (string): The ground clearance of the vehicle.
- icat (string): Information about the vehicle's ICAT compliance.
- floorMat (string): Information about the vehicle's floor mat.
- topSpeed (string): The top speed of the vehicle.
- wheel (string): Information about the vehicle's wheel.
- headlight (string): Information about the vehicle's headlight.
- backlight (string): Information about the vehicle's backlight.
- brakeLever (string): Information about the vehicle's brake lever.
- batteryWarranty (string): Warranty information for the vehicle's battery.

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
excel_file = "basic_details.xlsx"

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
    df = df[["", "", ""]]

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
        query = "INSERT INTO basic_details("", "") VALUES (%s, %s, %s)"
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

### AMC Scopes Table
This table has the list of scopes for each amc type(id), and works as the blueprint for creating the "amc-availability" table.

To populate the "amc_scopes" table using a Python script from an Excel file, follow the following steps:

1. Create an Excel file containing the data for the "amc_scopes" table.
2. Write a Python script to read data from the Excel file and insert it into the "amc_scopes" table.
3. Execute the python script to populate the "amc_scopes" table.

**Table Desc**<br>
The "amc_scopes" table has the following fields:
- id (integer): The unique identifier for the AMC scope.
- amcId (integer): The identifier of the associated Annual Maintenance Contract.
- scopeOfWork (string): A description of the scope of work.
- details (string): Additional details about the scope of work.
- frequency (integer): The frequency at which the scope of work is performed.

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
excel_file = "amc_scopes.xlsx"

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
    df = df[["", "", ""]]

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
        query = "INSERT INTO amc_scopes(id, amc_id, scope_of_work, details, frequency) VALUES (%s, %s, %s, %s, %s)"
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

### Warranty Scopes Table
This table has the list of scopes for each warranty type(id), and works as the blueprint for creating the "warranty-availability" table.

To populate the "warranty_scopes" table follow the same steps as amc_scopes, just replace "amc_scopes" with "warranty_scopes".
<br>

### Automovill Homes Table
This table has the information about all the automovill offices in different states.

To populate the "automovill_homes" table using a Python script from an Excel file, follow the following steps:

1. Create an Excel file containing the data for the "automovill_homes" table.
2. Write a Python script to read data from the Excel file and insert it into the "automovill_homes" table.
3. Execute the python script to populate the "automovill_homes" table.

**Table Desc**<br>
The "automovill_homes" table has the following fields:
- `id` (string): The id of the entry in the table.
- `state` (string): The state to which the workshop belongs.
- `gstin` (string): The gst number for the office in that state.
- `cin` (string): The cin for the office in that state.
- `pan` (string): The pan for the office in that state.

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
excel_file = "automovill_homes.xlsx"

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
    df = df[["", "", ""]]

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
        query = "INSERT INTO automovill_homes(state, address, gstin, cin, pan) VALUES (%s, %s, %s)"
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
