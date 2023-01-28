FROM ubuntu:20.04
MAINTAINER Fedi Aniefuna "fedia@uoregon.edu"
RUN apt-get update -y
RUN apt-get install python3.8 python3-pip -y
COPY ./web /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python3"]
CMD ["app.py"]
