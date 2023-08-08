FROM python:3.8-slim-buster

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

ENV FLASK_APP=app.py
ENV FLASK_ENV=production

CMD ["gunicorn", "--workers", "4", "--bind", "0.0.0.0:8000", "app:app"]
