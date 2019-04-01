#!/usr/bin/python

import cherrypy

from _movie_database import _movie_database
from movies import MoviesController
from users import UsersController
from ratings import RatingsController
from reset import ResetController
from recommendations import RecommendationsController

# web services
if __name__ == '__main__':
    # Backend setup
    movie_file = "./dat/movies.dat" 
    users_file = "./dat/users.dat"
    ratings_file = "./dat/ratings.dat"
    mdb = _movie_database(movie_file, users_file, ratings_file)

    # Server setup
    dispatcher = cherrypy.dispatch.RoutesDispatcher()

    # studentconf = { 'global': {'server.socket_host':'student04.cse.nd.edu',
    #                     'server.socket_port':51043},
    #           '/':{'request.dispatch':dispatcher}}
    conf = { 'global': {'server.socket_host':'localhost',
                        'server.socket_port':51043},
              '/':{'request.dispatch':dispatcher}}


    ## Controllers:
    moviesController  = MoviesController(mdb)
    usersController   = UsersController(mdb)
    ratingsController = RatingsController(mdb)
    resetController   = ResetController(mdb)
    recommendationsController = RecommendationsController(mdb)

    dispatcher.connect('movieG', '/movies/:movie_id', controller=moviesController, 
        action='GET_MOVIE', conditions=dict(method=['GET']))

    # dispatcher.connect('hellowname', '/helloworld/', controller=myController, action='PUT_INDEX', conditions=dict(method=['PUT']))

    ## Start
    cherrypy.config.update(conf)
    app = cherrypy.tree.mount(None, config=conf)
    cherrypy.quickstart(app)

# PREVIOUS TESTS:
## Testing movies:
    # mdb.load_movies(movie_file)
    # mdb.set_movie(5000, ['James at the Laundromat', ['Action', 'Thriller']])
    # for i in mdb.get_movies():
    #     mdb.print_movie(i)
    # mdb.delete_movie(5000)
    # mdb.print_movie(5000)

    ## Testing users:
    # mdb.load_users(users_file)
    # mdb.set_user(9999, ['M', 20, 999, 99999])
    # for i in mdb.get_users():
    #     mdb.print_user(i)
    # mdb.delete_user(9999)
    # mdb.print_user(9999)

    ## Testing ratings:
    # mdb.load_ratings(ratings_file)
    # mdb.delete_all_ratings()
    # print(mdb.ratings)

