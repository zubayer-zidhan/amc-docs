# API Documentation

## Admin Controller

### Get User Information

**Endpoint URL:** `/api/v1/`

**HTTP Method:** GET

**Description:** Retrieves information about a user.

**Request Parameters:**
- `{}` (path parameter): .

**Request Body:**
The request body for a POST request to create a new user should be in JSON format and include the following fields:
- `username` (string, required): The username of the new user.



**Response:**
- Status Code: 200 OK
- Response Body: JSON representation of the user.


**Response Body:**
The respnse body includes the following fields:
- `username` (string): The username of the new user.




**Example Request:**
```http
POST /api/v1/
Content-Type: application/json

{
    
}
```

**Example Response:**
```http
HTTP/1.1 200 OK
Content-Type: application/json
{
    
}
```