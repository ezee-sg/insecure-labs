FROM python:3.9

WORKDIR /app

RUN apt-get update && apt-get install -y \
    wkhtmltopdf \
    && apt-get clean

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000
