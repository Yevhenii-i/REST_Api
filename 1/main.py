from flask import Flask

app = Flask(__name__)


def create_app():
    app = Flask(__name__)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5000)
