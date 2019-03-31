import cherrypy

# Movies
class ResetController:
    def __init__(self, mdb):
        self.mdb = mdb

