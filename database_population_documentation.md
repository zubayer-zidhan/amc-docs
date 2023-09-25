# Database Population Documentation

This documentation explains how to populate various tables in the database using different methods.

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


