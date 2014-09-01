from flaskapi import db
from flaskapi.models.base import Base


class Asset(db.Model, Base):
    """
    Asset model
    """
    __tablename__ = 'assets'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50))
    description = db.Column(db.Unicode(200))
    type = db.Column(db.String(50))
    asset_text = db.Column(db.TEXT)
    asset_binary = db.Column(db.BLOB)

    def __init__(self, name, description='', type='binary', content=''):
        """
        Asset model
        :param name: string name of asset
        :param description: string description of asset
        :param type: string type of asset, usually 'string' or 'binary', defaults to binary
        :param content: string content
        :return:
        """
        self.name = name
        self.description = description
        self.type = type
        if type is "binary":
            self.asset_binary = content
        else:
            self.asset_text = content

    def __repr__(self):
        return 'Name: %r' % self.name

    @classmethod
    def search(cls, keyword):
        """
        simple search
        :param keyword: terms to search
        :return: sqlalchemy query result object
        """
        query = "SELECT id, name, description from " + cls.__tablename__ +\
                " WHERE MATCH (asset_text) AGAINST ('%s' IN BOOLEAN MODE)" % keyword
        data = cls.query.from_statement(query).all()
        #result = []
        #for row in data:
        #    result.append({"id": row.id, "name": row.name, "description": row.description})
        #return result
        return data

    def as_dict(self):
        """
        column constraint dict repr
        :return: more usable __dict__ that can be serialized
        """
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    @classmethod
    def serialize(cls, query_object):
        """
        turn query objects into serializable list+dict
        :param query_object: sqlalchemy orm query object
        :return: [{}]
        """
        results = []

        try:
            for item in query_object:
                results.append(item.as_dict())
        except Exception:
            results.append(query_object.as_dict())
        return results