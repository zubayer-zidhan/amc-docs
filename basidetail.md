# BasicDetailsService Controller

## The BasicDetailsService allows clients to access basic vehicle details, including make, model, fuel type, and various other attributes. It provides flexibility to retrieve details for all vehicles or a specific vehicle based on its unique identifier..

**Endpoint URL:** `/api/v1//api/v1/basic/allDetails`

**HTTP Method:** GET

**Description:** This endpoint allows clients to retrieve a list of all basic vehicle details..

**Request Parameters:**
Request Parameters: None

**Response:**

- Status Code: 200 OK
- Response Body: JSON.

**Response Body:**
The response body includes the following fields:

- id (string): The unique identifier of the vehicle.
- make (string): The make or manufacturer of the vehicle.
- model (string): The model of the vehicle.
- fuelType (string): The type of fuel the vehicle uses.
- ratedPower (string): The rated power of the vehicle's engine.
- peakPower (string): The peak power of the vehicle's engine.
- seatHeight (string): The seat height of the vehicle.
- loadingCapacity (string): The loading capacity of the vehicle.
- speedometer (string): Information about the vehicle's speedometer.
- batteryType (string): The type of battery used in the vehicle.
- controller (string): Information about the vehicle's controller.
- brakeSystem (string): Information about the vehicle's brake system.
- dimensions (string): The dimensions of the vehicle.
- tyre (string): Information about the vehicle's tires.
- chargingTime (string): The charging time for the vehicle's battery.
- chargerSpecs (string): Specifications of the vehicle's charger.
- voltage (string): The voltage used by the vehicle.
- suspension (string): Information about the vehicle's suspension.
- mileage (string): The mileage of the vehicle.
- groundClearance (string): The ground clearance of the vehicle.
- icat (string): Information about the vehicle's ICAT compliance.
- floorMat (string): Information about the vehicle's floor mat.
- topSpeed (string): The top speed of the vehicle.
- wheel (string): Information about the vehicle's wheel.
- headlight (string): Information about the vehicle's headlight.
- backlight (string): Information about the vehicle's backlight.
- brakeLever (string): Information about the vehicle's brake lever.
- batteryWarranty (string): Warranty information for the vehicle's battery..

**Example Request:**

```http
GET /api/v1//api/v1/basic/allDetails
```

**Example Response:**

```http
HTTP/1.1 200 OK
Content-Type: application/json
{
    [
    {
        "id": "7e9dd8ae-40e9-11ee-831d-6045bdc60669",
        "make": "Fujiyama",
        "model": "Spectra",
        "fuelType": "Electric(156 KWH)",
        "rated_power": "250 Watt,BLDC Motor",
        "peak_power": "3700 Watt",
        "seat_height": "740 mm",
        "loading_capacity": "150 kg",
        "speedometer": "LCD",
        "battery_type": "1.56 KWH (Li-ion)(Detachable Battery)",
        "controller": "E-ABS",
        "brake_system": "Drum Brakes(Both)",
        "dimensions": "L-1730mm | W-690mm | H-1280mm",
        "tyre": "3.0 - 10 Tubeless(Both)",
        "charging_time": "4 -5 hrs",
        "charger_specs": "Micro-charger with Auto Cut",
        "voltage": "48V / 60V",
        "suspension": "Front:Hydraulic Telescopic,Rear:Double Shocker with Dual Tube Technology",
        "mileage": "80-90 km/charge",
        "ground_clearance": "160 mm",
        "icat": "Yes",
        "floor_mat": "Design Hard Mat",
        "top_speed": "25 kmph",
        "wheel": "Aluminium Alloy",
        "headlight": "LED with DRL",
        "backlight": "LED Winkers",
        "brake_lever": "Aluminium Alloy",
        "battery_warranty": "3 Years (Li-ion)"
    }
]
}
```

## The BasicDetailsService allows clients to access basic vehicle details, including make, model, fuel type, and various other attributes. It provides flexibility to retrieve details for all vehicles or a specific vehicle based on its unique identifier..

**Endpoint URL:** `/api/v1/basic/{id}`

**HTTP Method:** GET

**Description:** This endpoint allows clients to retrieve basic vehicle details for a specific vehicle based on its unique identifier (id).

**Request Parameters:**

- id (string): The unique identifier of the vehicle

**Response:**

- Status Code: 200 OK
- Response Body: JSON.

**Request Body :** - None

**Response Body:**
The response body includes the following fields:

- id (string): The unique identifier of the vehicle.
- make (string): The make or manufacturer of the vehicle.
- model (string): The model of the vehicle.
- fuelType (string): The type of fuel the vehicle uses.
- ratedPower (string): The rated power of the vehicle's engine.
- peakPower (string): The peak power of the vehicle's engine.
- seatHeight (string): The seat height of the vehicle.
- loadingCapacity (string): The loading capacity of the vehicle.
- speedometer (string): Information about the vehicle's speedometer.
- batteryType (string): The type of battery used in the vehicle.
- controller (string): Information about the vehicle's controller.
- brakeSystem (string): Information about the vehicle's brake system.
- dimensions (string): The dimensions of the vehicle.
- tyre (string): Information about the vehicle's tires.
- chargingTime (string): The charging time for the vehicle's battery.
- chargerSpecs (string): Specifications of the vehicle's charger.
- voltage (string): The voltage used by the vehicle.
- suspension (string): Information about the vehicle's suspension.
- mileage (string): The mileage of the vehicle.
- groundClearance (string): The ground clearance of the vehicle.
- icat (string): Information about the vehicle's ICAT compliance.
- floorMat (string): Information about the vehicle's floor mat.
- topSpeed (string): The top speed of the vehicle.
- wheel (string): Information about the vehicle's wheel.
- headlight (string): Information about the vehicle's headlight.
- backlight (string): Information about the vehicle's backlight.
- brakeLever (string): Information about the vehicle's brake lever.
- batteryWarranty (string): Warranty information for the vehicle's battery..

**Example Request:**

```http
GET api/v1/basic/7e9dd8ae-40e9-11ee-831d-6045bdc60669
```

**Example Response:**

```http
HTTP/1.1 200 OK
Content-Type: application/json
{
    "id": "7e9dd8ae-40e9-11ee-831d-6045bdc60669",
    "make": "Fujiyama",
    "model": "Spectra",
    "fuelType": "Electric(156 KWH)",
    "rated_power": "250 Watt,BLDC Motor",
    "peak_power": "3700 Watt",
    "seat_height": "740 mm",
    "loading_capacity": "150 kg",
    "speedometer": "LCD",
    "battery_type": "1.56 KWH (Li-ion)(Detachable Battery)",
    "controller": "E-ABS",
    "brake_system": "Drum Brakes(Both)",
    "dimensions": "L-1730mm | W-690mm | H-1280mm",
    "tyre": "3.0 - 10 Tubeless(Both)",
    "charging_time": "4 -5 hrs",
    "charger_specs": "Micro-charger with Auto Cut",
    "voltage": "48V / 60V",
    "suspension": "Front:Hydraulic Telescopic,Rear:Double Shocker with Dual Tube Technology",
    "mileage": "80-90 km/charge",
    "ground_clearance": "160 mm",
    "icat": "Yes",
    "floor_mat": "Design Hard Mat",
    "top_speed": "25 kmph",
    "wheel": "Aluminium Alloy",
    "headlight": "LED with DRL",
    "backlight": "LED Winkers",
    "brake_lever": "Aluminium Alloy",
    "battery_warranty": "3 Years (Li-ion)"

}
```

<br>
