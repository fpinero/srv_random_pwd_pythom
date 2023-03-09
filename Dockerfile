# Imagen base
FROM python:3.9-slim-buster

# Creación de un usuario no-root
RUN adduser --disabled-password --gecos '' appuser

# Directorio de trabajo
WORKDIR /app

# Copia de los archivos requeridos
COPY secure_password.py requirements.txt ./

# Instalación de las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Configuración de logging
ENV PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app \
    LOG_LEVEL=INFO

# Ejecución del servidor
CMD ["python", "secure_password.py"]
