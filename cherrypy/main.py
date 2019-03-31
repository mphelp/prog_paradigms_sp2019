#!/usr/bin/python

from _movie_database import _movie_database

# web services
if __name__ == '__main__':
    # Testing OO backend
    movie_file = "./dat/movies.dat" 
    users_file = "./dat/users.dat"
    ratings_file = "./dat/ratings.dat"
    mdb = _movie_database()
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

    # Server setup
    dispatcher = cherrypy.dispatch.RoutesDispatcher()

    conf = { 'global': {'server.socket_host':'student04.cse.nd.edu',
                        'server.socket_port':51002},
              '/':{'request.dispatch':dispatcher}}

    ## Controllers:
    moviesController  = MoviesController(mdb)
    usersController   = UsersController(mdb)
    ratingsController = RatingsController(mdb)
    resetController   = ResetController(mdb)
    recommendationsController = RecommendationsController(mdb)

    dispatcher.connect('hellow', '/helloworld/', controller=myController, action='GET_INDEX', conditions=dict(method=['GET']))

    dispatcher.connect('hellowname', '/helloworld/', controller=myController, action='PUT_INDEX', conditions=dict(method=['PUT']))

    ## Start
    cherrypy.config.update(conf)
    app = cherrypy.tree.mount(None, config=conf)
    cherrypy.quickstart(app)

