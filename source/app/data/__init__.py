# __init__.py

from os.path import dirname, join

from .tables import *
from .dbsession import *

# ../../
db_folder = dirname(dirname(dirname(__file__)))


def init_db(db_folder=db_folder):
    rel_folder = join('db', 'muggledb.sqlite')
    DBSessionFactory.global_init(join(db_folder, rel_folder))
