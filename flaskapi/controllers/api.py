from flaskapi.models.asset import *
from flaskapi.util import *
from flask import request, make_response, flash, render_template
from wtforms import StringField, SubmitField
from wtforms.validators import Length
from flask.ext.wtf import Form
from flask_wtf.file import FileField


@app.route('/', methods=['GET'])
def home():
    return render_template('form.html')


@app.route('/test/<param>', methods=['GET'])
@app.route('/test', methods=['GET'])
def test(param=''):
    return render_template('test.html', name=param)


@app.route('/monitor')
def monitor():
    return 'OK'


@app.route('/api/index', methods=['GET'])
def index():
    return render_json(Asset.serialize(Asset.query.limit(10).offset(0).all()))


class FileForm(Form):
    file = FileField('Your File:  ')
    description = StringField('Description: ', validators=[Length(0, 30)])
    submit = SubmitField('Submit')


@app.route('/api/publish', methods=('GET', 'POST'))
def upload():
    form = FileForm()
    if form.validate_on_submit():
        # TODO: bugfix wtf-flask and werkzeug
        # TODO: hash implementation
        # TODO: create or update based on unique or same hash
        # TODO: unclutter this method
        new_file = request.files['file']
        allowed_file(new_file.filename)

        file_content = request.files['file'].stream.read(512)
        file_type = 'text' if is_text(file_content) else 'binary'

        file_content = unicode_safe(file_content + request.files['file'].stream.read(), 'utf-8')
        file_name = new_file.filename
        asset = Asset(file_name, request.form['description'], file_type, file_content)
        asset.save()
        flash('File Uploaded Successfully')
    else:
        file_name = None
        flash_errors(form)
    return render_template('upload.html', form=form, filename=file_name)


@app.route('/api/search/<terms>')
def search(terms=''):
    return render_json(Asset.serialize(Asset.search(terms)))


@app.route('/api/get/<my_id>')
def fetch(my_id=''):
    result = Asset.query.get(my_id)
    app.logger.debug(result.count())
    try:
        content = result.asset_binary
    except:
        content = result.asset_text
    if "text" in result.type:
        content = result.asset_text

    response = make_response(content)
    response.headers["Content-Disposition"] = "attachment; filename=" + result.name
    return response


@app.route('/api/view/<my_id>')
def view(my_id=1):
    return render_json(Asset.serialize(Asset.query.get(int(my_id))))