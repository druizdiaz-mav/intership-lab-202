# Usamos una imagen ligera de Python
FROM python:3.9-slim

# Directorio de trabajo dentro del contenedor
WORKDIR /app

RUN pip install --no-cache-dir fastapi uvicorn

# Copiamos el código fuente
COPY main.py .

# Comando de ejecución
CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]