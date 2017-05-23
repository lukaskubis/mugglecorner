# data.py

from ..data import *


class MuggleData:
    join = orm.joinedload('muggles')

    @staticmethod
    @DBSessionFactory.querysession
    def muggles(session):
        return session.query(Muggle).options(EntryData.join).all()

    @staticmethod
    @DBSessionFactory.querysession
    def get_muggle(session, muggle_id):
        return session.query(Muggle).filter_by(id=muggle_id).options(EntryData.join).first()

    @staticmethod
    @DBSessionFactory.querysession
    def new_muggle(session, muggle_id, active=True):
        return session.add(Muggle(id=muggle_id, active=active))


class EntryData:
    join = orm.joinedload('entries')

    @staticmethod
    @DBSessionFactory.querysession
    def entries(session):
        return session.query(Entry).options(MuggleData.join).all()

    @staticmethod
    @DBSessionFactory.querysession
    def get_entry(session, entry_id):
        return session.query(Entry).filter_by(id=entry_id).options(MuggleData.join).first()

    @staticmethod
    @DBSessionFactory.querysession
    def new_entry(session, mid, txt):
        return session.add(Entry(id=mid, txt=txt, status=False))


class DataService(MuggleData, EntryData):
    pass
