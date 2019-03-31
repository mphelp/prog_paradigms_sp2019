import sys

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
        if len(movie) != 2 or not isinstance(movie[0], basestring) \
                or not isinstance(movie[1], list) \
                or not isinstance(movie[1][0], basestring):
            raise Exception('database function {} requires '.format(sys._getframe().f_code.co_name) + \
                            'movie\'s title(str) and genre(list(str))')
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

    def get_user(self, uid):
        try:
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
        if len(user) != 4 or not isinstance(user[0], basestring) \
            or not isinstance(user[1], (int, long)) \
            or not isinstance(user[2], (int, long)) \
            or not isinstance(user[3], basestring):
            raise Exception('database function {} requires '.format(sys._getframe().f_code.co_name) + \
                            'user\'s gender(str), age(int), occupationcode(int) and zipcode(str)')
            return

        temp = {
            'gender': user[0],
            'age': user[1],
            'occupationcode': user[2],
            'zipcode': user[3]
        }
        self.users[uid] = temp

    def delete_user(self, uid):
        try:
            del self.users[uid]
        except KeyError:
            pass

    # Ratings
    def load_ratings(self, ratings_file):
        # Format: mid::uid::rating::timestamp
        # Stored: mid  uid  rating
        # Types:  int  int  int
        with open(ratings_file) as f:
            for line in f:
                attr = line.strip().split('::')
                mid = int(attr[0])
                uid = int(attr[1])
                rating = int(attr[2])
                # Set attr
                try:
                    self.ratings[mid][uid] = rating
                except KeyError:
                    self.ratings[mid] = {}
                    self.ratings[mid][uid] = rating


    def print_rating(self, mid, uid):
        try:
            print(self.ratings[mid][uid])
        except KeyError:
            print(None)

    def get_rating(self, mid):
        total = 0
        count = 0
        for uid, rating in self.ratings[mid].iteritems():
            count += 1
            total += rating
        return float(total)/float(count)

    def get_highest_rated_movie(self):
        bestRating = 1
        bestRatedMovie  = None
        for mid in self.movies.keys():
            rating = self.get_rating(mid)
            if rating > bestRating:
                bestRating = rating
                bestRatedMovie = mid
        return bestRatedMovie

            
    # def get_users(self):
    #     # list of mids
    #     return list(self.users.keys())

    # def set_user(self, uid, user):
    #     if len(user) != 4 or not isinstance(user[0], basestring) \
    #         or not isinstance(user[1], (int, long)) \
    #         or not isinstance(user[2], (int, long)) \
    #         or not isinstance(user[3], basestring):
    #         raise Exception('database function {} requires '.format(sys._getframe().f_code.co_name) + \
    #                         'user\'s gender(str), age(int), occupationcode(int) and zipcode(str)')
    #         return

    #     temp = {
    #         'gender': user[0],
    #         'age': user[1],
    #         'occupationcode': user[2],
    #         'zipcode': user[3]
    #     }
    #     self.users[uid] = temp

    # def delete_user(self, uid):
    #     try:
    #         del self.users[uid]
    #     except KeyError:
    #         pass


