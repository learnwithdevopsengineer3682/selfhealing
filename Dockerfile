# Dockerfile

FROM python:3.9-slim
WORKDIR /app
COPY app.py .
CMD [ "PYTHON", "app.py" ]