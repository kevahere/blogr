from flask import render_template,url_for,flash,redirect,request,abort
from . import main
from .forms import BlogForm, CommentForm
from ..models import User, Blog, Category, Comment
from ..import db
from flask_login import login_required,current_user

@main.route('/')
def index():
    """View root function that returns index"""
    title =  'Home | welcome to pitches'
    return render_template('index.html', title = title)

@main.route('/blog/new',methods=["GET","POST"])
def new_blog():
    form = BlogForm()
    if form.validate_on_submit():
        blog = blog(title = form.title.data, body = form.body.data)
        db.session.add(blog)
        db.session.commit()
        flash('Nice blog!')
        return redirect (url_for('main.new_blog'))
    title = "Show us what you've got"
    blogs = Blog.query.all()

    return render_template('blog.html', title=title, form=form, blog_list=blogs)

