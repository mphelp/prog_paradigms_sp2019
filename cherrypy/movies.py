import cherrypy
import json

# Movies
class MoviesController:
    def __init__(self, mdb):
        self.mdb = mdb

    def GET_MOVIES(self):
        movies = []
        for movie_id in self.mdb.get_movies():
            movie = self.mdb.get_movie(movie_id)
            if movie is not None:
                movies.append({
                    "genres": movie[1],
                    "title" : movie[0],
                    "result": "success",
                    "id"    : movie_id
                })
        return json.dumps({
            "movies": movies,
            "result": "success"
        })

    def POST_MOVIES(self):
        pass

    def DELETE_MOVIES(self):
        for movie_id in self.mdb.get_movies():
            try:
                self.mdb.delete_movie(movie_id)
            except KeyError:
                pass
        return json.dumps({ "result": "success" })

    def GET_MOVIE(self, movie_id):
        movie_id = int(movie_id)
        movie = self.mdb.get_movie(movie_id)
        if movie is None:
            return json.dumps({ "result": "failure" })
        else:
            return json.dumps({
                "genres": movie[1],
                "title" : movie[0],
                "result": "success",
                "id"    : movie_id
            })

    def PUT_MOVIE(self, movie_id):
        movie = json.loads(str(cherrypy.request.body.read()), 
            encoding='latin-1')
        # Example format of movie:
        # {
        #   'title': 'First Man',
        #   'genres': 'Action|Thriller|Comedy'
        # }
        print(movie)
        self.mdb.set_movie(movie_id, [movie['title'], \
            movie['genres'].split('|')])
