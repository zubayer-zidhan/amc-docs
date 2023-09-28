# AMC Scopes Controller

## The AmcScopesService is a service interface in the Automovill Microservices application responsible for managing and retrieving data related to AMC (Annual Maintenance Contract) scopes of work. It provides methods to fetch information about AMC scopes.

**Endpoint URL:** `/api/v1/amc/amcScopes`

**HTTP Method:** GET

**Description:** The AmcScopesService is designed to provide access to AMC scopes of work data. It allows clients to retrieve a list of AMC scopes based on various criteria..

**Response:**

- Status Code: 200 OK
- Response Body: JSON.

**Example Request:**

```http
GET /api/v1//api/v1/amc/details
```

**Response Body:**
The response body includes the following fields:
- id (integer): The unique identifier for the AMC scope.
- amcId (integer): The identifier of the associated Annual Maintenance Contract.
- scopeOfWork (string): A description of the scope of work.
- details (string): Additional details about the scope of work.
- frequency (integer): The frequency at which the scope of work is performed.

**Example Response:**

```http
HTTP/1.1 200 OK
Content-Type: application/json
{
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
}
```

<br>
