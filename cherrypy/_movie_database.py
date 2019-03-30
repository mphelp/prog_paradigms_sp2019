# Backend DB
class _movie_database:
    def __init__(self):
        self.movies = dict()
        self.users  = dict()
        self.ratings = dict()

    # Movies
    def load_movies(self, movie_file):
        # Format: mid::title::genre|genre|genre
        # Stored: mid  title  genres
        # Types:  int  str    list of str
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

    def print_movie(self, mid):
        try:
            print(self.movies[mid])
        except KeyError:
            print(None)

    def get_movie(self, mid):
        # genres returned as string not list
        try:
            return [self.movies[mid]['title'], \
                    ' '.join(self.movies[mid]['genres'])]
        except KeyError:
            return None

    def get_movies(self):
        # list of mids
        return list(self.movies.keys())

    def set_movie(self, mid, movie):
        if len(movie) != 2:
            raise Exception('set_movie requires movie title and genre')
            return
        # genres is stored as a list of str currently
        temp = {
            'title': movie[0],
            'genres': movie[1]
        }
        self.movies[mid] = temp

    def delete_movie(self, mid):
        try:
            del self.movies[mid]
        except KeyError:
            pass
    
    # Users
    def load_users(self, users_file):
        # Format: uid::gender::age::occupationcode::zipcode
        # Stored: uid  gender  age  occupationcode  zipcode
        # Types:  int  str     int  int             str
        with open(users_file) as f:
            for line in f:
                attr = line.strip().split('::')
                uid = int(attr[0])
                gender = attr[1]
                age = int(attr[2])
                occupationcode = int(attr[3])
                zipcode = attr[4] # because of zips like XXXXX-XXXX
                # Set attr
                temp = {
                    'gender': gender,
                    'age': age,
                    'occupationcode': occupationcode,
                    'zipcode': zipcode
                }
                self.users[uid] = temp

    def print_user(self, uid):
        try:
            print(self.users[uid])
        except KeyError:
            print(None)


