import cherrypy
import json

# Movies
class RatingsController:
    def __init__(self, mdb):
        self.mdb = mdb

    def GET_RATING(self, movie_id):
        rating = self.get_rating(mid)
        return json.dumps({
            "rating": rating,
            "movie_id": movie_id,
            "result": "success"
        })
