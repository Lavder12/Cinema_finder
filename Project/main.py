import os
from db_manager import DBManager
from UserHand import User


def db_config():
    dbconfig = {'host': os.environ.get('host'),
            'user': os.environ.get('user'),
            'password': os.environ.get('password'),
            'database': 'sakila'}
    return dbconfig

if __name__ == '__main__':
    dbconf = db_config()
    db_manager = DBManager(dbconf)
    ui = User(db_manager)

    try:
        ui.start()
    finally:
    # except:
        db_manager.close()