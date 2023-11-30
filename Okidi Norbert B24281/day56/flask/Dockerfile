FROM python:3.8-slim

WORKDIR /flask

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py /flask

COPY .env .

CMD ["python", "app.py"]