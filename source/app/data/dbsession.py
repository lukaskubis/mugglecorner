# dbsession.py

import sqlalchemy
import sqlalchemy.orm as orm
import sqlalchemy.ext.declarative as db

SqlAlchemyBase = db.declarative_base()


class DBSessionFactory:
    factory = None

    @staticmethod
    def global_init(db_file):
        if DBSessionFactory.factory:
            return

        if not db_file or not db_file.strip():
            raise Exception('Data file err')

        conn_str = 'sqlite:///' + db_file
        engine = sqlalchemy.create_engine(conn_str, echo=False)
        SqlAlchemyBase.metadata.create_all(engine)
        DBSessionFactory.factory = orm.sessionmaker(bind=engine)
