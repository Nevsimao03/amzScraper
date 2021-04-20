from flask import Blueprint, render_template
from . import db
from flask_login import login_required, current_user
import os

main = Blueprint('main', __name__)

filepath = os.path.join(os.path.dirname(__file__),'results.csv')
open_read = open(filepath,'r')
page =''

while True:
    read_data = open_read.readline()
    page += '<p>%s</p>' % read_data
    if open_read.readline() == '':
        break
@main.route("/data")
def data():
    return page

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)