FROM python:latest
WORKDIR /api
COPY . /api
RUN pip install -r requirements.txt
CMD ["python3", "run.py"]

# docker build -t pydo:latest .    
# docker run -p 5000:5000 pydo:latest 
