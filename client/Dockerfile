FROM python:3.12-slim

WORKDIR /app

COPY . .

RUN pip install --upgrade pip && pip install flask requests

ENTRYPOINT [ "python", "app.py" ]

