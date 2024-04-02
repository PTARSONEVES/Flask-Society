from flask import (
    Blueprint,
    Flask, 
    jsonify, 
    send_from_directory, 
    request,
    current_app,
)
#from flask_sqlalcemy import SQLAlchemy
from werkzeug.utils import secure_filename
import os

bp = Blueprint('managefiles', __name__)

@bp.route("/staticfiles/<path:filename>")
def staticfiles(filename):
    return send_from_directory(current_app.config["STATIC_FOLDER"],filename)

@bp.route("/media/<path:filename>")
def mediafiles(filename):
    return send_from_directory(current_app.config["MEDIA_FOLDER"],filename)

@bp.route("/upload", methods=["GET","POST"])
def upload_file():
    if request.method=="POST":
        file=request.files["file"]
        filename=secure_filename(file.filename)
        file.save(os.path.join(current_app.config["MEDIA_FOLDER"],filename))
        return """
        <!doctype html>
        <title>upload new File</title>
        <form action="" method=post enctype=multipart/form-data>
            <p><input type=file name=file><input type=submit value=Upload>
        </form>
        """
    if request.method=="GET":
        return """
        <!doctype html>
        <title>upload new File</title>
        <form action="" method=post enctype=multipart/form-data>
            <p><input type=file name=file><input type=submit value=Upload>
        </form>
        """