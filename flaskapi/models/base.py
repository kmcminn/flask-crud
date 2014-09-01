from flaskapi import db


class Base(object):
    def save(self, commit=True):
        db.session.add(self)

        if commit:
            db.session.commit()
