FROM python:3.11-slim

WORKDIR /python-app

COPY menu.py .

RUN apt-get update
RUN apt-get install -y python3-tk
RUN apt-get install -y tk
RUN apt-get clean

CMD ["python","menu.py"]

