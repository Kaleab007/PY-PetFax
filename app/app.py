# config                    
from flask import Flask
app = Flask(__name__)

# index routes 
@app.route('/')
def index():
    return 'Hello, this is PetFax'
#pets
@app.route('/pets')
def pets():
    return 'These are our pets available for adoption!'