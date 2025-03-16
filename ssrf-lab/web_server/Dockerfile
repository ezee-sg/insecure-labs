FROM python:3.9

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN apt-get update && apt-get install -y iptables && rm -rf /var/lib/apt/lists/*

EXPOSE 5000

#RUN iptables -A INPUT -p tcp --dport 3000 -j DROP

CMD ["sh", "-c", "python app.py & python api_interna.py"]
