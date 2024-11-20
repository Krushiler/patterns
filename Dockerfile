FROM python:3.11-alpine

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY ./working_with_settings ./working_with_settings
COPY ./main.py .

EXPOSE 8080

CMD ["python", "main.py"]