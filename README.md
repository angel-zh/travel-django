# Travel Booking Django App

## OVERVIEW

This travel booking app handles the booking of travellers and accommodation for anyone looking to make their travel plans as easy and convenient as possible.

## INSTRUCTIONS
This project requires the following:
- `pipenv install`
- `pipenv shell`
- `pipenv install django`
- `pipenv install psycopg2-binary`
- `pipenv install djangorestframework`

## ROUTES
`Traveller` is joined to `Hotel` and `Flight` via `Booking` in a many-to-many relationship.
### Hotel:
| Endpoint      | HTTP Verb | Description |
|---------------|-----------|-------------|
| trip/hotels/        | get       | index all hotels  |
| trip/hotels/       | post      | create a hotel      |
| trip/hotels/:pk/   | get       | show a hotel      |
| trip/hotels/:pk/   | patch     | update a hotel    |
| trip/hotels/:pk/   | delete    | delete a hotel    |

### Flight: 
| Endpoint          | HTTP Verb | Description |
|-------------------|-----------|-------------|
| trip/flights/       | get       | index all flights  |
| trip/flights/       | post      | create a flight      |
| trip/flights/:pk/   | get       | show a flight      |
| trip/flights/:pk/   | patch     | update a flight    |
| trip/flights/:pk/   | delete    | delete a flight    |

### Traveller: 
| Endpoint          | HTTP Verb | Description |
|-------------------|-----------|-------------|
| trip/travellers/       | get       | index all travellers  |
| trip/travellers/       | post      | create a traveller      |
| trip/travellers/:pk/   | get       | show a traveller      |
| trip/travellers/:pk/   | patch     | update a traveller    |
| trip/travellers/:pk/   | delete    | delete a traveller    |

### Booking: 
| Endpoint          | HTTP Verb | Description |
|-------------------|-----------|-------------|
| trip/bookings/       | get       | index all bookings  |
| trip/bookings/       | post      | create a booking      |
| trip/bookings/:pk/   | get       | show a booking      |
| trip/bookings/:pk/   | patch     | update a booking    |
| trip/bookings/:pk/   | delete    | delete a booking    |
