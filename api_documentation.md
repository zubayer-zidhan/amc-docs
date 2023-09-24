- [Authentication Controller](#authentication-controller)
  - [Register new users](#register-new-users)
  - [Authenticate the existing users](#authenticate-the-existing-users)
- [Admin Controller](#admin-controller)
  - [Add a new vehicle](#add-a-new-vehicle)
  - [Add a new workshop](#add-a-new-workshop)
- [AMC Availability Controller](#amc-availability-controller)
  - [Check if a particular part/scope is covered by AMC](#check-if-a-particular-partscope-is-covered-by-amc)
  - [Get the list of all scopes covered by AMC for the concerned vehicle](#get-the-list-of-all-scopes-covered-by-amc-for-the-concerned-vehicle)
- [Automovill Homes Controller](#automovill-homes-controller)
  - [Get information about the automovill offices in concerned state](#get-information-about-the-automovill-offices-in-concerned-state)
  - [Get all homes for all states](#get-all-homes-for-all-states)
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
- `admin` (string, required): The role of the user.

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
- 

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

