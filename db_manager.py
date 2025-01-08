import mysql.connector
from mysql.connector import Error
from Const import Const


class DBManager:
    def __init__(self, dbconfig,db_conf_write):
        try:
            self.connection_read = mysql.connector.connect(**dbconfig)

            if self.connection_read.is_connected():
                print("Успешное подключение к базе данных")
                self.cursor_read = self.connection_read.cursor(dictionary=True)
        except Error as e:
            print(f"Ошибка подключения к базе данных: {e}")
            raise

        try:
            self.connection_write = mysql.connector.connect(**db_conf_write)
            if self.connection_write.is_connected():
                print("Успешное подключение к базе данных")
                self.cursor_write = self.connection_write.cursor(dictionary=True)
        except Error as e:
            print(f"Ошибка подключения к базе данных: {e}")
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
        if self.connection_read.is_connected():
            self.cursor_read.close()
            self.connection_read.close()
            print("Соединение с базой данных (чтение) закрыто")

        if self.connection_write.is_connected():
            self.cursor_write.close()
            self.connection_write.close()
            print("Соединение с базой данных (запись) закрыто")