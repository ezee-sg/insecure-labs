FROM debian:latest

RUN apt-get update && apt-get install -y \
    texlive-latex-base \
    texlive-latex-extra \
    texlive-fonts-recommended \
    texlive-fonts-extra \
    texlive-lang-spanish \
    python3 \
    python3-pip

WORKDIR /app

COPY requirements.txt .
RUN pip3 install -r requirements.txt --break-system-packages

COPY . .

EXPOSE 5000

CMD ["python3", "app.py"]
