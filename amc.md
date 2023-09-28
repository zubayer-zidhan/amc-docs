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
