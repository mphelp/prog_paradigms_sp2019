import cherrypy

# Movies
class MoviesController:
    def __init__(self, mdb):
        self.mdb = mdb

    def GET_MOVIES(self):
        pass

    def GET_MOVIE(self, movie_id)
        movie_id = int(movie_id)

