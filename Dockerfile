FROM python:3.9.5-slim
ENV PYTHONUNBUFFERED=1

RUN useradd -ms /bin/bash tarantino
WORKDIR /app

COPY ["Pipfile", "Pipfile.lock", "movies_admin", "/app/"]
EXPOSE 8000

ENV PIPENV_VENV_IN_PROJECT=1
RUN pip install pipenv && pipenv install --deploy --system --dev

RUN chown -R tarantino:tarantino /app/
USER tarantino
