FROM python:3.11
EXPOSE 3000
WORKDIR /app
COPY requirements.txt /app
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    poppler-utils \
    tesseract-ocr \
    tesseract-ocr-fas \
    --no-install-recommends && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
RUN pip3 install -r requirements.txt --no-cache-dir
COPY . /app
ENTRYPOINT ["python3"]
CMD ["manage.py", "runserver", "0.0.0.0:3000"]
