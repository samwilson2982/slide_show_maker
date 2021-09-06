from src.managers import MovieManager

class AppController(object):
    def __init__(self):
        try:
            manager = MovieManager()
        except Exception as e:
            print("minor error :)")
            print(str(e))