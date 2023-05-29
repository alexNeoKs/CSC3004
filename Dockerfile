FROM python

WORKDIR /

COPY . .

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python3","main.py"]


# docker build -t chatserver .
# docker login --username <username>
# docker tag localimage:version remoteregistry:version
# docker push remoteregistry:version
# docker run --name chatserver -it -p 5000:5000 -d chatserver