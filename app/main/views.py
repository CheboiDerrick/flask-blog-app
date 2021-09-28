from flask import render_template, redirect, url_for,abort,request
from . import main
from flask_login import login_required,current_user
from ..models import User,Blog,Comment,Upvote,Downvote
from .forms import UpdateProfile,BlogForm,CommentForm
from .. import db,photos
from sqlalchemy import desc
from app.request import get_quotes


@main.route('/')
def index():
    blogs = Blog.query.order_by(desc(Blog.time)).all()
    categories = Blog.query.with_entities(Blog.category)
    categories = [r for (r,) in categories]
    quote=get_quotes()
    
    title='Blogs | Home'
    return render_template('index.html', blogs = blogs, categories=categories, title=title, quote=quote)

@main.route('/blogs/<category_name>')
def category(category_name):
    category = Blog.query.filter_by(category=category_name).all()
    categories = Blog.query.with_entities(Blog.category)
    categories = [r for (r,) in categories]
    title=f'{category_name}'
    return render_template('category.html', category = category, title=title, categories=categories, category_name=category_name)

@main.route('/new/blogpost', methods = ['POST','GET'])
@login_required
def new_blog():
    form = BlogForm()
    categories = Blog.query.with_entities(Blog.category)
    categories = [r for (r,) in categories]
    if form.validate_on_submit():
        title = form.title.data
        post = form.post.data
        category = form.category.data
        user_id = current_user
        new_blog_object = Blog(post=post,user_id=current_user._get_current_object().id,category=category,title=title)
        new_blog_object.save_blog ()
        return redirect(url_for('main.index'))
        
    return render_template('new_blog.html', categories=categories,form = form)

@main.route('/comment/<int:blog_id>', methods = ['POST','GET'])
@login_required
def comment(blog_id):
    form = CommentForm()
    blog = Blog.query.get(blog_id)
    all_comments = Comment.query.filter_by(blog_id = blog_id).all()
    categories = Blog.query.with_entities(Blog.category)
    categories = [r for (r,) in categories]
    if form.validate_on_submit():
        comment = form.comment.data 
        blog_id = blog_id
        user_id = current_user._get_current_object().id
        new_comment = Comment(comment = comment,user_id = user_id,blog_id = blog_id)
        new_comment.save_c()
        return redirect(url_for('.comment', blog_id = blog_id))
    return render_template('comment.html', form =form, blog = blog,all_comments=all_comments, categories=categories)

@main.route('/user/<name>')
def profile(name):
    user = User.query.filter_by(username = name).first()
    user_id = current_user._get_current_object().id
    posts = Blog.query.filter_by(user_id = user_id).all()
    categories = Blog.query.with_entities(Blog.category)
    categories = [r for (r,) in categories]
    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user,posts=posts, categories=categories)


@main.route('/user/<name>/updateprofile', methods = ['POST','GET'])
@login_required
def updateprofile(name):
    form = UpdateProfile()
    user = User.query.filter_by(username = name).first()
    categories = Blog.query.with_entities(Blog.category)
    categories = [r for (r,) in categories]
    if user == None:
        abort(404)
    if form.validate_on_submit():
        user.bio = form.bio.data
        user.save_u()
        return redirect(url_for('.profile',name = name))
    return render_template('profile/update.html',form =form, categories=categories)

@main.route('/user/<name>/update/pic',methods= ['POST'])
@login_required
def update_pic(name):
    categories = Blog.query.with_entities(Blog.category)
    categories = [r for (r,) in categories]
    user = User.query.filter_by(username = name).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',name=name, categories=categories))

@main.route('/like/<int:id>',methods = ['POST','GET'])
@login_required
def like(id):
    get_blogs = Upvote.get_upvotes(id)
    valid_string = f'{current_user.id}:{id}'
    for blog in get_blogs:
        to_str = f'{blog}'
        print(valid_string+" "+to_str)
        if valid_string == to_str:
            return redirect(url_for('main.index',id=id))
        else:
            continue
    new_vote = Upvote(user = current_user, blog_id=id)
    new_vote.save()
    return redirect(url_for('main.index',id=id))

@main.route('/dislike/<int:id>',methods = ['POST','GET'])
@login_required
def dislike(id):
    blog = Downvote.get_downvotes(id)
    valid_string = f'{current_user.id}:{id}'
    for p in blog:
        to_str = f'{p}'
        print(valid_string+" "+to_str)
        if valid_string == to_str:
            return redirect(url_for('main.index',id=id))
        else:
            continue
    new_downvote = Downvote(user = current_user, blog_id=id)
    new_downvote.save()
    return redirect(url_for('main.index',id = id))

