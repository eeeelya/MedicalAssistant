FROM python:3.10-slim

RUN apt-get update && apt-get -y dist-upgrade
RUN apt install -y netcat ffmpeg libsm6 libxext6

COPY medical_assistant app/
WORKDIR app/

ENV PYTHONUNBUFFERED=1 \
    PYTHONPATH="."

RUN pip install --upgrade pipenv
RUN pipenv install --system --deploy
