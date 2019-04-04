FROM python:3
MAINTAINER Magnus Bystrom <mbystrom@gmail.com>
LABEL version="0.0.1"

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN pip3 install hug -U

COPY . .

CMD [ "hug", "-f", "./service.py" ]
