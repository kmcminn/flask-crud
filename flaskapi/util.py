from __future__ import division
import string
from flaskapi import app
from flask import make_response, Response, render_template, jsonify, flash


def is_text(file_bytes):
    """
    test simple criteria for binary files
    :param file_bytes: string of characters to evaluate
    :return: boolean
    """
    text_characters = "".join(map(chr, range(32, 127)) + list("\n\r\t\b"))
    _null_trans = string.maketrans("", "")
    if not file_bytes:
        # Empty files are considered text
        return True
    if "\0" in file_bytes:
        # Files with null file_bytes are likely binary
        return False
    # Get the non-text characters (maps a character to itself then
    # use the 'remove' option to get rid of the text characters.)
    t = file_bytes.translate(_null_trans, text_characters)
    # If more than 30% non-text characters, then
    # this is considered a binary file
    if len(t)/len(file_bytes) > 0.30:
        return False
    return True


def unicode_safe(obj, *args):
    """

    :param obj: string to convert
    :param args: optional args to pass to unicode()
    :return: decoded string
    """

    try:
        return unicode(obj, *args)
    except UnicodeDecodeError:
        # obj is byte string
        ascii_text = str(obj).encode('string_escape')
        return unicode(ascii_text)


def str_safe(obj):
    """

    :param obj: string to convert
    :return: decoded string
    """
    try:
        return str(obj)
    except UnicodeEncodeError:
        # obj is unicode
        return unicode(obj).encode('unicode_escape')


def allowed_file(filename):
    """

    :param string filename:
    :return: boolean if allowed file extension according to app.config['ALLOWED_EXTENSIONS']
    """
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']


def render_json(data):
    # response = make_response(render_template(template, results=data))
    response = make_response(jsonify(items=data))
    response.headers['Content-Type'] = 'application/json'
    response.mimetype = 'application/json'
    return response


def flash_errors(form):
    """Flashes form errors"""
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (getattr(form, field).label.text, error), 'error')