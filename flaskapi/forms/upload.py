from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Length
from flask_wtf.file import FileField


class FileForm(Form):
    file = FileField('Your File:  ')
    description = StringField('Description: ', validators=[Length(0, 30)])
    submit = SubmitField('Submit')