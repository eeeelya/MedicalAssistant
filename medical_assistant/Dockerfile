FROM python:3.10

WORKDIR /usr/src/app/

ENV PYTHONUNBUFFERED=1 \
    PYTHONPATH="."

RUN pip install pipenv

COPY Pipfile /usr/src/app/
COPY Pipfile.lock /usr/src/app/
RUN pipenv install --system --deploy

COPY . /usr/src/app/

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]