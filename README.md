# Flight Project

### writen in django 

## Startup

##### Install dependencies
```shell
uv sync
```
> uv automatically creates a virtual environment

##### Activate the venv

- linux, mac
```shell
source .venv/bin/activate
```

- windows:
```shell
.venv\Scripts\activate
```

##### SetUp the [.env](.env) file based on [.env.example](.env.example)

you can use ["*"] for ALLOWED_HOSTS

##### SetUp database

> since the project uses SQLite, no extra configuration need

```shell
python manage.py migrate
```

##### Create sample data

```shell
python manage.py setup_data
```

##### Start Server on development

```shell
python manage.py runserver
```

## StartUp Using Docker

##### SetUp the [.env](.env) file based on [.env.example](.env.example)

you can use ["*"] for ALLOWED_HOSTS

#### Run container
```shell
docker compose up -d
```

##### Create sample data

```shell
docker exec -it flight bash
python manage.py setup_data
```

## Run Tests

```shell
pytest -v
```

## Note:
This app is not production-ready and it only purpose is to show my coding style

Since we use ORM for this project, there wasn't many benefits in using **Repository** layer

Because project is too small and there is no business logic (just normal query), we have no **Service** layer

The most used pattern in django is **"Fat model, Thin View"** and most of the time, serializer can act like service layer and keep the business logics, but having service layer in django project is normal too.

Because of the small scale of project, we used **static_root** instead of object storages like MinIO
