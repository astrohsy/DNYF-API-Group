# DFNY Group API

## Start up local API and DB

```bash
docker-compose -f docker-compose.yml up --build
```

## To only use DB with Docker

```bash
docker-compose -f docker-compose.yml up -d --build db
```

To start the API using a local Python environment:

```
uvicorn src.app:app --reload
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

## Without Docker Compose (for reference)

```bash
docker volume create mysql
docker volume create mysql_config
docker network create dnyfnet
```

```bash
docker build --tag dnyf-group-api .
```

```bash
docker run --name dnyf-group-api \
    -p 8000:8000 \
    --network dnyfnet \
    -d dnyf-group-api
```

```bash
docker run --rm --name dnyf-group-db \
    --network dnyfnet \
    -v mysql:/var/lib/mysql \
    -v mysql_config:/etc/mysql \
    -e MYSQL_ROOT_PASSWORD=dbuser \
    -e MYSQL_USER=dbuser \
    -e MYSQL_PASSWORD=dbuser \
    -e MYSQL_DATABASE=dnyf-group-db \
    -p 3306:3306 \
    -d mysql:8.0
```
