# Usa la imagen oficial de Python (última versión estable)
FROM python:latest

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia todos los archivos necesarios al directorio /app del contenedor
COPY . .

# Instala las dependencias desde requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Abre un bash del contenedor
CMD ["bash"]

# Para que se ejecute directamente el script al iniciar el contenedor
#CMD ["python3", "data10_0.py"]

