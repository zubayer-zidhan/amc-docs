# AMC Controller 

## The Amc Service is a service interface in the Automovill Microservices application responsible for managing and retrieving AMC (Annual Maintenance Contract) details. It provides methods to retrieve a list of all AMC details.

**Endpoint URL:** `/api/v1//api/v1/amc/details`

**HTTP Method:** GET

**Description:** This endpoint allows clients to retrieve a list of all AMC details..

**Request Parameters:**

- Request Parameters: None .

**Response:**

- Status Code: 200 OK
- Response Body: JSON.

**Response Body:**
The response body includes the following fields:

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
{


}
```

<br>
