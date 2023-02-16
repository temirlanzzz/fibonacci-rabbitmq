FROM python:3.9
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
COPY fibonacci_worker.py /app/fibonacci_worker.py
CMD ["python", "fibonacci_worker.py"]
