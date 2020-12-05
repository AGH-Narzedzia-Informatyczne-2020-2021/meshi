FROM python:3.8.6
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN apt-get -y --no-upgrade update && apt-get -y upgrade python3-dev libpq-dev libgirepository1.0-dev libglib2.0-dev build-essential libpython3-dev libdbus-1-dev libcups2-dev libcairo2-dev pkg-config 
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
COPY . /code/