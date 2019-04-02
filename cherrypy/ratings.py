import cherrypy
import json

# Movies
class RatingsController:
    def __init__(self, mdb):
        self.mdb = mdb

    def GET_RATING(self, movie_id):
        movie_id = int(movie_id)
        rating = self.mdb.get_rating(movie_id)
        if rating is None:
            return json.dumps({
                "result": "failure"
            })
        else:
            return json.dumps({
                "rating": rating,
                "movie_id": movie_id,
                "result": "success"
            })
