FROM python:3.9-slim

WORKDIR /app1

COPY . /app1
CMD ["pyhton","pip install -r requirements.txt"]

CMD ["python","Day_4_2.py"]
