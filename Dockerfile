FROM python:3.9-slim

WORKDIR /app1

COPY . /app1
RUN pip install -r requirements.txt

CMD ["python","Day4_2.py"]
