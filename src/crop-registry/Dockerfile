FROM python:3.12-slim

WORKDIR /app

COPY /app/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expone el puerto de la aplicación (usualmente FastAPI usa el puerto 8000)
EXPOSE 8000

# Comando para ejecutar la aplicación usando Uvicorn
CMD ["fastapi", "run", "--host", "0.0.0.0", "--port", "8000"]
