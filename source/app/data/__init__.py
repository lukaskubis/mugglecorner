# __init__.py

import os
from .tables import *
from .dbsession import *

def init_db(db_folder):
    rel_folder = os.path.join('db', 'muggledb.sqlite')
    print(os.path.join(db_folder, rel_folder))
    DBSessionFactory.global_init(os.path.join(db_folder, rel_folder))

class Wrapper():
    pass
