FROM python:alpine

LABEL org.opencontainers.image.description Simple Web Application developed in Flask with Colorful background 

COPY . /opt/
WORKDIR /opt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 9000

ENV APP_COLOR=dark
ENV APP_VERSION=v8

ENTRYPOINT ["python", "app.py"]
#CMD ["--color", "red"]