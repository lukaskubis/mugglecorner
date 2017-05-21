# dbsession.py

import sqlalchemy
import sqlalchemy.orm as orm
import sqlalchemy.ext.declarative as db

from functools import wraps
from .tables import *

SqlAlchemyBase = db.declarative_base()

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
        SqlAlchemyBase.metadata.create_all(engine)
        DBSessionFactory.session = orm.sessionmaker(bind=engine)


def db_session(query_func):
    @wraps(query_func)
    def session_wrapper(*args, **kwargs):
        session = DBSessionFactory.session()
        query_result = query_func(session, *args, **kwargs)
        if not query_result:
            session.commit()
        else:
            return query_result
    return session_wrapper
