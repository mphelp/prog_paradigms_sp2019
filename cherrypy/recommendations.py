import cherrypy

# Movies
class RecommendationsController:
    def __init__(self, mdb):
        self.mdb = mdb

    def GET_RECOMMENDATION(self, user_id):
        recommendation = self.mdb.get_recommendation(user_id)
        if recommendation is None:
            return json.dumps({
                "result": "failure"
            })
        else:
            return json.dumps({
                "result": "success",
                "movie_id": recommendation
            })

    def PUT_RECOMMENDATION(self, user_id):
        self.mdb.set_recommendation(user_id)

