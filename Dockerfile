FROM python:3.8

WORKDIR /app

COPY *.py /app
COPY *.txt /app

RUN pip install -r requirements.txt
EXPOSE 5000


CMD ["python", "app.py"]