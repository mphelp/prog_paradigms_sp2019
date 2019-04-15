import sys
from statistics import mean

# Backend DB
# Note: Sometimes, a user method requires the a database dictionary
#       other than user. The same can be said of movie or ratings.
#       Thus, always load all three dat files into the movie database
#       to ensure all three set of methods work properly.
class _movie_database:
    def __init__(self):
        self.movies = dict()
        self.users  = dict()
        self.ratings = dict()

    def __init__(self, movie_file, users_file, ratings_file, images_file):
        self.movies = dict()
        self.users = dict()
        self.ratings = dict()
        self.images = dict()
        self.recommendations = dict()
        self.movie_file = movie_file
        self.users_file = users_file
        self.ratings_file = ratings_file
        self.images_file = images_file
        self.load_movies(movie_file)
        self.load_users(users_file)
        self.load_ratings(ratings_file)
        self.load_images(images_file)

    # Movies
    def load_movies(self, movie_file):
        # Format: mid::title::genre|genre|genre
        # Stored: mid  title  genres
        # Types:  int  str    list of str
        self.movies = {}
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
                mid = int(mid)
                self.movies[mid] = temp

    def print_movie(self, mid):
        try:
            mid = int(mid)
            print(self.movies[mid])
        except KeyError:
            print(None)

    def get_movie(self, mid):
        # genres returned as string not list
        #print("GET: mid {}: {}".format(mid, self.movies[mid]))
        try:
            mid = int(mid)
            return [self.movies[mid]['title'], \
                    '|'.join(self.movies[mid]['genres'])]
        except KeyError:
            return None

    def get_movies(self):
        # list of mids
        return list(self.movies.keys())

    def set_movie(self, mid, movie):
        if not isinstance(movie[0], str) \
                or not isinstance(movie[1], list) \
                or not isinstance(movie[1][0], str):
            raise Exception('database function {} requires '.format(sys._getframe().f_code.co_name) + \
                            'movie\'s title(str) and genre(list(str))')
            return
        # genres is stored as a list of str currently
        temp = {
            'title': movie[0],
            'genres': movie[1]
        }
        mid = int(mid)
        print(temp)
        self.movies[mid] = temp
        print(self.movies[mid])

    def delete_movie(self, mid):
        # account for KeyError in moviesController
        mid = int(mid)
        del self.movies[mid]
    
    # Users
    def load_users(self, users_file):
        # Format: uid::gender::age::occupationcode::zipcode
        # Stored: uid  gender  age  occupationcode  zipcode
        # Types:  int  str     int  int             str
        self.users = {}
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
            uid = int(uid)
            print(self.users[uid])
        except KeyError:
            print(None)

    def get_user(self, uid):
        try:
            uid = int(uid)
            return [self.users[uid]['gender'], \
                    self.users[uid]['age'], \
                    self.users[uid]['occupationcode'], \
                    self.users[uid]['zipcode']]
        except KeyError:
            return None

    def get_users(self):
        # list of mids
        return list(self.users.keys())

    def set_user(self, uid, user):
        #if not isinstance(user[0], str) \
        #    or not isinstance(user[3], str):
        #    raise Exception('database function {} requires '.format(sys._getframe().f_code.co_name) + \
        #                    'user\'s gender(str), age(int), occupationcode(int) and zipcode(str)')
        #    return

        temp = {
            'gender': user[0],
            'age': int(user[1]),
            'occupationcode': int(user[2]),
            'zipcode': user[3]
        }
        uid = int(uid)
        self.users[uid] = temp

    def delete_user(self, uid):
        try:
            uid = int(uid)
            del self.users[uid]
        except KeyError:
            pass

    # Ratings
    # Note: if mid, uid, and rating are ever in func args ...
    #       then order is mid THEN uid!
    def load_ratings(self, ratings_file):
        # Format: uid::mid::rating::timestamp
        # Stored: uid  mid  rating
        # Types:  int  int  int
        self.ratings = {}
        with open(ratings_file) as f:
            for line in f:
                attr = line.strip().split('::')
                uid = int(attr[0])
                mid = int(attr[1])
                rating = int(attr[2])
                # Set attr
                try:
                    self.ratings[uid][mid] = rating
                except KeyError:
                    self.ratings[uid] = {}
                    self.ratings[uid][mid] = rating


    def print_rating(self, mid, uid):
        try:
            mid = int(mid)
            uid = int(uid)
            print(self.ratings[uid][mid])
        except KeyError:
            print(None)

    def get_rating(self, mid):
        mid = int(mid)
        getratings = []
        for uid, midDict in self.ratings.items():
            rating = midDict.get(mid)
            if rating:
                getratings.append(rating)
        if len(getratings):
            return mean(getratings)
        else:
            return 0

    def get_highest_rated_movie(self):
        bestRating = 1
        bestRatedMovie  = None
        for mid in self.movies.keys():
            rating = self.get_rating(mid)
            if rating > bestRating:
                bestRating = rating
                bestRatedMovie = mid
        return bestRatedMovie

    def set_user_movie_rating(self, mid, uid, rating):
        mid = int(mid)
        uid = int(uid)
        rating = int(rating)
        self.ratings[uid][mid] = rating

    def get_user_movie_rating(self, mid, uid):
        try:
            mid = int(mid)
            uid = int(uid)
            rating = self.ratings[uid][mid]
            return rating
        except KeyError:
            return None

    def delete_all_ratings(self):
        del self.ratings
        self.ratings = {}

    # Recommendations

    # Reset
    def reset_all(self):
        del self.movies
        del self.users
        del self.ratings
        self.movies = dict()
        self.users = dict()
        self.ratings = dict()
        self.load_movies(self.movie_file)
        self.load_users(self.users_file)
        self.load_ratings(self.ratings_file)

    def reset_movie(self, mid):
        mid = int(mid)
        with open(movie_file) as f:
            for line in f:
                attr = line.strip().split('::')
                movie_id = int(attr[0])
                if mid == movie_id:
                    title = attr[1]
                    genres = attr[2].split('|')
                    # Set attr
                    self.movies[mid] = {
                        'title': title,
                        'genres': genres
                    }
                    break

    # Images
    def load_images(self, images_file):
        # Format: mid::uid::rating::timestamp
        # Stored: mid  uid  rating
        # Types:  int  int  int
        self.images = {}
        with open(images_file) as f:
            for line in f:
                attr = line.strip().split('::')
                mid = int(attr[0])
                img = attr[2]
                # Set attr
                self.images[mid] = img

    def get_image(self, mid):
        try:
            mid = int(mid)
            return self.images[mid]
        except KeyError:
            return None

    # Recommendations
    def delete_recommendations(self):
        del self.recommendations
        del self.ratings
        self.recommendations = {}
        self.ratings = {}

    def get_recommendation(self, uid):
        uid = int(uid)
        sortedMovies = sorted(self.movies.keys(), key=lambda mid: self.get_rating(mid), reverse=True)
        for mid in sortedMovies:
            if self.get_user_movie_rating(mid, uid) is None:
                return mid
        return None

    def set_recommendation(self, mid, uid, rating):
        try:
            self.set_user_movie_rating(mid, uid, rating)
        except KeyError:
            pass


