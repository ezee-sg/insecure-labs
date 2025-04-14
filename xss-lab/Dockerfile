FROM python:3.9

# Falta instalar el chrome
RUN apt-get update && apt-get install -y \
    firefox-esr \
    wget \
    && wget https://github.com/mozilla/geckodriver/releases/download/v0.30.0/geckodriver-v0.30.0-linux64.tar.gz \
    && tar -xvzf geckodriver-v0.30.0-linux64.tar.gz \
    && mv geckodriver /usr/local/bin/

# Asegúrate de que Firefox esté instalado
RUN firefox --version

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["sh", "-c", "python db.py && python app.py & python admin_bot.py"]
