FROM python:3
MAINTAINER Magnus Bystrom <mbystrom@gmail.com>
LABEL version="0.0.2"

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN pip3 install hug -U

COPY . .
EXPOSE 8080
USER 9000 
CMD [ "hug", "-p", "8080", "-f", "./service.py" ]
