FROM python:3
ENV PYTHONUNBUFFERED=1

RUN useradd -ms /bin/bash tarantino
WORKDIR /app

RUN pip install pipenv
COPY Pipfile /app/
COPY Pipfile.lock /app/
RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --deploy --system --dev

COPY movies_admin /app/

RUN chown -R tarantino:tarantino /app/
USER tarantino

EXPOSE 8000
