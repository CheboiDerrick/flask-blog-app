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

@main.route('/blogs/<category_name>')
def category(category_name):
    category = Blog.query.filter_by(category=category_name).all() 
    title=f'{category_name} Pitches'
    return render_template('category.html', category = category, title=title, category_name=category_name)

@main.route('/blogpost', methods = ['POST','GET'])
@login_required
def new_blog():
    form = BlogForm()
    if form.validate_on_submit():
        title = form.title.data
        post = form.post.data
        category = form.category.data
        user_id = current_user
        new_pitch_object = Blog(post=post,user_id=current_user._get_current_object().id,category=category,title=title)
        new_pitch_object.save_p()
        return redirect(url_for('main.index'))
        
    return render_template('new_blog.html', form = form)