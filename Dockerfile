# FROM python:3.9

# WORKDIR /app

# COPY ./requirements.txt /app/requirements.txt

# RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# COPY ./app /app/app

# # Use uvicorn as the ASGI server
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

# # Alternatively, for potentially better production stability, use gunicorn with uvicorn workers:
# # RUN pip install gunicorn
# # CMD ["gunicorn", "app.main:app", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8000"]
FROM python:3.9-slim-buster

WORKDIR /app

RUN pip install --no-cache-dir uvicorn fastapi

COPY ./app /app/app

CMD ["uvicorn", "app.app.main:app", "--host", "0.0.0.0", "--port", "$PORT"]