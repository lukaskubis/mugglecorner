# data.py

from ..data import *

class DataService:
    @staticmethod
    @DBSessionFactory.querysession
    def muggles(session):
        return session.query(Muggle).all()

    @staticmethod
    @DBSessionFactory.querysession
    def add_muggle(session, uid, active=True):
        credentials = {'id':uid, 'active':active}
        session.add(Muggle(**credentials))
