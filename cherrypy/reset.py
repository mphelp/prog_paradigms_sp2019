import cherrypy

# Movies
class ResetController:
    def __init__(self, mdb):
        self.mdb = mdb

    def PUT_RESET_ALL(self):
        self.mdb.reset_all()

    def PUT_RESET_MOVIE(self, movie_id):
        self.mdb.reset_movie(movie_id)

