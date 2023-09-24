- [Admin Controller](#admin-controller)
  - [Add a new vehicle](#add-a-new-vehicle)
  - [Add a new workshop](#add-a-new-workshop)
- [AMC Availability Controller](#amc-availability-controller)
  - [Check if a particular part/scope is covered by AMC](#check-if-a-particular-partscope-is-covered-by-amc)
  - [Get the list of all scopes covered by AMC for the concerned vehicle](#get-the-list-of-all-scopes-covered-by-amc-for-the-concerned-vehicle)



# Admin Controller
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
Added Successfully
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
Added Successfully
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
GET api/v1/amc-availability/availability?chassis_num=CHVH008&scope=Handle%20Bar
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