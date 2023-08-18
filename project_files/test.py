from flask import Flask
from flask import json, request
app = Flask(__name__)
@app.get('/')
def a():
    b = request.json()
    return b
if __name__ == '__main__':
    app.run(debug=True,port=7001)