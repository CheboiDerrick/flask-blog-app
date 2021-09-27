from flask import render_template, redirect, url_for,abort,request
from . import main
from flask_login import login_required,current_user
from ..models import User,Blog,Comment,Upvote,Downvote
from .forms import UpdateProfile,BlogForm,CommentForm
from .. import db,photos


@main.route('/')
def index():
    blogs = Blog.query.all()
    technology = Blog.query.filter_by(category="Technology").all() 
    print(technology)
    health = Blog.query.filter_by(category = 'Health').all()
    education = Blog.query.filter_by(category = 'Education').all()
    title='Blogs | Home'
    return render_template('index.html', education = education,technology = technology, blogs = blogs, health=health, title=title)