
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
                    title: title
                    genres: genres
                }
                self.movies[mid] = temp
        print(self.movies[1])
