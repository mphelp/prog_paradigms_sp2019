
# OO
class _movie_database:
    def __init__(self):
        self.movies = dict()
        self.users  = dict()
        self.ratings = dict()

    def load_movies(self, movie_file):
        # Format: mid::title::genre|genre|genre
        with open(movie_file) as f:
            for line in f:
                attr = line.strip().split('::')
                mid = int(attr[0])
                title = attr[1]
                genres = attr[2].split('|')
                # Set attr
                temp = {
                    'title': title,
                    'genres': genres
                }
                self.movies[mid] = temp
    def get_movie(self, mid):
        try:
            # genres returned as string
            return [self.movies[mid]['title'], \
                    ' '.join(self.movies[mid]['genres'])]
        except KeyError:
            return None
    def get_movies(self):
        # list of mids
        return list(self.movies.keys())
    def print_movie(self, mid):
        try:
            print(self.movies[mid])
        except KeyError:
            print(None)
    def set_movie(self, mid, movie):
        if len(movie) != 2:
            raise Exception('set_movie requires movie title and genre')
            return
        self.print_movie(mid)
        # genres is list currently
        temp = {
            'title': movie[0],
            'genres': movie[1]
        }
        self.movies[mid] = temp
        self.print_movie(mid)
    def delete_movie(self, mid):
        try:
            del self.movies[mid]
        except KeyError:
            pass
    


