# Import the necessary libraries
import os

# Function to create an API documentation entry
def create_api_entry():
    parent_controller = input("Parent Controller (e.g. Admin, Users): " )
    title = input("Enter a title: ")
    endpoint_url = input("Enter the endpoint URL(after /api/v1/): ")
    http_method = input("Enter the HTTP method (GET, POST): ")
    description = input("Enter a description for the endpoint: ")
    
    # Generate the Markdown entry
    markdown_entry = f"""# { parent_controller } Controller
## { title }

**Endpoint URL:** `/api/v1/{ endpoint_url }`

**HTTP Method:** { http_method }

**Description:** { description }.

**Request Parameters:**
- `` (path parameter): .

**Request Body:**
The request body for a POST request to { title.lower() } should be in JSON format and include the following fields:\n
- `` (string, required): The .

**Response:**
- Status Code: 200 OK
- Response Body: JSON.

**Response Body:**
The response body includes the following fields:
- `` (string): The .

**Example Request:**\n
```http
{http_method} /api/v1/{ endpoint_url }
Content-Type: application/json
{{
    
}}
```

**Example Response:**
```http
HTTP/1.1 200 OK
Content-Type: application/json
{{
    
}}
```
<br>

"""

    # Append the entry to the documentation file
    with open("api_documentation.md", "a") as file:
        file.write(markdown_entry)

# Main script
if __name__ == "__main__":
    create_api_entry()

print("API documentation created successfully.")
