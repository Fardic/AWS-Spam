from flask import Flask, request
import joblib
import logging
app = Flask(__name__)

model = joblib.load("spam_ham_model.pkl")

@app.route("/")
def hello_world():
    return "Version 2 Github"

@app.route("/spamorham", methods=["GET", "POST"])
def spamorham():
    message = request.args.get("message")
    print(message)
    return model.predict([message])[0]

if __name__ == "__main__":
    print("good job")
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)


