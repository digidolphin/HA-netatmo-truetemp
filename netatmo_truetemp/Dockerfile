ARG BUILD_FROM
FROM ${BUILD_FROM}

# Install Python + tooling (Alpine base)
RUN apk add --no-cache python3 py3-pip py3-virtualenv bash

# Create venv and install deps
RUN python3 -m venv /opt/venv \
  && /opt/venv/bin/pip install --no-cache-dir --upgrade pip setuptools wheel \
  && /opt/venv/bin/pip install --no-cache-dir fastapi uvicorn py-netatmo-truetemp-cli

# App code
COPY app /app

# Ensure venv is used by default
ENV PATH="/opt/venv/bin:${PATH}"

CMD ["python3", "/app/start.py"]
