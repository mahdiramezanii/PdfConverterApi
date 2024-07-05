FROM python:3.11

# باز کردن پورت 8000 برای دسترسی به سرور توسعه Django
EXPOSE 8000

# تنظیم دایرکتوری کاری در داخل کانتینر
WORKDIR /app

# کپی کردن فایل requirements.txt به دایرکتوری کاری
COPY requirements.txt /app/

# نصب وابستگی‌ها و بسته‌های مورد نیاز
RUN apt-get update && apt-get install -y \
    libpq-dev \
    poppler-utils \
    tesseract-ocr \
    tesseract-ocr-fas \
    --no-install-recommends && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN pip3 install --no-cache-dir -r requirements.txt

# کپی کردن تمامی فایل‌های پروژه به دایرکتوری کاری
COPY . /app/

CMD ["python3","manage.py", "runserver", "0.0.0.0:8000"]
