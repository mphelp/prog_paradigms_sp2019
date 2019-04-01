import cherrypy

# Movies
class MoviesController:
    def __init__(self, mdb):
        self.mdb = mdb

    def GET_MOVIES(self):
        pass

    def GET_MOVIE(self, movie_id):
        movie_id = int(movie_id)
        title, genres = self.mdb.get_movie(movie_id)
        if title is None or genres is None:
            return json.dumps({ "result": "failure" })
        else:
            d = {
                "genres": genres,
                "title" : title,
                "result": "success",
                "id"    : movie_id
            }
            return json.dumps(d)

