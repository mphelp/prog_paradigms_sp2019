#!/usr/bin/python3

from _movie_database import _movie_database

# web services
if __name__ == '__main__':
    # Testing OO backend
    movie_file = "./dat/movies.dat" 
    mdb = _movie_database()
    mdb.load_movies(movie_file)
    mdb.set_movie(5000, ['James at the Laundromat', ['Action', 'Thriller']])
    for i in mdb.get_movies():
        mdb.print_movie(i)
    mdb.delete_movie(5000)
    mdb.print_movie(5000)
