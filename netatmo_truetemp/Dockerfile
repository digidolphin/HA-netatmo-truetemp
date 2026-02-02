ARG BUILD_FROM
FROM ${BUILD_FROM}

RUN python3 -m venv /opt/venv \
  && /opt/venv/bin/pip install --no-cache-dir --upgrade pip setuptools wheel \
  && /opt/venv/bin/pip install --no-cache-dir fastapi uvicorn py-netatmo-truetemp-cli

ENV PATH="/opt/venv/bin:${PATH}"

COPY app /app

CMD ["python3", "/app/start.py"]
