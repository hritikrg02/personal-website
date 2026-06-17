FROM ghcr.io/benoitc/gunicorn:24.1.0

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
