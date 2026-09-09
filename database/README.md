# NER Logistics Database

## Project

AI-Based Smart Logistics and Accessibility Intelligence Platform for the North Eastern Region (NER)

## Database

* Database Name: `NER_Logistics_DB`
* DBMS: PostgreSQL
* Port: `5432`
* Schema: `public`

## Purpose

This database stores and organizes information required for the logistics and accessibility platform for the North Eastern Region.

It contains data related to:

* Locations
* Routes
* Weather
* Road conditions
* Disruptions
* Traffic
* Vehicles
* Facilities
* Public transport
* Accessibility
* Logistics and shipments
* Alerts
* Data sources
* Data quality

## Tables

The database contains 14 tables:

1. `locations`
2. `routes`
3. `weather`
4. `road_conditions`
5. `disruptions`
6. `traffic`
7. `vehicles`
8. `facilities`
9. `public_transport`
10. `accessibility`
11. `logistics`
12. `alerts`
13. `data_sources`
14. `data_quality`

## Database File

`NER_Logistics_DB.sql`

This SQL file contains the database structure and prototype data required to recreate the database.

## How to Restore the Database

1. Install PostgreSQL.
2. Create a database named `NER_Logistics_DB`.
3. Open the SQL file using pgAdmin Query Tool or PostgreSQL `psql`.
4. Execute the SQL file to create the tables and insert the prototype data.

## Backend Connection

The backend should connect to PostgreSQL using the following configuration:

```text
Host: localhost
Port: 5432
Database: NER_Logistics_DB
User: postgres
Password: <your-local-password>
```

The actual PostgreSQL password must NOT be stored in GitHub.

Use environment variables or a `.env` file for local credentials.

## Data Note

The current records are prototype/demo data created for development and testing.

They are not live government records.

The database structure is designed so that the prototype data can later be replaced or updated using government datasets, live APIs, GPS feeds, weather services, and other approved data sources.

## Team Usage

The backend team can use this database to:

* Retrieve route information
* Retrieve weather and road-condition information
* Track vehicles
* Access logistics and shipment information
* Retrieve accessibility scores
* Retrieve alerts and disruptions

The AI/ML team can later use relevant database data for route-risk prediction, accessibility analysis, ETA prediction, and route optimization.

## Important

Do not commit:

* PostgreSQL passwords
* `.env` files containing real credentials
* Private keys
* Local PostgreSQL data directories

The SQL file in this folder is intended to be shared through the team's GitHub repository.
