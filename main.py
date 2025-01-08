import os
from db_manager import DBManager
from UserHand import User
import dotenv

def db_config():
    dotenv.load_dotenv()

    dbconfig = {'host': os.environ.get('host_read'),
            'user': os.environ.get('user_read'),
            'password': os.environ.get('password_read'),
            'database': 'sakila'}
    return dbconfig

def db_conf_write():
    dotenv.load_dotenv()
    dbconfig = {'host': os.environ.get('host_write'),
                'user': os.environ.get('user_write'),
                'password': os.environ.get('password_write'),
                'database': 'Vladyslav_Habelko'}
    return dbconfig


if __name__ == '__main__':
    dbconf = db_config()
    db_conf_write = db_conf_write()
    db_manager = DBManager(dbconf, db_conf_write)
    ui = User(db_manager)

    try:
        ui.start()
    finally:
    # except:
        db_manager.close()