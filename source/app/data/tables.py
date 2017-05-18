# tables.py

from .dbsession import *

class Muggle(SqlAlchemyBase):
    __tablename__ = 'User'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    twitter_handle = sqlalchemy.Column(sqlalchemy.String, index=True, unique=True, nullable=False)
    email = sqlalchemy.Column(sqlalchemy.String, index=True, unique=True)

    # relationships
    submits = orm.relationship('MuggleAction', back_populates='submitter')
    actions = orm.relationship('MuggleAction', back_populates='muggles')


class MuggleAction(SqlAlchemyBase):
    __tablename__ = 'Muggle Action'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    submitter_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('User.id'), nullable=False)

    # relationships
    submitter = orm.relationship('Muggle', back_populates='submits')
    muggles = orm.relationship('Muggle', back_populates='actions')
