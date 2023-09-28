# AMC Scopes Controller

## Get Access to the AMC scopes table, which contains the blueprint for amc_availability table.

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
