FROM python:3.10-buster

COPY . .

RUN pip install poetry

RUN poetry install

EXPOSE 80

CMD ["poetry", "run", "task", "prod"]