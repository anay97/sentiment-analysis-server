from flask import Flask
from flask import request
from sentiment import getMood

app = Flask(__name__)

@app.route("/")
def hello():
    query=request.args.get('query')
    return getMood(query)

if (__name__ == "__main__"):
    app.run(port = 5000)
