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
    def get_muggle(session, uid):
        return session.query(Muggle).filter_by(id=uid).options(EntryData.join).first()

    @staticmethod
    @DBSessionFactory.querysession
    def add_muggle(session, uid, active=True):
        return session.add(Muggle(id=uid, active=active))


class EntryData:
    join = orm.joinedload('entries')

    @staticmethod
    @DBSessionFactory.querysession
    def muggly_things(session):
        return session.query(Entry).options(MuggleData.join).all()

    @staticmethod
    @DBSessionFactory.querysession
    def get_muggly_thing(session, mid):
        return session.query(Entry).filter_by(id=mid).options(MuggleData.join).first()

    @staticmethod
    @DBSessionFactory.querysession
    def add_muggly_thing(session, mid, txt):
        return session.add(Entry(id=mid, txt=txt, status=False))


class DataService(MuggleData, EntryData):
    pass
