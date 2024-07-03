FROM python:3.8-slim

WORKDIR /app

COPY traffic_generator.py .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "traffic_generator.py"]
