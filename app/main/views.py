from flask import render_template,url_for,flash,redirect,request,abort
from . import main
#from .forms import PitchForm, CommentForm
#from ..models import User, Pitch, Category, Comment
from ..import db
from flask_login import login_required,current_user

@main.route('/')
def index():
    """View root function that returns index"""
    title =  'Home | welcome to pitches'
    return render_template('index.html', title = title)

