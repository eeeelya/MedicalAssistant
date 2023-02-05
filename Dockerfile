FROM python:3.10-alpine

RUN apk update && apk add python3-dev \
                          gcc \
                          libc-dev \
                          libffi-dev

WORKDIR /app

ENV PYTHONUNBUFFERED=1 \
    PYTHONPATH="."

COPY ./medical_assistant /app

RUN python -m pip install --upgrade pip pipenv
RUN pipenv install --system --deploy

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
