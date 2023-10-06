FROM python:3.10-alpine

RUN pip install --upgrade pip
RUN pip install flask

COPY . /opt/

EXPOSE 9000

WORKDIR /opt

ENTRYPOINT ["python", "app.py"]
