FROM python:3.13-slim

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "django_project/manage.py", "runserver", "0.0.0.0:8000", "--noreload"]
