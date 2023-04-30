FROM python:3.8-slim-buster
WORKDIR /app
COPY requirements.txt requirements.txt
COPY app.py app.py
COPY spam_ham_model.pkl spam_ham_model.pkl
RUN pip3 install -r requirements.txt
CMD ["python3", "app.py"]
EXPOSE 8080

