# data.py

from app.data import *

@DBSessionFactory.sessionmethods
class MuggleData:
    join = orm.joinedload('muggles')

    @staticmethod
    def muggles(session):
        return session.query(Muggle).options(EntryData.join).all()

    @staticmethod
    def get_muggle(session, muggle_id):
        return session.query(Muggle).filter_by(id=muggle_id).options(EntryData.join).first()

    @staticmethod
    def new_muggle(session, *, muggle_id, active=True):
        return session.add(Muggle(id=muggle_id, active=active))


@DBSessionFactory.sessionmethods
class EntryData:
    join = orm.joinedload('entries')

    @staticmethod
    def entries(session):
        return session.query(Entry).options(MuggleData.join).all()

    @staticmethod
    def get_entry(session, entry_id):
        return session.query(Entry).filter_by(id=entry_id).options(MuggleData.join).first()

    @staticmethod
    def new_entry(session, *, entry_id, txt):
        return session.add(Entry(id=entry_id, txt=txt, status=False))


@DBSessionFactory.sessionmethods
class DataService(MuggleData, EntryData):
    @staticmethod
    def assign(session, *, muggle_id, entry_id):
        muggle = session.query(Muggle).filter_by(id=muggle_id).options(EntryData.join).first()
        entry = session.query(Entry).filter_by(id=entry_id).options(MuggleData.join).first()
        entry.muggles.append(muggle)


__all__ = ['DataService']
