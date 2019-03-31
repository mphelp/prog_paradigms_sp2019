import cherrypy

# Movies
class MoviesController:
    def __init__(self, mdb):
        self.mdb = mdb

    def GET_MOVIES(self):

