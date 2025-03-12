from flask import Flask

from .views import main


def handle_404(err):
    return ({"error": "Not Found"}, 404)


def create_app():
    app = Flask(__name__)
    app.register_blueprint(main, url_prefix='/v1/api')
    app.register_error_handler(404, handle_404)
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5000)
