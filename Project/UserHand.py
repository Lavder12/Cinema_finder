class User:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def start(self):
        while True:
            print('\nКоманды')
            print('1. Поиск по ключевому слову') ## Готово
            print('2. Поиск по жанру или году выпуска фильма') ## Готово
            print('3. Список самых популярных запросов')
            print('Выход')
            print()


            commands = input('Введите ваш запрос!')

            if commands == '1':
                keyword = input('Введите ключевое слово: ').lower()
                movies = self.db_manager.find_movies_by_keyword(keyword)
                print("Результат поиска: ")
                for movie in movies:
                    print(f"- {movie['title']}")

            elif commands == '2':
                genre_or_year = input('Жанр/Год ').lower()
                if genre_or_year == 'жанр':
                    genre = input('Введите Жанр: ')
                    movies = self.db_manager.find_movies_by_genre(genre)
                    print("Фильмы:")
                    for movie in movies:
                        print(f"- {movie['title']}")
                elif genre_or_year == 'год':
                    year = input('Введите Год: ')
                    movies = self.db_manager.find_movies_by_year(year)
                    print("Фильмы:")
                    for movie in movies:
                        print(f"- {movie['title']} ---- {movie['name']}")

            elif commands == '3':
                pass

