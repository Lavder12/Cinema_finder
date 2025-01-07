class Const:
    find_movies_by_year = """
        SELECT f.title 
        FROM sakila.film f 
        JOIN sakila.film_category fc ON fc.film_id = f.film_id 
        JOIN sakila.category cat ON fc.category_id = cat.category_id 
        WHERE f.release_year = %s
        ORDER BY RAND()
        LIMIT 10
                """

    find_movies_by_genre = """
        SELECT f.title, cat.name 
        FROM sakila.film f 
        JOIN sakila.film_category fc ON fc.film_id = f.film_id 
        JOIN sakila.category cat ON fc.category_id = cat.category_id 
        WHERE cat.name = %s
        ORDER BY RAND()
        LIMIT 10
        """

    find_movies_by_keyword = """
        SELECT f.title
        FROM sakila.film f
        JOIN sakila.film_actor fa
        ON f.film_id = fa.film_id
        JOIN sakila.actor ac
        ON fa.actor_id = ac.actor_id
        JOIN sakila.language lg
        ON f.language_id = lg.language_id
        WHERE LOWER(ac.first_name) LIKE LOWER(%s)
        OR LOWER(f.title) LIKE LOWER(%s)
        OR LOWER(ac.last_name) LIKE LOWER(%s)
        OR LOWER(lg.name) LIKE LOWER(%s)
        ORDER BY RAND()
        LIMIT 10
        """

    search_queries = """
        SELECT query_text FROM Vladyslav_Habelko.search_queries
        ORDER BY created_at DESC 
        LIMIT 5"""

    search_count = """
        SELECT query_text, COUNT(*) as order_count
        FROM Vladyslav_Habelko.search_queries
        GROUP BY query_text
        ORDER BY order_count DESC 
        LIMIT 1"""



    save_keyword_query = """
                        INSERT INTO Vladyslav_Habelko.search_queries (query_text) VALUES (%s)
                        """