#!/usr/bin/env python3

import cherrypy

from _movie_database import _movie_database
from movies import MoviesController
from users import UsersController
from ratings import RatingsController
from reset import ResetController
from recommendations import RecommendationsController
from cors import CorsController

def CORS():
		cherrypy.response.headers["Access-Control-Allow-Origin"] = "*"
		cherrypy.response.headers["Access-Control-Allow-Methods"] = "GET, PUT, POST, OPTIONS, DELETE"

# web services
if __name__ == '__main__':
    # Backend setup
    movie_file = "./dat/movies.dat" 
    users_file = "./dat/users.dat"
    ratings_file = "./dat/ratings.dat"
    images_file = "./dat/images.dat"
    mdb = _movie_database(movie_file, users_file, ratings_file, images_file)

    dispatcher = cherrypy.dispatch.RoutesDispatcher()
    conf = { 
        'global': {
            'server.socket_host':'student04.cse.nd.edu',
            'server.socket_port':51043
        },
        '/': {
            "request.dispatch": dispatcher, 
            "tools.CORS.on": True
        }
    }

    ## Controllers:
    moviesController  = MoviesController(mdb)

    dispatcher.connect('movieG', '/movies/:movie_id', controller=moviesController, 
        action='GET_MOVIE', conditions=dict(method=['GET']))
    dispatcher.connect('moviePU', '/movies/:movie_id', controller=moviesController, 
        action='PUT_MOVIE', conditions=dict(method=['PUT']))
    dispatcher.connect('movieD', '/movies/:movie_id', controller=moviesController, 
        action='DELETE_MOVIE', conditions=dict(method=['DELETE']))

    dispatcher.connect('moviesG', '/movies/', controller=moviesController, 
        action='GET_MOVIES', conditions=dict(method=['GET']))
    dispatcher.connect('moviesPO', '/movies/', controller=moviesController, 
        action='POST_MOVIES', conditions=dict(method=['POST']))
    dispatcher.connect('moviesD', '/movies/', controller=moviesController, 
        action='DELETE_MOVIES', conditions=dict(method=['DELETE']))

    usersController   = UsersController(mdb)

    dispatcher.connect('userG', '/users/:user_id', controller=usersController, 
        action='GET_USER', conditions=dict(method=['GET']))
    dispatcher.connect('userPU', '/users/:user_id', controller=usersController, 
        action='PUT_USER', conditions=dict(method=['PUT']))
    dispatcher.connect('userD', '/users/:user_id', controller=usersController, 
        action='DELETE_USER', conditions=dict(method=['DELETE']))

    dispatcher.connect('usersG', '/users/', controller=usersController, 
        action='GET_USERS', conditions=dict(method=['GET']))
    dispatcher.connect('usersPO', '/users/', controller=usersController, 
        action='POST_USERS', conditions=dict(method=['POST']))
    dispatcher.connect('usersD', '/users/', controller=usersController, 
        action='DELETE_USERS', conditions=dict(method=['DELETE']))


    ratingsController = RatingsController(mdb)

    dispatcher.connect('ratingG', '/ratings/:movie_id', controller=ratingsController, 
        action='GET_RATING', conditions=dict(method=['GET']))

    recommendationsController = RecommendationsController(mdb)

    dispatcher.connect('recommendationsD', '/recommendations/', controller=recommendationsController, 
        action='DELETE_RECOMMENDATIONS', conditions=dict(method=['DELETE']))
    dispatcher.connect('recommendationPU', '/recommendations/:user_id', controller=recommendationsController, 
        action='PUT_RECOMMENDATION', conditions=dict(method=['PUT']))
    dispatcher.connect('recommendationG', '/recommendations/:user_id', controller=recommendationsController, 
        action='GET_RECOMMENDATION', conditions=dict(method=['GET']))
    
    resetController   = ResetController(mdb)

    dispatcher.connect('resetallP', '/reset/', controller=resetController, 
        action='PUT_RESET_ALL', conditions=dict(method=['PUT']))
    dispatcher.connect('resetP', '/reset/:movie_id', controller=resetController, 
        action='PUT_RESET_MOVIE', conditions=dict(method=['PUT']))

    corsController = CorsController()

    dispatcher.connect('cors', '/recommendations/:uid', controller=corsController, action="GET_OPTIONS", conditions=dict(method=["OPTIONS"]))

    ## Start
    cherrypy.config.update(conf)
    cherrypy.tools.CORS = cherrypy.Tool("before_handler", CORS)
    app = cherrypy.tree.mount(None, config=conf)
    cherrypy.quickstart(app)

