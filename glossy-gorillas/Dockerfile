FROM python:3.8-slim

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

ENV POETRY_VERSION 1.0.10

RUN mkdir /code
WORKDIR /code

# Install any needed packages
ADD poetry.lock pyproject.toml /code/
RUN pip install poetry==$POETRY_VERSION
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

ADD . /code
RUN chmod +x docker-entrypoint.sh
