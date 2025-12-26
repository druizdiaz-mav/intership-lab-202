FROM python:3.11-slim

# Variables de entorno para Python en Docker
# PYTHONDONTWRITEBYTECODE: Evita generar archivos .pyc (basura en el contenedor)
# PYTHONUNBUFFERED: Fuerza a que los logs salgan directo a la consola (vital para debug)
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# INSTALACIÓN DE DEPENDENCIAS
COPY requirements.txt .

# Instalo las dependencias.
# Primero actualizo el pip y luego instala las dependencias de requirements.txt
RUN pip install --no-cache-dir --upgrade pip && \ 
    pip install --no-cache-dir -r requirements.txt

# Copio el resto del código fuente
COPY . .

# Arranque
# --reload se quita en producción.
CMD ["uvicorn", "app.api.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]