# data.py

from app.data import *

@DBSessionFactory.session_methods
class MuggleData:
    join = orm.joinedload('muggles')

    @staticmethod
    def muggles(session):
        return session.query(Muggle).options(EntryData.join).all()

    @staticmethod
    def get_muggle(session, id):
        return session.query(Muggle).filter_by(id=id).options(EntryData.join).first()

    @staticmethod
    def new_muggle(session, *, id, active=True):
        return session.add(Muggle(id=id, active=active))


@DBSessionFactory.session_methods
class EntryData:
    join = orm.joinedload('entries')

    @staticmethod
    def entries(session):
        return session.query(Entry).options(MuggleData.join).all()

    @staticmethod
    def get_entry(session, id):
        return session.query(Entry).filter_by(id=id).options(MuggleData.join).first()

    @staticmethod
    def new_entry(session, *, id, txt):
        return session.add(Entry(id=id, txt=txt, status=False))


@DBSessionFactory.session_methods
class DataService(MuggleData, EntryData):
    @staticmethod
    def assign(session, *, muggle_id, entry_id):
        muggle = session.query(Muggle).filter_by(id=muggle_id).options(EntryData.join).first()
        entry = session.query(Entry).filter_by(id=entry_id).options(MuggleData.join).first()
        entry.muggles.append(muggle)


__all__ = ['DataService']
