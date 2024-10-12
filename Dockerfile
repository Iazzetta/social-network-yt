FROM python:3.10-buster

RUN pip install poetry

COPY . .

RUN poetry install

EXPOSE 80

ENTRYPOINT ["poetry", "run", "task", "prod"]