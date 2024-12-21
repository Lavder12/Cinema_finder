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
                SELECT f.title 
                FROM sakila.film f 
                JOIN sakila.film_category fc ON fc.film_id = f.film_id 
                JOIN sakila.category cat ON fc.category_id = cat.category_id 
                WHERE f.release_year = %s
                ORDER BY RAND()
                LIMIT 10
                """
        self.cursor.execute(query, (year,))
        movies = self.cursor.fetchall()

        # Сохраняем ключевое слово в таблицу search_keywords
        save_keyword_query = """
                    INSERT INTO search_queries (query) VALUES (%s)
                    """
        self.cursor.execute(save_keyword_query, (year,))
        self.connection.commit()  # Сохраняем изменения в базе данных

        return movies

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
        movies = self.cursor.fetchall()

        # Сохраняем ключевое слово в таблицу search_keywords
        save_keyword_query = """
                    INSERT INTO search_queries (query) VALUES (%s)
                    """
        self.cursor.execute(save_keyword_query, (genre,))
        self.connection.commit()  # Сохраняем изменения в базе данных

        return movies

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
        OR LOWER(lg.name) LIKE LOWER(%s)
        ORDER BY RAND()
        LIMIT 10
        """
        # Добавляем подстановочные символы для поиска
        keyword_with_wildcards = f"%{keyword}%"
        # Передаём параметр для каждого %s в запросе
        self.cursor.execute(query, (
        keyword_with_wildcards, keyword_with_wildcards, keyword_with_wildcards, keyword_with_wildcards))
        movies = self.cursor.fetchall()

        # Сохраняем ключевое слово в таблицу search_keywords
        save_keyword_query = """
            INSERT INTO search_queries (query) VALUES (%s)
            """
        self.cursor.execute(save_keyword_query, (keyword,))
        self.connection.commit()  # Сохраняем изменения в базе данных

        return movies


    def search_queries(self):
        query = """
        SELECT query FROM sakila.search_queries
        order by created_at desc
        Limit 10"""
        self.cursor.execute(query)
        return self.cursor.fetchall()


    def search_count(self):
        query = """
        SELECT query, COUNT(*) as order_count
        FROM sakila.search_queries
        GROUP BY query
        order by order_count desc
        limit 5
"""
        self.cursor.execute(query)
        return self.cursor.fetchall()



    def close(self):
        if self.connection.is_connected():
            self.cursor.close()
            self.connection.close()
            print("Соединение с базой данных закрыто")
