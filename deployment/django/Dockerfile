FROM python:3.11.6-bookworm as build

WORKDIR /app

COPY ../../app/requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY ../../app /app/

RUN apt-get update -q && apt-get install -yq \
    gdal-bin \
    libgdal-dev \
    proj-bin \
    libproj-dev \
    gettext \
    python3-pip \
    python3-cffi \
    python3-brotli \
    libpango-1.0-0 \
    tesseract-ocr && \
    apt-get clean && rm -rf /var/lib/apt/lists/*


RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=bit_app.settings.base

CMD ["while !</dev/tcp/db/5432 do sleep 1; done;"]
