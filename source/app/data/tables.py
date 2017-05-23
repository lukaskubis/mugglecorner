# tables.py

from sqlalchemy import Table, Column, ForeignKey, String, Integer, Boolean
from .dbsession import *


# association table
mugglary = Table('Mugglary', Base.metadata,
    Column('mug_id', String, ForeignKey('Muggle.id')),
    Column('mugthing_id', String, ForeignKey('CornerEntry.id'))
    )


class Muggle(Base):
    __tablename__ = 'Muggle'

    id = Column(String, primary_key=True)
    active = Column(Boolean, index=True, nullable=False)

    # mugglary
    entries = orm.relationship('CornerEntry', secondary=lambda: mugglary, back_populates='muggles')


class CornerEntry(Base):
    __tablename__ = 'CornerEntry'

    id = Column(String, primary_key=True)
    txt = Column(String, index=True, nullable=False)
    status = Column(Boolean, index=True, nullable=False)

    # mugglary
    muggles = orm.relationship('Muggle', secondary=lambda: mugglary, back_populates='entries')
