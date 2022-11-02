FROM python:3.8-buster
RUN mkdir /myapp
COPY ./requirements.txt /myapp

WORKDIR /myapp
RUN pip3 install -r requirements.txt

COPY ./app.py .
ENTRYPOINT ["panel", "serve", "--port", "5555", "app.py"]
