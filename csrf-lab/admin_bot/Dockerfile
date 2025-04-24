FROM python:3.9

RUN apt-get update && apt-get install -y \
    curl \
    gnupg \
    && apt-get clean

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "admin_bot.py"]
