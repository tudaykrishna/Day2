FROM python:3.9-slim

WORKDIR /app1

COPY . /app1

CMD ["python","Day_4_2.py"]
