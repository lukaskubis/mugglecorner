# tables.py

from sqlalchemy import Table, Column, ForeignKey, String, Integer, Boolean
from .dbsession import *


# association table
mugglary = Table('Mugglary', Base.metadata,
    Column('mug_id', String, ForeignKey('Muggle.id')),
    Column('mugthing_id', String, ForeignKey('MugglyThing.id'))
    )


class Muggle(Base):
    __tablename__ = 'Muggle'

    id = Column(String, primary_key=True)
    active = Column(Boolean, index=True, nullable=False)

    # mugglary
    muggly_things = orm.relationship('MugglyThing', secondary=lambda: mugglary, back_populates='muggles')


class MugglyThing(Base):
    __tablename__ = 'MugglyThing'

    id = Column(String, primary_key=True)
    txt = Column(String, index=True, nullable=False)
    status = Column(Boolean, index=True, nullable=False)

    # mugglary
    muggles = orm.relationship('Muggle', secondary=lambda: mugglary, back_populates='muggly_things')
