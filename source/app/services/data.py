# data.py

from ..data import *

class DataService:
    @staticmethod
    @db_session
    def muggles(session):
        return session.query(Muggle).all()

    @staticmethod
    @db_session
    def add_muggle(session, uid, active=True):
        credentials = {'id':uid, 'active':active}
        session.add(Muggle(**credentials))
