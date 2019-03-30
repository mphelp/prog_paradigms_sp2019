#!/usr/bin/python3

from _movie_database import _movie_database

# web services
if __name__ == '__main__':
    # Testing OO backend
    movie_file = "./dat/movies.dat" 
    users_file = "./dat/users.dat"
    mdb = _movie_database()
    ## Testing movies:
    # mdb.load_movies(movie_file)
    # mdb.set_movie(5000, ['James at the Laundromat', ['Action', 'Thriller']])
    # for i in mdb.get_movies():
    #     mdb.print_movie(i)
    # mdb.delete_movie(5000)
    # mdb.print_movie(5000)

    ## Testing users:
    mdb.load_users(users_file)
    mdb.print_user(0)
    mdb.print_user(1)
