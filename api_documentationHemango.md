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
- `services` (list {JSON}): 
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
- `invoice_id` : The invoice ID generated for each new invoice generated and added to the Database.
  
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
  
#  Parts Details Controller Controller
  
##  Get the details of all the services available.
  
  
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
  
  