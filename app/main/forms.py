from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField,SubmitField
from ..models import Blog, Comment
from wtforms.validators import DataRequired

class BlogForm(FlaskForm):
    title = StringField('Pitch Category Title', validators=[DataRequired()])
    body = TextAreaField('Enter your Pitch here', validators=[DataRequired()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    comment = TextAreaField('Write a comment here',validators=[DataRequired()])
    submit = SubmitField('Submit')
