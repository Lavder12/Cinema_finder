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

    def find_movies_by_keyword(self, keyword):
        query = """
        SELECT f.title
        FROM sakila.film f
        JOIN sakila.film_actor fa
        ON f.film_id = fa.film_id
        JOIN sakila.actor ac
        ON fa.actor_id = ac.actor_id
        JOIN sakila.film_text ft
        ON ft.film_id = f.film_id
        JOIN sakila.language lg
        ON f.language_id = lg.language_id
        WHERE LOWER(ft.description) LIKE LOWER(%s)
        OR LOWER(ac.first_name) LIKE LOWER(%s)
        OR LOWER(ac.last_name) LIKE LOWER(%s)
        OR LOWER(lg.name) LIKE LOWER(%s) -- language_id заменён на name, так как language_id — это число
        ORDER BY RAND()
        LIMIT 10
        """
        # Добавляем подстановочные символы для поиска
        keyword_with_wildcards = f"%{keyword}%"
        # Передаём параметр для каждого %s в запросе
        self.cursor.execute(query, (
        keyword_with_wildcards, keyword_with_wildcards, keyword_with_wildcards, keyword_with_wildcards))
        return self.cursor.fetchall()

    def frequently_used_queries(self, queries):
        pass


























    def close(self):
        if self.connection.is_connected():
            self.cursor.close()
            self.connection.close()
            print("Соединение с базой данных закрыто")
