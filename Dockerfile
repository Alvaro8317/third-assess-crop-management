FROM python:3
WORKDIR /crop-management
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY src/ .
EXPOSE 5000
CMD ["python", "app.py"]
