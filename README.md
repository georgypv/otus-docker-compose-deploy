# otus-docker-compose-deploy

This repository contains a sample app containerized via docker-compose.
The structure of the app consists of a sample Panel dashboard, a Postgres database with some randomly-generated data and (optionally) a pgadmin4 instance. 

In order to run the app (dashboad+DB) locally, use command:
`docker-compose up`
You should find a working interactive dashboard at port 5555.


Additionally, if you want a pgadmin instance running, modify the command above in the following fashion:
`docker-compose --profile debug up`
In result, you get a local instance of pgadmin4 at port 8090. In order to connect to the `POSTGRES_DB` database, use following `host:port`: 
`db:5432`

### Credentials
Credenials such as POSTGRES_USER, POSTGRES_PASSWORD etc. are stored in an .env file which you must have on a machine where you want to run the application. 
