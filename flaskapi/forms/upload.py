from flask.ext.wtf import Form
from wtforms import StringField, TextAreaField, BooleanField, SelectField,\
    SubmitField
from wtforms.validators import Required, Length, Email, Regexp
from flask_wtf.file import FileField
from wtforms import ValidationError
from flask.ext.pagedown.fields import PageDownField
from ..models import Role, User

class EditProfileForm(Form):
    name = StringField('filename', validators=[Length(0, 64)])
    description = StringField('Location', validators=[Length(0, 64)])
    n_file = FileField('Your File:')
    submit = SubmitField('Submit')