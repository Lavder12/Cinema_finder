# application.py
import os
import dotenv
from db_manager import DBManager
from user_hand import User

class Application:
    def __init__(self):
        self.dbconf = self.db_config()
        self.db_conf_write = self.db_conf_write()
        self.db_manager = DBManager(self.dbconf, self.db_conf_write)
        self.ui = User(self.db_manager)

    @staticmethod
    def db_config():
        dotenv.load_dotenv()

        dbconfig = {'host': os.environ.get('host_read'),
                    'user': os.environ.get('user_read'),
                    'password': os.environ.get('password_read'),
                    'database': 'sakila'}
        return dbconfig

    @staticmethod
    def db_conf_write():
        dotenv.load_dotenv()
        dbconfig = {'host': os.environ.get('host_write'),
                    'user': os.environ.get('user_write'),
                    'password': os.environ.get('password_write'),
                    'database': 'Vladyslav_Habelko'}
        return dbconfig

    def run(self):
        try:
            # Запуск пользовательского интерфейса
            self.ui.start()
        finally:
            # Закрытие соединения с базой данных
            self.db_manager.close()
