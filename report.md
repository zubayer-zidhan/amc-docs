# AMC Availability Microservice Documentation

## Overview

This documentation provides an overview of the AMC (Automobile Maintenance Contract) Availability Microservice, which is responsible for managing and retrieving information about AMC availability for different vehicles. This microservice is a part of the larger "Automovill Microservices" ecosystem.

## Table of Contents

- Introduction
- Controller
- API Endpoints

### 1.Introduction

The AMC Availability Microservice is designed to handle and manage information related to AMC availability for automobiles. It provides endpoints for retrieving AMC availability details, searching for availability by chassis number and scope of work, and getting detailed information for a specific chassis number.

### 2.Controller

The AmcAvailabilityController is responsible for handling HTTP requests and invoking the corresponding service methods:

```java
@CrossOrigin(value = "localhost:19000")
@RestController
@RequestMapping("api/v1/amc-availability")
public class AmcAvailabilityController {
    @Autowired
    AmcAvailabilityService amcAvailabilityService;

@GetMapping("/all")
public List<AmcAvailability> getAmcAvailabilityDetails(){
        return amcAvailabilityService.getAmcAvailabilityDetails();
    }
    @GetMapping("/availability")
    public ResponseEntity<ScopeResponse> getAvailability(
        @RequestParam("chassis_num") String chassis_num,
        @RequestParam("scope") String scope
    ) {
        return ResponseEntity.ok(amcAvailabilityService.getAvailability(chassis_num, scope));
    }
    @GetMapping("/{chassisNum}")
    public List<AmcAvailabilityDetails> getAmcDetailsByChassisNum(@PathVariable String chassisNum){
        return amcAvailabilityService.getAmcDetailsByChassisNum(chassisNum);
    }
}
```

### 3.API Endpoints

## The AMC Availability Microservice provides the following API endpoints:

### (a) Get All AMC Availability Details

-     HTTP Method: GET
-     Endpoint: /api/v1/amc-availability/all
- Description: Retrieves a list of all AMC availability details.
- Response: List of AmcAvailability objects

### (b) Get AMC Availability by Chassis Number and Scope

-      HTTP Method: GET
-      Endpoint: /api/v1/amc-availability/availability
- Description: Retrieves AMC availability based on chassis number and scope of work.
- Request Parameters:
  - chassis_num (String): Chassis number of the automobile.
  - scope (String): Scope of work.
- Response: ScopeResponse object containing availability details.

### (c) Get AMC Details by Chassis Number

-       HTTP Method: GET
-       Endpoint: /api/v1/amc-availability/{chassisNum}
- Description: Retrieves detailed AMC availability information for a specific chassis number.
- Path Parameter:
  - chassisNum (String): Chassis number of the automobile.
  - Response: List of AmcAvailabilityDetails objects.
