# factory
from flask import Flask


def create_app():
    app = Flask(__name__)
    
    @app.route('/')
    def index():
        return 'Hello, PetFax!'

    # register pet blueprint 
    from . import pet
    app.register_blueprint(pet.bp)
    
    from . import about
    app.register_blueprint(about.bp)


    # return the app 
    return app