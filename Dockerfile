FROM python:3.8

WORKDIR /app

COPY *.py /app
COPY *.txt /app
COPY templates /app/templates

RUN pip install -r requirements.txt


CMD ["python", "app.py"]