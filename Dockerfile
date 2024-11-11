FROM python:3.10-slim

WORKDIR /api

COPY pyproject.toml poetry.lock* /api/

RUN pip install --no-cache-dir poetry

RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

COPY . /api

EXPOSE 8000

CMD ["fastapi", "run", "./api/main.py"]