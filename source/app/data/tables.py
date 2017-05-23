# tables.py

from sqlalchemy import Table, Column, ForeignKey, String, Integer, Boolean
from .dbsession import *


# association table
mugglary = Table('Mugglary', Base.metadata,
    Column('mug_id', String, ForeignKey('Muggle.id')),
    Column('entry_id', String, ForeignKey('Entry.id'))
    )


class Muggle(Base):
    __tablename__ = 'Muggle'

    id = Column(String, primary_key=True)
    active = Column(Boolean, index=True, nullable=False)

    # mugglary
    entries = orm.relationship('Entry', secondary=lambda: mugglary, back_populates='muggles')


class Entry(Base):
    __tablename__ = 'Entry'

    id = Column(String, primary_key=True)
    txt = Column(String, index=True, nullable=False)
    status = Column(Boolean, index=True, nullable=False)

    # mugglary
    muggles = orm.relationship('Muggle', secondary=lambda: mugglary, back_populates='entries')
