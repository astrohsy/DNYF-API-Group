# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /src

COPY requirements.txt /src/requirements.txt
RUN pip3 install -r requirements.txt

COPY . /src/

CMD [ "python3", "-m", "uvicorn", "src.app:app", "--reload", "--host=0.0.0.0"]
