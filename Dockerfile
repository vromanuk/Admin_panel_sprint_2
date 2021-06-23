FROM python:3.9.5-slim
ENV PYTHONUNBUFFERED=1

RUN useradd -ms /bin/bash tarantino
WORKDIR /app

COPY --chown=tarantino:tarantino ["Pipfile", "Pipfile.lock", "/app/"]
EXPOSE 8000

ENV PIPENV_VENV_IN_PROJECT=1
RUN pip install pipenv && pipenv install --deploy --system --dev

COPY --chown=tarantino:tarantino ["movies_admin/", "/app/"]
USER tarantino
