# data.py

from ..data import *


class MuggleData:
    join = orm.joinedload('muggles')

    @staticmethod
    @DBSessionFactory.querysession
    def muggles(session):
        return session.query(Muggle).options(MugglyThingData.join).all()

    @staticmethod
    @DBSessionFactory.querysession
    def get_muggle(session, uid):
        return session.query(Muggle).filter_by(id=uid).options(MugglyThingData.join).first()

    @staticmethod
    @DBSessionFactory.querysession
    def add_muggle(session, uid, active=True):
        session.add(Muggle(id=uid, active=active))


class MugglyThingData:
    join = orm.joinedload('muggly_things')

    @staticmethod
    @DBSessionFactory.querysession
    def muggly_things(session):
        return session.query(MugglyThing).options(Muggle.join).all()

    @staticmethod
    @DBSessionFactory.querysession
    def get_muggly_thing(session, mid):
        return session.query(MugglyThing).filter_by(id=mid).options(Muggle.join).first()

    @staticmethod
    @DBSessionFactory.querysession
    def add_muggly_thing(session, mid, txt):
        session.add(MugglyThing(id=mid, txt=txt, status=False))


class DataService(MuggleData, MugglyThingData):
    pass
