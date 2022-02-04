from flask import Flask, g
from router import blueprints

def create_app():
    app = Flask(__name__)

    # app config
    app.config.from_pyfile("config.py")

    # set routers
    for bp in blueprints:
        app.register_blueprint(bp)

    @app.teardown_appcontext
    def teardown_db(exception):
        db = g.pop('db', None)
        if db is not None:
            print("close db")
            db.dispose()

    return app

if __name__ == "__main_-":
    app = create_app()
    app.run()

