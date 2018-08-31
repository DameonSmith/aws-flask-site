from flask import Flask
application = Flask(__name__)


@application.route("/")
def hello():
    return "<h1 style='color:green'>Hello There!</h1>"


@application.route("/health")
def health():
    return "<h1 style='color:blue'>Application is Healthy!</h1>"


if __name__ == "__main__":
    application.run(host='0.0.0.0')
