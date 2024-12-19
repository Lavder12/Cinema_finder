from db_manager import DBManager
from UserHand import User

dbconfig = {'host': 'ich-db.ccegls0svc9m.eu-central-1.rds.amazonaws.com',
            'user': 'ich1',
            'password': 'password',
            'database': 'sakila'}

if __name__ == '__main__':
    db_manager = DBManager(dbconfig)
    ui = User(db_manager)

    try:
        ui.start()
    finally:
    # except:
        db_manager.close()
