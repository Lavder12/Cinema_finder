import mysql.connector
from mysql.connector import Error

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
        query = """
                SELECT f.title, cat.name 
                FROM sakila.film f 
                JOIN sakila.film_category fc ON fc.film_id = f.film_id 
                JOIN sakila.category cat ON fc.category_id = cat.category_id 
                WHERE f.release_year = %s
                ORDER BY RAND()
                LIMIT 10
                """
        self.cursor.execute(query, (year,))
        return self.cursor.fetchall()

    def find_movies_by_genre(self, genre):
        query = """
        SELECT f.title, cat.name 
        FROM sakila.film f 
        JOIN sakila.film_category fc ON fc.film_id = f.film_id 
        JOIN sakila.category cat ON fc.category_id = cat.category_id 
        WHERE cat.name = %s
        ORDER BY RAND()
        LIMIT 10
        """
        self.cursor.execute(query, (genre,))
        return self.cursor.fetchall()

    def find_movies_by_keyword(self, keyword): ## Задача выполняется исправно!
        query = """
        SELECT title 
        FROM sakila.film_text
        WHERE LOWER(film_text.description) LIKE LOWER(%s)
        ORDER BY RAND()
        LIMIT 10
        """
        # Добавляем подстановочные символы для поиска
        keyword_with_wildcards = f"%{keyword}%"
        self.cursor.execute(query, (keyword_with_wildcards,))
        return self.cursor.fetchall()

    # def find_movies_by_genre(self, genre):
    #     pass


























    def close(self):
        if self.connection.is_connected():
            self.cursor.close()
            self.connection.close()
            print("Соединение с базой данных закрыто")
