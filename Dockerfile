FROM python

WORKDIR /

COPY . .

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python3","main.py"]

# docker build -t chart-server .
# docker run --name chart-server -it -p 5000:5000 -d chart-server