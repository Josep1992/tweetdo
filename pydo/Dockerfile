FROM python:latest
WORKDIR /pydo
COPY . /pydo
RUN pip install -r requirements.txt
CMD ["python", "index.py"]

# docker build -t pydo:latest .    
# docker run -p 5000:5000 pydo:latest 
