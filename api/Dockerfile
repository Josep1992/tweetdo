FROM python:3.9

WORKDIR /api

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . /api
CMD ["python3", "run.py"]
