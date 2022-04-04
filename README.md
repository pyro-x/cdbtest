# a carto db test 
This project creates a small python-based backend server that gives geo content and payment data to a very nice frontend that knows how to render it.

Backend is based on python with fastapi , asyncpg as the db connector and fastapi_asyncpg module as an effective bridge between.
The python server talks to a postgis database that contains all the needed tables.

Initial assumptions
* There are two tables at the db from the two csv files one for the postal codes and the other one with the payment data
* There are also some postgis cities layer (postal codes are rendered on top )
* Frontend knows how to draw a GEO JSON layer

## How to run the project via Docker
In the project a docker compose yaml is provided to run it just..

```bash

# build the image
$ docker-compose build

# once built you can start the images
# backend server will be available at http://localhost:8000 and api doc at 
$ docker-compose up 

# once you get bored you can just bring everything down with 
$ docker-compose down 
```


