FROM python:3.9

ENV PYTHONUNBUFFERED 1

RUN mkdir /app

WORKDIR /app

COPY . .

RUN apt update
RUN apt-get install -y chromium

RUN pip install -r requirements.txt


WORKDIR /app/radon

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]