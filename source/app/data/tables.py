# tables.py

from .dbsession import *


class Muggle(SqlAlchemyBase):
    __tablename__ = 'Muggle'

    id = sqlalchemy.Column(sqlalchemy.String, primary_key=True)
    active = sqlalchemy.Column(sqlalchemy.Boolean)

    # relationships
    # muggly_things = orm.relationship('MugglyThing', back_populates='muggles')


class MugglyThing(SqlAlchemyBase):
    __tablename__ = 'MugglyThing'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    txt = sqlalchemy.Column(sqlalchemy.String, index=True)
    page = sqlalchemy.Column(sqlalchemy.String, index=True, unique=True)

    # relationships
    # muggles = orm.relationship('Muggle', back_populates='actions')
