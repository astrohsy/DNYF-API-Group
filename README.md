# DFNY Group API

## Start up local API and DB

```bash
docker-compose -f docker-compose.yml up --build
```

## Debug in VSCode

First build and start the containers in debug mode:

```bash
docker-compose -f docker-compose.debug.yml up --build
```

Then in VSCode:
- Navigate to *Run and Debug*
- Select the *Python: Remote Attach* configuration
- Start debugging

## To start up API and DB separately (for reference)

```bash
docker network create dnyfnet
```

```bash
docker build --tag dnyf-group-api .
docker run -d -p 8000:8000 --network dnyfnet --name dnyf-group-api dnyf-group-api
```

```bash
docker run --name dnyf-group-db \
    --network dnyfnet \
    -e POSTGRES_PASSWORD=dbuser \
    -e POSTGRES_USER=dbuser \
    -e POSTGRES_DB=dnyf-group-db \
    -p 5432:5432 \
    -d postgres:14.5-alpine
```

To connect to Postgres from within the DB container:

```bash
psql -U dbuser -d dnyf-group-db
```
