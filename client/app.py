import requests
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    response = requests.get("http://server:4000") #name the server container server or else it will not work 
    return f"CLIENT GOT: {response.text}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
