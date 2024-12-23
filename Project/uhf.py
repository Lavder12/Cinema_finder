# from db_manager import DBManager
# from UserHand import User
#
#
# class UHF:
#     def __init__(self, db_manager):
#         self.db_manager = db_manager
#
#     def command_1(self):
#         keyword = input('Введите ключевое слово: ').lower()
#         movies = self.db_manager.find_movies_by_keyword(keyword)
#         print("Результат поиска: ")
#         for movie in movies:
#             print(f"- {movie['title']}")