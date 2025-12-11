# Usamos una imagen ligera de Python
FROM python:3.10-slim

# Directorio de trabajo dentro del contenedor
WORKDIR /code

RUN pip install --no-cache-dir fastapi uvicorn

# Copiamos el código fuente
COPY ./app /code/app

# Comando de ejecución
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]