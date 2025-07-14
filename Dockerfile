# Usa una imagen base con Python
FROM python:3.11-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia tu código al contenedor
COPY . /app

# Instala las dependencias desde requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto Flask (por defecto 5000)
EXPOSE 5000

# Comando para ejecutar la app con Gunicorn
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:5000"]
