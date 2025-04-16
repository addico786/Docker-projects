FROM python:3.11-slim

WORKDIR /python-app

COPY menu.py . 

RUN sudo apt-get update 
    sudo apt-get install -y python3-tk 
    sudo apt-get install -y tk 
    sudo apt-get clean

CMD ["python","menu.py"]
    
