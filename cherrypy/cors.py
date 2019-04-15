import cherrypy
import json

# Movies
class CorsController:
    def __init__(self):
        pass

    def GET_OPTIONS(self, uid):
        return ""

    def CORS():
        cherrypy.response.headers["Access-Control-Allow-Origin"] = "*"
        cherrypy.response.headers["Access-Control-Allow-Methods"] = "GET, PUT, POST, OPTIONS, DELETE"

