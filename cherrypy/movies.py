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
            image = self.mdb.get_image(movie_id)
            if movie is not None and image is not None:
                movies.append({
                    "genres": movie[1],
                    "title" : movie[0],
                    "result": "success",
                    "id"    : movie_id,
                    "img"   : image
                })
        return json.dumps({
            "movies": movies,
            "result": "success"
        })

    def POST_MOVIES(self):
        movie = json.loads(str(cherrypy.request.body.read()),
            encoding='latin-1')
        # Example format of movie:
        # {
        #   'title': 'First Man',
        #   'genres': 'Action|Thriller|Comedy'
        # }
        try:
            new_movie_id = max(self.mdb.get_movies()) + 1
            self.mdb.set_movie(new_movie_id, [movie['title'], \
                movie['genres'].split('|')])
            return json.dumps({ "result": "success", "id": new_movie_id })
        except Exception:
            return json.dumps({ "result": "error" })

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
        image = self.mdb.get_image(movie_id)
        if movie is None or image is None:
            return json.dumps({ "result": "error" })
        else:
            return json.dumps({
                "genres": movie[1],
                "title" : movie[0],
                "result": "success",
                "id"    : movie_id,
                "img"   : image,
            })

    def PUT_MOVIE(self, movie_id):
        movie = json.loads((cherrypy.request.body.read()), \
            encoding='latin-1')
        # Example format of movie:
        # {
        #   'title': 'First Man',
        #   'genres': 'Action|Thriller|Comedy'
        # }
        try:
            self.mdb.set_movie(movie_id, [movie['title'], \
                movie['genres'].split('|')])
            return json.dumps({ "result": "success" })
        except Exception as e:
            return json.dumps({ 
								"result": "error",
								"msg": str(e)
			 			})


    def DELETE_MOVIE(self, movie_id):
        try:
            self.mdb.delete_movie(movie_id)
            return json.dumps({ "result": "success" })
        except KeyError:
            return json.dumps({ "result": "error" })

