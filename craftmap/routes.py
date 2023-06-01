from flask import render_template
from . import app
from .models.mcworld import get_worlds

@app.route('/')
def home():
    worlds = get_worlds()
    return render_template('index.html', worlds=worlds)
