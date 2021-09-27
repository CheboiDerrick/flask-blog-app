from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, SubmitField
from wtforms.validators import Required

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us a little about your awesome self.',validators = [Required()])
    submit = SubmitField('Update')

class BlogForm(FlaskForm):
    title = StringField('Title', validators=[Required()])
    category = SelectField('Category', choices=[('Design','Design'),('Entertainment','Entertainment'),('Fashion & Style','Fashion & Style'),('Photography','Photograpgy'),('Business','Business')],validators=[Required()])
    post = TextAreaField('Blog', validators=[Required()])
    submit = SubmitField('Post')

class CommentForm(FlaskForm):
    comment = TextAreaField('Leave a comment',validators=[Required()])
    submit = SubmitField('Add Comment')