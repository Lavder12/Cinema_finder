import mysql.connector
from mysql.connector import Error
from Const import Const


class DBManager:
    def __init__(self, dbconfig, db_conf_write):
        self.connection_read = self._connect_to_db(dbconfig, "чтение")
        self.connection_write = self._connect_to_db(db_conf_write, "запись")
        self.cursor_read = self.connection_read.cursor(dictionary=True)
        self.cursor_write = self.connection_write.cursor(dictionary=True)

    def _connect_to_db(self, config, purpose):
        try:
            connection = mysql.connector.connect(**config)
            if connection.is_connected():
                print(f"Успешное подключение к базе данных ({purpose})")
            return connection
        except Error as e:
            print(f"Ошибка подключения к базе данных ({purpose}): {e}")
            raise


    def find_movies_by_year(self, year):

        self.cursor_read.execute(Const.find_movies_by_year, (year,))
        movies = self.cursor_read.fetchall()

        # Сохраняем ключевое слово в таблицу search_keywords

        self.cursor_write.execute(Const.save_keyword_query, (year,))
        self.connection_write.commit()  # Сохраняем изменения в базе данных

        return movies

    def find_movies_by_genre(self, genre):
        self.cursor_read.execute(Const.find_movies_by_genre, (genre,))
        movies = self.cursor_read.fetchall()

        # Сохраняем ключевое слово в таблицу search_keywords
        self.cursor_write.execute(Const.save_keyword_query, (genre,))
        self.connection_write.commit()  # Сохраняем изменения в базе данных

        return movies

    def find_movies_by_keyword(self, keyword):

        # Добавляем подстановочные символы для поиска
        keyword_with_wildcards = f"%{keyword}%"
        # Передаём параметр для каждого %s в запросе
        self.cursor_read.execute(Const.find_movies_by_keyword, (
        keyword_with_wildcards,keyword_with_wildcards, keyword_with_wildcards, keyword_with_wildcards))
        movies = self.cursor_read.fetchall()

        # Сохраняем ключевое слово в таблицу search_keywords

        self.cursor_write.execute(Const.save_keyword_query, (keyword,))
        self.connection_write.commit()  # Сохраняем изменения в базе данных

        return movies


    def search_queries(self):
        self.cursor_write.execute(Const.search_queries)
        return self.cursor_write.fetchall()


    def search_count(self):
        self.cursor_write.execute(Const.search_count)
        return self.cursor_write.fetchall()

    def close(self):
        self._close_connection(self.connection_read, "чтение")
        self._close_connection(self.connection_write, "запись")

    def _close_connection(self, connection, purpose):
        if connection.is_connected():
            connection.close()
            print(f"Соединение с базой данных ({purpose}) закрыто")