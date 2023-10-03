Andgreen Service 
# Table of Content
1. [ Description ](#description)
2. [ REST API ](#rest-api)
# Description
Service to manage customers, their products and consumption of products using IoT devices. Consumption values are:
- ppm C02 water
- ppm C02 air
- water temperature
# REST API
## Customers
- GET /customers
- GET /customers/{customerId}
## Products
- GET /products
- GET /products/{productId}
## Service
- GET /health
- GET /version
- GET /restversion