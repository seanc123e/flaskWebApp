from flask import Blueprint, render_template
#blueprint tells the application that this file contains multiple URL paths that will be used for the site

views = Blueprint('views', __name__)

#decorator
@views.route('/')
def home():
    return render_template("home.html")
