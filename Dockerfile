# Usa una imagen base con Python
FROM python:3.11-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia tu código al contenedor
COPY . /app

# Instala las dependencias
RUN pip install --no-cache-dir flask psycopg2-binary

# Expone el puerto Flask (por defecto 5000)
EXPOSE 5000

# Comando para ejecutar tu app
CMD ["python", "app.py"]
