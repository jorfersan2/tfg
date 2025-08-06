# Usa la imagen oficial de Python (última versión estable)
FROM python:latest

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /api

# Copia todos los archivos necesarios al directorio /app del contenedor
COPY . .

# Instala las dependencias desde requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

#Puerto donde correrá Flask
EXPOSE 5000

# Abre un bash del contenedor
CMD ["bash"]

# Para que se ejecute directamente el script al iniciar el contenedor
#CMD ["python3", "api_flask.py"]

