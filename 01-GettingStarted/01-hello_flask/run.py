import os
from flask import Flask # importing flask class

#           1st arg of flask class is name of flask class is the name of the applications's module - our package
app = Flask(__name__) # instance of flask

# in python a decorator starts with the @ symbol which is also called pie notation
# decorator is a way of wrapping functions
@app.route("/")
def index():
    return "Hello, World"


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
