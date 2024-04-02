from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for,current_app
)
from werkzeug.exceptions import abort

from flaskr.controller.auth.auth import login_required

bp = Blueprint('start',__name__)

@bp.route('/')
def home():
    nfan = current_app.config["NOME_FANTASIA"]
    return render_template('home.html',rsoc=nfan) 
