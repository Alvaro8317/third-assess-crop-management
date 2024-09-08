FROM python:3

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /crop-management

# Copia el archivo de requerimientos (si tienes más dependencias) en el contenedor
COPY requirements.txt requirements.txt

# Instala las dependencias del proyecto
RUN pip install -r requirements.txt

# Copia el código de la aplicación al contenedor
COPY src/ .

# Expone el puerto 5000 para acceder a la aplicación
EXPOSE 5000

# Define el comando por defecto para correr la app
CMD ["python", "app.py"]
