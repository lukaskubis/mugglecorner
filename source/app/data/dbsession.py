# dbsession.py

import sqlalchemy
import sqlalchemy.orm as orm
import sqlalchemy.ext.declarative as db

from functools import wraps
from contextlib import contextmanager

Base = db.declarative_base()


class DBSessionFactory:
    session = None

    @staticmethod
    def global_init(db_file):
        if DBSessionFactory.session:
            return

        if not db_file or not db_file.strip():
            raise Exception('Data file error ({}, {})'.format(db_file, db_file.strip()))

        conn_str = 'sqlite:///' + db_file
        engine = sqlalchemy.create_engine(conn_str, echo=True)
        Base.metadata.create_all(engine)
        DBSessionFactory.session = orm.sessionmaker(bind=engine)

    @staticmethod
    @contextmanager
    def make_session():
        session = DBSessionFactory.session()
        session.result = None
        try:
            yield session
        finally:
            if session.result is None:
                session.commit()

    @staticmethod
    def session_method(func):
        @wraps(func)
        def session_wrapper(*args, **kwargs):
            with DBSessionFactory.make_session() as session:
                session.result = func(session, *args, **kwargs)
                return session.result
        return session_wrapper

    @staticmethod
    def session_methods(cls):
        for key, val in cls.__dict__.items():
            if isinstance(val, (staticmethod)):
                setattr(cls, key, staticmethod(DBSessionFactory.session_method(val.__func__)))
        return cls
