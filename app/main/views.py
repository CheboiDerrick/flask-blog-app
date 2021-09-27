from flask import render_template, redirect, url_for,abort,request
from . import main
from flask_login import login_required,current_user
from ..models import User,Pitch,Comment,Upvote,Downvote
from .forms import UpdateProfile,PitchForm,CommentForm
from .. import db,photos


@main.route('/')
def index():
    pitches = Pitch.query.all()
    technology = Pitch.query.filter_by(category="Technology").all() 
    print(technology)
    health = Pitch.query.filter_by(category = 'Health').all()
    education = Pitch.query.filter_by(category = 'Education').all()
    title='Flash Pitch'
    return render_template('index.html', education = education,technology = technology, pitches = pitches, health=health, title=title)