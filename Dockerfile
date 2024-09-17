FROM --platform=linux/amd64 python:3.12-slim

RUN mkdir -p /app

WORKDIR /app

COPY Pipfile Pipfile.lock /app/

RUN pip install -U pipenv

RUN pipenv install --deploy

COPY . /app

EXPOSE 5000

CMD ["pipenv", "run", "gunicorn", "--bind", "0.0.0.0:5000", "run:gunicorn_app"]