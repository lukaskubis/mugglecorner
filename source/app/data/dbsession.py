# dbsession.py

import sqlalchemy
import sqlalchemy.ext.declarative as db

SqlAlchemyBase = db.declarative_base()

class DBSessionFactory:
    @staticmethod
    def global_init(db_file):
        if not db_file or not db_file.strip():
            raise Exception('Data file err')

        conn_str = 'sqlite:///' + db_file
        engine = sqlalchemy.create_engine(conn_str)
        SqlAlchemyBase.metadata.create_all(engine)
