- [Authentication Controller](#authentication-controller)
  - [Register new users](#register-new-users)
  - [Authenticate the existing users](#authenticate-the-existing-users)
- [Admin Controller](#admin-controller)
  - [Add a new vehicle](#add-a-new-vehicle)
  - [Add a new workshop](#add-a-new-workshop)
- [AMC Controller](#amc-controller)
  - [Get list of all available types of AMCs.](#get-list-of-all-available-types-of-amcs)
- [AMC Scopes Controller](#amc-scopes-controller)
  - [Get Access to the AMC scopes table.](#get-access-to-the-amc-scopes-table)
- [AMC Availability Controller](#amc-availability-controller)
  - [Check if a particular part/scope is covered by AMC](#check-if-a-particular-partscope-is-covered-by-amc)
  - [Get the list of all scopes covered by AMC for the concerned vehicle](#get-the-list-of-all-scopes-covered-by-amc-for-the-concerned-vehicle)
- [Automovill Homes Controller](#automovill-homes-controller)
  - [Get information about the automovill offices in concerned state](#get-information-about-the-automovill-offices-in-concerned-state)
  - [Get all homes for all states](#get-all-homes-for-all-states)
- [Basic Details Controller](#basic-details-controller)
  - [Get Basic Details of all Vehicles](#get-basic-details-of-all-vehicles)
  - [Get Basic Details of the concerned vehicle](#get-basic-details-of-the-concerned-vehicle)
- [Invoices Controller](#invoices-controller)
  - [Add new Invoices into the Database.](#add-new-invoices-into-the-database)
  - [Get all the invoices that have been generated.](#get-all-the-invoices-that-have-been-generated)
  - [Get the generated invoice for a particular vehicle.](#get-the-generated-invoice-for-a-particular-vehicle)
- [Parts Controller](#parts-controller)
  - [Get the details of all the scopes of services available.](#get-the-details-of-all-the-scopes-of-services-available)
- [Vehicle Details Controller](#vehicle-details-controller)
  - [Get the details of a particular vehicle.](#get-the-details-of-a-particular-vehicle)
- [Warranty Availability Controller](#warranty-availability-controller)
  - [Check if a particular part/scope is covered by Warranty](#check-if-a-particular-partscope-is-covered-by-warranty)
  - [Get the list of all scopes covered by Warranty for the concerned vehicle](#get-the-list-of-all-scopes-covered-by-warranty-for-the-concerned-vehicle)
- [WarrantyScopes Controller](#warrantyscopes-controller)
  - [Get the list of all scopes covered under "Warranty".](#get-the-list-of-all-scopes-covered-under-warranty)



# Authentication Controller
The auth api end-points are open for all. No JWT tokens required.
## Register new users

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

## Authenticate the existing users

**Endpoint URL:** `/api/v1/auth/authenticate`

**HTTP Method:** POST

**Description:** Authenticate the existing users.

**Request Parameters:**
- Request Body .

**Request Body:**
The request body for a POST request to authenticate the existing users should be in JSON format and include the following fields:

- `username` (string, required): The username for the workshop/user .
- `password` (string, required): The password for the workshop/user .

**Response:**
- Status Code: 200 OK
- Response Body: JSON.

**Response Body:**
The response body includes the following fields:
- `token` (string): Machine-generated codes to verify a user's identity .

**Example Request:**

```http
POST /api/v1/auth/authenticate
Content-Type: application/json
{
    "password": "pass", 
    "username": "workshop12"
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

# Admin Controller
These end-points can only be accessed using a jwt token for a user with admin priveleges.
## Add a new vehicle

**Endpoint URL:** `/api/v1/admin/addNewVehicle`

**HTTP Method:** POST

**Description:** Add a new vehicle to the database.

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
- `warranty_id` (int, required): The id of the warranty type availed by the vehicle.
- `amc_id` (int, required): The id of the amc type availed by the vehicle.

**Response:**
- Status Code: 200 OK
- Response Body: String.


**Example Request:**

```http
POST /api/v1/admin/addNewVehicle
Authorization: Bearer token
Content-Type: application/json
{
    "chassis_num": "CHVH013",
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

## Add a new workshop

**Endpoint URL:** `/api/v1/admin/addNewWorkshop`

**HTTP Method:** POST

**Description:** Add a new workshop to the database..

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

**Example Request:**

```http
POST /api/v1/admin/addNewWorkshop
Authorization: Bearer token
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

All the remaining end-points can be accessed using a jwt token with user level or above priveleges

# AMC Controller 

## Get list of all available types of AMCs.

**Endpoint URL:** `/api/v1/api/v1/amc/details`

**HTTP Method:** GET

**Description:** Get list of all available types of AMCs.

**Request Parameters:**

- Request Parameters: None .

**Response:**

- Status Code: 200 OK
- Response Body: List of JSON objects.

**Response Body:**
Each item of the response body includes the following fields:
- id (integer): The unique identifier for the AMC contract.
- name (string): The name or title of the AMC contract.
- type (string): The type or category of the AMC contract.

**Example Request:**

```http
GET /api/v1//api/v1/amc/details
```

**Example Response:**

```http
HTTP/1.1 200 OK
Content-Type: application/json
[
    {
        "id": 1,
        "name": "amc1",
        "type": "basic"
    },
    {
        "id": 2,
        "name": "amc2",
        "type": "deluxe"
    },
]
```

<br>

# AMC Scopes Controller

## Get Access to the AMC scopes table.

**Endpoint URL:** `/api/v1/amc/amcScopes`

**HTTP Method:** GET

**Description:** Get Access to the AMC scopes table, which contains the blueprint for amc_availability table.

**Response:**
- Status Code: 200 OK
- Response Body: List of JSON objects.

**Response Body:**
Each item in the response body includes the following fields:
- id (integer): The unique identifier for the AMC scope.
- amcId (integer): The identifier of the associated Annual Maintenance Contract.
- scopeOfWork (string): A description of the scope of work.
- details (string): Additional details about the scope of work.
- frequency (integer): The frequency at which the scope of work is performed.

**Example Request:**

```http
GET /api/v1//api/v1/amc/details
```

**Example Response:**

```http
HTTP/1.1 200 OK
Content-Type: application/json
[
    {
        "id": 10,
        "amcId": 1,
        "scopeOfWork": "Head light",
        "details": "Change headlight(in total lifetime)",
        "frequency": 1
    },
    {
        "id": 11,
        "amcId": 1,
        "scopeOfWork": "Handle Bar",
        "details": "Change Handle Bar (in total lifetime)",
        "frequency": 2
    },
    {
        "id": 12,
        "amcId": 1,
        "scopeOfWork": "Wire Harness",
        "details": "Change (in total lifetime)",
        "frequency": 3
    }
]
```

<br>

# AMC Availability Controller
## Check if a particular part/scope is covered by AMC

**Endpoint URL:** `/api/v1/amc-availability/availability`

**HTTP Method:** GET

**Description:** Check if a particular part is covered by AMC.

**Request Parameters:**
- `chassis_num` (query parameter, string, required): The chassis_num of the concerned vehicle.
- `scope` (query parameter, string, required): The concerened part/scope for which the amc-availability is to be checked.


**Response:**
- Status Code: 200 OK
- Response Body: JSON.

**Response Body:**
The response body includes the following fields:
- `available` (string): The number of times the concerned part/scope can still be repaired for free under AMC.
- `total` (string): The number of times the concerned part/scope can be repaired(in total) for free under AMC.

**Example Request:**

```http
GET /api/v1/amc-availability/availability?chassis_num=CHVH008&scope=Handle%20Bar
```

**Example Response:**
```http
HTTP/1.1 200 OK
Content-Type: application/json
{
    "available": 2,
    "total": 2
}
```
<br>

## Get the list of all scopes covered by AMC for the concerned vehicle

**Endpoint URL:** `/api/v1/amc-availability/{chassisNum}`

**HTTP Method:** GET

**Description:** Get the list of all scopes covered by AMC for the concerned vehicle.

**Request Parameters:**
- `chassisNum` (path parameter): The chassis number of the concerned vehicle.

**Response:**
- Status Code: 200 OK
- Response Body: List of JSON objects.

**Response Body:**
Each item of the response body includes the following fields:
- `scopeOfWork` (string): The name of the scope covered by the AMC.
- `details` (string): Details about the scope.
- `frequency` (int): Total number of times the concerned scope can be repaired under AMC.

**Example Request:**

```http
GET /api/v1/amc-availability/CHVH001
```

**Example Response:**
```http
HTTP/1.1 200 OK
Content-Type: application/json
[
    {
        "scopeOfWork": "Head light",
        "details": "Change headlight(in total lifetime)",
        "frequency": 1
    },
    {
        "scopeOfWork": "Handle Bar",
        "details": "Change Handle Bar (in total lifetime)",
        "frequency": 2
    },
]
```
<br>

# Automovill Homes Controller
## Get information about the automovill offices in concerned state

**Endpoint URL:** `/api/v1/automovill-homes/{workshopId}`

**HTTP Method:** GET

**Description:** Get information about the autmovill offices in concerned state.

**Request Parameters:**
- `workshopId` (path parameter): The workshop id of the workshop in which the vehicle is taken to be serviced.


**Response:**
- Status Code: 200 OK
- Response Body: JSON.

**Response Body:**
The response body includes the following fields:
- `id` (string): The id of the entry in the table.
- `state` (string): The state to which the workshop belongs.
- `gstin` (string): The gst number for the office in that state.
- `cin` (string): The cin for the office in that state.
- `pan` (string): The pan for the office in that state.

**Example Request:**

```http
GET /api/v1/automovill-homes/workshop03
```

**Example Response:**
```http
HTTP/1.1 200 OK
Content-Type: application/json
{
    "id": 3,
    "state": "Madhya Pradesh",
    "address": "187, Ground Floor, 18th Cross. 2nd Main, KPC Layout, Kasavanahalli, MP-35",
    "gstin": "59VANCA9593J1ZQ",
    "cin": "K741IOKA201SPTC083874",
    "pan": "ALLCA9593J"
}
```
<br>

## Get all homes for all states

**Endpoint URL:** `/api/v1/automovill-homes/allHomes`

**HTTP Method:** GET

**Description:** Get the list of all homes from database..

**Request Parameters:**
- No request parameters required.

**Response:**
- Status Code: 200 OK
- Response Body: List of JSON objects.

**Response Body:**
Each item in the response body includes the following fields:
- `id` (string): The id of the entry in the table.
- `state` (string): The state to which the workshop belongs.
- `gstin` (string): The gst number for the office in that state.
- `cin` (string): The cin for the office in that state.
- `pan` (string): The pan for the office in that state.

**Example Request:**

```http
GET /api/v1/automovill-homes/allHomes
```

**Example Response:**
```http
HTTP/1.1 200 OK
Content-Type: application/json
[
    {
        "id": 1,
        "state": "Karnataka",
        "address": "900, Ground Floor, 18th Cross. 2nd Main, KPC Layout, Kasavanahalli, Bangalore-35",
        "gstin": "29AANCA9593J1ZQ",
        "cin": "U741IOKA201SPTC083874",
        "pan": "ABNCA9593J"
    },
    {
        "id": 2,
        "state": "Telengana",
        "address": "587, Ground Floor, 18th Cross. 2nd Main, KPC Layout, Kasavanahalli, T-35",
        "gstin": "89DANCA9593J1ZQ",
        "cin": "T741IOKA201SPTC083874",
        "pan": "ADDFA9593J"
    },
]
```
<br>

# Basic Details Controller

## Get Basic Details of all Vehicles

**Endpoint URL:** `/api/v1/api/v1/basic/allDetails`

**HTTP Method:** GET

**Description:** Get Basic Details of all Vehicles.

**Request Parameters:**
Request Parameters: None

**Response:**

- Status Code: 200 OK
- Response Body: List of JSON objects.

**Response Body:**
Each item of the response body includes the following fields:
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

**Example Request:**

```http
GET /api/v1/api/v1/basic/allDetails
```

**Example Response:**

```http
HTTP/1.1 200 OK
Content-Type: application/json
[
    {
        "id": "7e9dd8ae-40e9-11ee-831d-6045bdc60669",
        "make": "Fujiyama",
        "model": "Spectra",
        "fuelType": "Electric(156 KWH)",
        "rated_power": "250 Watt,BLDC Motor",
        "peak_power": "3700 Watt",
        "seat_height": "740 mm",
        "loading_capacity": "150 kg",
        "speedometer": "LCD",
        "battery_type": "1.56 KWH (Li-ion)(Detachable Battery)",
        "controller": "E-ABS",
        "brake_system": "Drum Brakes(Both)",
        "dimensions": "L-1730mm | W-690mm | H-1280mm",
        "tyre": "3.0 - 10 Tubeless(Both)",
        "charging_time": "4 -5 hrs",
        "charger_specs": "Micro-charger with Auto Cut",
        "voltage": "48V / 60V",
        "suspension": "Front:Hydraulic Telescopic,Rear:Double Shocker with Dual Tube Technology",
        "mileage": "80-90 km/charge",
        "ground_clearance": "160 mm",
        "icat": "Yes",
        "floor_mat": "Design Hard Mat",
        "top_speed": "25 kmph",
        "wheel": "Aluminium Alloy",
        "headlight": "LED with DRL",
        "backlight": "LED Winkers",
        "brake_lever": "Aluminium Alloy",
        "battery_warranty": "3 Years (Li-ion)"
    }
]
```

## Get Basic Details of the concerned vehicle

**Endpoint URL:** `/api/v1/basic/{id}`

**HTTP Method:** GET

**Description:** Get Basic Details of the concerned vehicle.

**Request Parameters:**

- id (string): The unique identifier of the vehicle

**Response:**

- Status Code: 200 OK
- Response Body: JSON.

**Request Body :** - None

**Response Body:**
The response body includes the following fields:
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
- batteryWarranty (string): Warranty information for the vehicle's battery..

**Example Request:**

```http
GET api/v1/basic/7e9dd8ae-40e9-11ee-831d-6045bdc60669
```

**Example Response:**

```http
HTTP/1.1 200 OK
Content-Type: application/json
{
    "id": "7e9dd8ae-40e9-11ee-831d-6045bdc60669",
    "make": "Fujiyama",
    "model": "Spectra",
    "fuelType": "Electric(156 KWH)",
    "rated_power": "250 Watt,BLDC Motor",
    "peak_power": "3700 Watt",
    "seat_height": "740 mm",
    "loading_capacity": "150 kg",
    "speedometer": "LCD",
    "battery_type": "1.56 KWH (Li-ion)(Detachable Battery)",
    "controller": "E-ABS",
    "brake_system": "Drum Brakes(Both)",
    "dimensions": "L-1730mm | W-690mm | H-1280mm",
    "tyre": "3.0 - 10 Tubeless(Both)",
    "charging_time": "4 -5 hrs",
    "charger_specs": "Micro-charger with Auto Cut",
    "voltage": "48V / 60V",
    "suspension": "Front:Hydraulic Telescopic,Rear:Double Shocker with Dual Tube Technology",
    "mileage": "80-90 km/charge",
    "ground_clearance": "160 mm",
    "icat": "Yes",
    "floor_mat": "Design Hard Mat",
    "top_speed": "25 kmph",
    "wheel": "Aluminium Alloy",
    "headlight": "LED with DRL",
    "backlight": "LED Winkers",
    "brake_lever": "Aluminium Alloy",
    "battery_warranty": "3 Years (Li-ion)"

}
```

<br>

#  Invoices Controller
##  Add new Invoices into the Database.
    
**Endpoint URL:** `/api/v1/invoices/addNew`
  
**HTTP Method:** POST
  
**Description:** Add new Invoices into the Database.
  
**Request Parameters:**
- Request Body
  
**Request Body:**
The request body for a POST request to add new invoices into the database. Should be in JSON format and include the following fields:
- `amc_items`(list {JSON}): The list of services that are covered by  AMC. 
- `chassis_num`(string) : The chassis number of the concerned vehicle.
- `date_of_booking` (string): The date on which the vehicle is serviced.
- `last_service_date` (string): The date on which the vehicle was last serviced.
- `last_service_km` (int): The distance covered by the vehicle till the last servicing.
- `services` (JSON): 
        - `name`(string): Service done on the vehicle. 
        - `price`(int): Price for the particular service.
        - `type`(string): If the service is covered under AMC or Warranty. If not covered either then the value returned is "N/A".
- `total_cost` (int): Total cost of the servicing.
- `warranty_items` (list {JSON}): The list of items that are covered by Warranty.
- `workshop_id` (string): The workshop id of the workshop in which the vehicle is taken to be serviced.
  
**Response:**
- Status Code: 200 OK
- Response Body: JSON.
  
**Response Body:**
The response body includes the following fields:
- `invoice_id` : The invoice ID generated for the invoice that is generated and added to the Database based on the request.
  
**Example Request:**
  
```http
POST /api/v1/invoices/addNew
Authorization: Bearer Token
Content-Type: application/json
{
    "amc_items": [],
    "chassis_num": "CHVH007",
    "date_of_booking": "2023-09-18",
    "last_service_date": "2023-09-18",
    "last_service_km": "701",
    "services": [
        {
            "name": "Speedometer",
            "price": 699,
            "type": "N/A"
        }
    ],
    "total_cost": 699,
    "warranty_items": [],
    "workshop_id": "workshop02"
}
```
  
**Example Response:**
```http
HTTP/1.1 200 OK
Content-Type: application/json
{
    "invoice_id": "00006202309280002"
}
```
<br>
  
##  Get all the invoices that have been generated.
  
**Endpoint URL:** `/api/v1/invoices/allinvoices`
  
**HTTP Method:** GET
  
**Description:** Get all the invoices that have been generated.
  
**Request Parameters:**
- No request parameter required.
  
  
**Response:**
- Status Code: 200 OK
- Response Body: List of JSON objects.
  
**Response Body:**
The response body includes the following fields:
- `bill_number`(string) : The bill number generated for the particular invoice. 
- `chassis_Num`(string) : The chassis number of the concerned vehicle.
- `workshop_id`(string) : The workshop id of the workshop in which the vehicle is taken to be serviced.
- `date_of_booking`(string) : The date on which the vehicle is serviced.
- `services` (list {JSON}): 
        - `name`(string): Service done on the vehicle. 
        - `price`(int): Price for the particular service
        - `type`(string): If the service is covered under AMC or Warranty. If not covered either then the value returned is "N/A".
- `total_cost`(int) : Total cost for the services.
- `distance_Travelled`(int) : Distance covered by the vehicle till the date of service.
  
**Example Request:**
```http
GET /api/v1/invoices/allinvoices
Content-Type: application/json
```
  
**Example Response:**
```http
HTTP/1.1 200 OK
Content-Type: application/json
[
    {
        "bill_number": "00006202309180004",
        "chassisNum": "CHVH007",
        "workshop_id": "workshop02",
        "date_of_booking": "2023-09-18",
        "services": [
            {
                "name": "Speedometer",
                "price": 699,
                "type": "N/A"
            }
        ],
        "total_cost": 699.0,
        "distanceTravelled": 701
    },
    {
        "bill_number": "00302202309180005",
        "chassisNum": "CHVH007",
        "workshop_id": "workshop04",
        "date_of_booking": "2023-09-18",
        "services": [
            {
                "name": "Speedometer",
                "price": 699,
                "type": "N/A"
            },
            {
                "name": "Handle Bar",
                "price": 0,
                "type": "AMC"
            }
        ],
        "total_cost": 699.0,
        "distanceTravelled": 702
    }
]
  
```
<br>
  
##  Get the generated invoice for a particular vehicle.
    
**Endpoint URL:** `/api/v1/invoices/{chassisNum}`
  
**HTTP Method:** GET
  
**Description:** Get the generated invoice for a particular vehicle.
  
**Request Parameters:**
- `chassisNum`  (path parameter): The chassis number of the concerned vehicle.
  
**Response:**
- Status Code: 200 OK
- Response Body: List of JSON objects.
  
**Response Body:**
The response body includes the following fields:
  - `bill_number`(string) : The bill number generated for the particular invoice. 
- `date_of_booking`(string) : The date on which the vehicle is serviced.
- `services` (list {JSON}): 
        - `name`(string): Service done on the vehicle. 
        - `price`(int): Price for the particular service.
        - `type`(string): If the service is covered under AMC or Warranty. If not covered either then the value returned is "N/A".
- `total_cost`(int) : Total cost for the services.
- `workshop_id`(string) : The workshop id of the workshop in which the vehicle is taken to be serviced.
- `distance_Travelled`(int) : Distance covered by the vehicle till the date of service.
  
**Example Request:**
```http
GET /api/v1/invoices/CHVH007
Content-Type: application/json
```
  
**Example Response:**
```http
HTTP/1.1 200 OK
Content-Type: application/json
[
    {
        "bill_number": "00302202309220001",
        "date_of_booking": "2023-09-23",
        "services": [
            {
                "name": "Speedometer",
                "price": 699,
                "type": "N/A"
            },
            {
                "name": "Handle Bar",
                "price": 319,
                "type": "N/A"
            },
            {
                "name": "Seat Rest Cover",
                "price": 119,
                "type": "N/A"
            },
            {
                "name": "Side stand",
                "price": 85,
                "type": "N/A"
            }
        ],
        "total_cost": 1222.0,
        "workshop_id": "workshop04",
        "distance_travelled": 901
    }
]
  
```
<br>

#  Parts Controller
##  Get the details of all the scopes of services available.
  
**Endpoint URL:** `/api/v1/parts/allParts`
  
**HTTP Method:** GET
  
**Description:** Get the details of all the services available.
  
**Request Parameters:**
- No request parameter required.
  
  
**Response:**
- Status Code: 200 OK
- Response Body: List of JSON objects.
  
**Response Body:**
The response body includes the following fields:
- `id` (int): ID for the part/service.
- `partCode` (string): A specific code for that particular part.
- `itemName` (string): Name of the part.
- `price` (int): Price of that particular part.
- `hsn` (int): HSN code of that part.
- `tax` (int): Tax category.
  
**Example Request:**
  
```http
GET /api/v1/parts/allParts
Content-Type: application/json
```
  
**Example Response:**
```http
HTTP/1.1 200 OK
Content-Type: application/json
  
[
    {
        "id": 1,
        "partCode": "FJ-SP1-EL-03-S",
        "itemName": "Speedometer",
        "price": 699.0,
        "hsn": "902920",
        "tax": "18.0"
    },
    {
        "id": 2,
        "partCode": "FJ-SP1-EL-07-S",
        "itemName": "Wire Harness",
        "price": 815.0,
        "hsn": "16030010",
        "tax": "12.0"
    },
    {
        "id": 3,
        "partCode": "FJ-SP1-M-007-S",
        "itemName": "Rear Suspension Set",
        "price": 659.0,
        "hsn": "87088020",
        "tax": ""
    }
]
```
<br>
  
#  Vehicle Details Controller
##  Get the details of a particular vehicle.
  
**Endpoint URL:** `/api/v1/vehicle/{chassisNum}`
  
**HTTP Method:** GET
  
**Description:** Get the details of a particular vehicle by giving the Chassis number of the vehicle as the Parameter..
  
**Request Parameters:**
- `chassisNum`  (path parameter): The chassis number of the concerned vehicle.
  
**Response:**
- Status Code: 200 OK
- Response Body: JSON.
  
**Response Body:**
The response body includes the following fields:
- `chassis_num` (string): The chassis number of the concerned vehicle.
- `phone_num` (int): The Phone number of the owner.
- `owner` (string): The owner of the vehicle.
- `reg_date` (string): The day on which the vehicle was registered.
- `warranty_start` (string): Warranty start date.
- `warranty_end` (string): Warranty end date.
- `amc_start_date` (string): AMC start date.
- `amc_end_date` (string): AMC end date. 
- `last_service_date` (string): The date on which the vehicle was last serviced.
- `last_service_km` (int): The distance covered by the vehicle on the last date of servce.
- `basic_details_id` (string): An ID generated for each car.
- `make` (string): Name of the company that made the vehicle. 
- `model` (string): Name of the model.
- `fuel_type` (string): The fuel type used. 
- `amc_type` (string): Type of AMC. 
  
**Example Request:**
```http
GET /api/v1/vehicle/CHVH001
Content-Type: application/json
```
  
**Example Response:**
```http
HTTP/1.1 200 OK
Content-Type: application/json
{
    "chassis_num": "CHVH001",
    "phone_num": "7364237649",
    "owner": "Fujiyama",
    "reg_date": "2022-03-22",
    "warranty_start": "2022-03-22",
    "warranty_end": "2023-03-22",
    "amc_start_date": "2023-03-22",
    "amc_end_date": "2024-03-22",
    "last_service_date": "2023-09-14",
    "last_service_km": 8000,
    "basic_details_id": "7e9dd8ae-40e9-11ee-831d-6045bdc60669",
    "make": "Fujiyama",
    "model": "Spectra",
    "fuel_type": "Electric(156 KWH)",
    "amc_type": "basic"
}
```
<br>

# Warranty Availability Controller
## Check if a particular part/scope is covered by Warranty

**Endpoint URL:** `/api/v1/warranty-availability/availability`

**HTTP Method:** GET

**Description:** Check if a particular part is covered by Warranty.

**Request Parameters:**
- `chassis_num` (query parameter, string, required): The chassis_num of the concerned vehicle.
- `scope` (query parameter, string, required): The concerened part/scope for which the warranty-availability is to be checked.


**Response:**
- Status Code: 200 OK
- Response Body: JSON.

**Response Body:**
The response body includes the following fields:
- `available` (string): The number of times the concerned part/scope can still be repaired for free under Warranty.
- `total` (string): The number of times the concerned part/scope can be repaired(in total) for free under Warranty.

**Example Request:**

```http
GET /api/v1/warranty-availability/availability?chassis_num=CHVH002&scope=Ignition%20Lock
```

**Example Response:**
```http
HTTP/1.1 200 OK
Content-Type: application/json
{
    "available": 1,
    "total": 2
}
```
<br>

## Get the list of all scopes covered by Warranty for the concerned vehicle

**Endpoint URL:** `/api/v1/warranty-availability/{chassisNum}`

**HTTP Method:** GET

**Description:** Get the list of all scopes covered by Warranty for the concerned vehicle.

**Request Parameters:**
- `chassisNum` (path parameter): The chassis number of the concerned vehicle.

**Response:**
- Status Code: 200 OK
- Response Body: List of JSON objects.

**Response Body:**
Each item of the response body includes the following fields:
- `scopeOfWork` (string): The name of the scope covered by the Warranty.
- `details` (string): Details about the scope.
- `frequency` (int): Total number of times the concerned scope can be repaired under Warranty.

**Example Request:**

```http
GET /api/v1/warranty-availability/CHVH001
```

**Example Response:**
```http
HTTP/1.1 200 OK
Content-Type: application/json
[
    {
        "scopeOfWork": "Ignition Lock",
        "details": "Change ignition(in total lifetime)",
        "frequency": 2
    },
    {
        "scopeOfWork": "Rear Fender",
        "details": "Change Rear Fender (in total lifetime)",
        "frequency": 1
    },
]
```
<br>

# WarrantyScopes Controller
## Get the list of all scopes covered under "Warranty".

**Endpoint URL:** `/api/v1/warranty/warrantyScopes`

**HTTP Method:** GET

**Description:** Get the list of all scopes covered under "Warranty".

**Response:**
- Status Code: 200 OK
- Response Body: JSON.

**Response Body:**
The response body includes the following fields:
- `id` (int): The id of the warrantyScopes.
- `warrantyId` (int): The id of the type of warranty plan .
- `scopeOfWork` (string): The name of the scope covered by the Warranty .
- `details` (string): Details about the scope.
- `frequency` (int): Total number of times the concerned scope can be repaired under "Warranty.

**Example Request:**

```http
GET /api/v1/warranty/warrantyScopes
```

**Example Response:**
```http
HTTP/1.1 200 OK
Content-Type: application/json
{
    "id": 1,
    "warrantyId": 1,
    "scopeOfWork": "Ignition Lock",
    "details": "Change ignition(in total lifetime)",
    "frequency": 2
}
```
<br>

