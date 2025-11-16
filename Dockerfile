FROM python:3.12
WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV UV_PROJECT_ENVIRONMENT="/usr/local/"

COPY . .

RUN pip install uv

RUN uv sync --locked --no-dev

RUN chown -R www-data:www-data /app

USER www-data

EXPOSE 8000

CMD gunicorn --reload --bind 0.0.0.0:8000 --access-logfile - core.wsgi:application
