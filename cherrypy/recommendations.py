import cherrypy
import json

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
        recommendation = json.loads(cherrypy.request.body.read())
        print(recommendation)
        self.mdb.set_recommendation(recommendation['movie_id'], \
            user_id, recommendation['rating'])
        return json.dumps({
            "result": "success"
        })

    def DELETE_RECOMMENDATIONS(self):
        self.mdb.delete_recommendations()
        return json.dumps({
            "result": "success"
        })

