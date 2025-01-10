class User:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def show_menu(self):
        print('\nКоманды:')
        print('1. Поиск по ключевому слову')
        print('2. Поиск по жанру или году выпуска фильма')
        print('3. Список самых популярных запросов')
        print('q. Выход')
        print()

    def search_by_keyword(self):
        keyword = input('Введите ключевое слово: ').lower()
        movies = self.db_manager.find_movies_by_keyword(keyword)
        print("Результат поиска: ")
        self.print_movie_titles(movies)

    def search_by_genre_or_year(self):
        print('1. Жанр')
        print('2. Год')
        genre_or_year = input('Выберите вариант: ').lower()

        if genre_or_year == '1':
            genre = input('Введите Жанр: ')
            movies = self.db_manager.find_movies_by_genre(genre)
            print("Фильмы по жанру:")
            self.print_movie_titles(movies)
        elif genre_or_year == '2':
            year = input('Введите Год: ')
            movies = self.db_manager.find_movies_by_year(year)
            print("Фильмы по году:")
            self.print_movie_titles(movies)

    def search_popular_queries(self):
        print('1. Вывести последние 5 запросов')
        print('2. Вывести самый популярный запрос')
        change = input('Выберите нужный вариант: ')

        if change == '1':
            queries = self.db_manager.search_queries()
            self.print_queries(queries)
        elif change == '2':
            queries = self.db_manager.search_count()
            self.print_queries(queries)

    def print_movie_titles(self, movies): ## Обьеденить с print_queries
        if not movies:
            print("Нет результатов.")
        else:
            for movie in movies:
                print(f"- {movie['title']}")

    def print_queries(self, queries):
        if not queries:
            print("Нет популярных запросов.")
        else:
            for query in queries:
                print(query['query_text'])

    def start(self):
        while True:
            self.show_menu()
            command = input('Введите ваш запрос: ').strip().lower()

            if command == '1':
                self.search_by_keyword()
            elif command == '2':
                self.search_by_genre_or_year()
            elif command == '3':
                self.search_popular_queries()
            elif command == 'q':
                break
            else:
                print("Неизвестная команда, попробуйте снова.")
