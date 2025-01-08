class User:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def start(self):
        while True:
            print('\nКоманды')
            print('1. Поиск по ключевому слову') ## Готово
            print('2. Поиск по жанру или году выпуска фильма') ## Готово
            print('3. Список самых популярных запросов') ## Готово
            print('Выход') ## Готово
            print()


            commands = input('Введите ваш запрос!')


            if commands == '1':
                keyword = input('Введите ключевое слово: ').lower()
                movies = self.db_manager.find_movies_by_keyword(keyword)
                print("Результат поиска: ")
                for movie in movies:
                    print(f"- {movie['title']}")

            elif commands == '2':
                print('1. Жанр')
                print('2. Год')
                genre_or_year = input('Выберите вариант:  ').lower()
                if genre_or_year == '1':
                    genre = input('Введите Жанр: ')
                    movies = self.db_manager.find_movies_by_genre(genre)
                    print("Фильмы:")
                    for movie in movies:
                        print(f"- {movie['title']}")
                elif genre_or_year == '2':
                    year = input('Введите Год: ')
                    movies = self.db_manager.find_movies_by_year(year)
                    print("Фильмы:")
                    for movie in movies:
                        print(f"- {movie['title']}")

            elif commands == '3':
                print('1. Вывести последние 5 запросов')
                print('2. Вывести самый популярный запрос')
                change = input('Выберите нужный вариант:')
                if change == '1':
                    movies = self.db_manager.search_queries()
                    for movie in movies:
                        print(movie['query_text'])
                elif change == '2':
                    movies = self.db_manager.search_count()
                    for movie in movies:
                        print(movie['query_text'])
            elif commands == 'q':
                break