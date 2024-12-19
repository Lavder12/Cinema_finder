class UserInterface:
    def __init__(self):
        self.db = Database()

    def display_movies_by_genre(self, genre):
        query = """
            SELECT m.title, m.release_year, g.name AS genre
            FROM movies m
            JOIN genres g ON m.genre_id = g.id
            WHERE g.name = ?
        """
        movies = self.db.fetchall(query, (genre,))
        for movie in movies:
            print(f"Title: {movie[0]}, Year: {movie[1]}, Genre: {movie[2]}")

    def display_movies_by_year(self, year):
        query = """
            SELECT title, release_year, rating
            FROM movies
            WHERE release_year = ?
        """
        movies = self.db.fetchall(query, (year,))
        for movie in movies:
            print(f"Title: {movie[0]}, Year: {movie[1]}, Rating: {movie[2]}")

    def display_popular_keywords(self):
        query = """
            SELECT keyword, search_count
            FROM search_keywords
            ORDER BY search_count DESC
        """
        keywords = self.db.fetchall(query)
        for keyword in keywords:
            print(f"Keyword: {keyword[0]}, Search Count: {keyword[1]}")

    def save_search_keyword(self, keyword):
        query = """
            INSERT INTO search_keywords (keyword)
            SELECT ? 
            WHERE NOT EXISTS (SELECT 1 FROM search_keywords WHERE keyword = ?)
        """
        self.db.execute_query(query, (keyword, keyword))

