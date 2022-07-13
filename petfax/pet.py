from flask import (Blueprint , render_template)
import json

pets = json.load(open('pets.json'))
print(pets)

bp = Blueprint('pet', __name__, url_prefix="/pets")

@bp.route('/')
def index():
    return render_template('index.html', pets=pets)

@bp.route('/<int:id>')
def image(id):
    pet = pets[id -1]
    return render_template('image.html', pet=pet)

@bp.route('/about')
def about():
  
    return render_template('about.html')



