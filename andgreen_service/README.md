Andgreen Service

# Table of Content

1. [ Description ](#description)
2. [ REST API ](#rest-api)
3. [ OpenAPI ](#openapi)
4. [ Local Development ](#local-development)

# Description

Service to manage customers, their products and consumption of products through readings using IoT devices. Consumption values are:

- ppm C02 water
- ppm C02 air
- water temperature

# REST API

## Customers

- GET /customers/
- POST /customers/
- GET /customers/{customerId}
- PUT /customers/{customerId}
- DELETE /customers/{customerId}

## Products

- GET /products/
- POST /products/
- GET /products/{productId}
- PUT /products/{productId}
- DELETE /products/{productId}

## Devices

- GET /products/{productId}/devices/
- POST /products/{productId}/devices/
- GET /products/{productId}/devices/{deviceId}
- PUT /products/{productId}/devices/{deviceId}
- DELETE /products/{productId}/devices/{deviceId}

## Readings

- GET /products/{productId}/devices/{deviceId}/readings
- POST /products/{productId}/devices/{deviceId}

## Service

- GET /health
- GET /version
- GET /restversion

## Users

- POST /users/register/
- GET /users/current/
- POST /users/token/

# OpenAPI

OpenAPI documentation can be found here:

- LOCAL: [ AndGreen Service OpenAPI LOCAL ](http://localhost:8000/api/schema/swagger-ui/#/)
- DEV: n/a
- TEST: n/a
- PROD: n/a

# Local Development

## Backend

0. Prerequisites: Python Version >= 3.11
1. Navigate into folder 'Backend'
2. Install needed modules with 'pip install -r requirements.txt'
3. Run 'python manage.py runserver'

All endpoints are protected, thus a valid bearer token is needed in the 'Authorization' header.
A valid token can only be obtained by registered users (/users/token/).

## Frontend

todo
