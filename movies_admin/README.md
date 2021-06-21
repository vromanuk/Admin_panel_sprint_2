# Getting started

- Before running the application, you have to install [Docker](https://docs.docker.com/get-docker/)

## Local launch

- Create `.env` file in `the folder root` and set the environment variables.
- You should provide the following variables:
    - SECRET_KEY=your_secret_key
    - POSTGRES_USER=your_postgres_user
    - POSTGRES_PASSWORD=your_postgres_password
    - POSTGRES_DB=your_postgres_db_name
    - DB_PORT=5432
    - DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1
- Run `docker-compose up -d --build` from `the folder root`.
- Visit [localhost:8000](localhost:8000)
