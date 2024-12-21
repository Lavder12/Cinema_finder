import mysql.connector
from mysql.connector import Error
from Const import Const


class DBManager:
    def __init__(self, dbconfig):
        try:
            self.connection = mysql.connector.connect(**dbconfig)
            if self.connection.is_connected():
                print("Успешное подключение к базе данных")
                self.cursor = self.connection.cursor(dictionary=True)
        except Error as e:
            print(f"Ошибка подключения к базе данных: {e}")
            raise

    def find_movies_by_year(self, year):

        self.cursor.execute(Const.find_movies_by_year, (year,))
        movies = self.cursor.fetchall()

        # Сохраняем ключевое слово в таблицу search_keywords

        self.cursor.execute(Const.save_keyword_query, (year,))
        self.connection.commit()  # Сохраняем изменения в базе данных

        return movies

    def find_movies_by_genre(self, genre):
        self.cursor.execute(Const.find_movies_by_genre, (genre,))
        movies = self.cursor.fetchall()

        # Сохраняем ключевое слово в таблицу search_keywords
        self.cursor.execute(Const.save_keyword_query, (genre,))
        self.connection.commit()  # Сохраняем изменения в базе данных

        return movies

    def find_movies_by_keyword(self, keyword):

        # Добавляем подстановочные символы для поиска
        keyword_with_wildcards = f"%{keyword}%"
        # Передаём параметр для каждого %s в запросе
        self.cursor.execute(Const.find_movies_by_keyword, (
        keyword_with_wildcards, keyword_with_wildcards, keyword_with_wildcards, keyword_with_wildcards))
        movies = self.cursor.fetchall()

        # Сохраняем ключевое слово в таблицу search_keywords

        self.cursor.execute(Const.save_keyword_query, (keyword,))
        self.connection.commit()  # Сохраняем изменения в базе данных

        return movies


    def search_queries(self):
        self.cursor.execute(Const.search_queries)
        return self.cursor.fetchall()


    def search_count(self):
        self.cursor.execute(Const.search_count)
        return self.cursor.fetchall()



    def close(self):
        if self.connection.is_connected():
            self.cursor.close()
            self.connection.close()
            print("Соединение с базой данных закрыто")
