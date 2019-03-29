#!/usr/bin/python3

from _movie_database import _movie_database

# web services
if __name__ == '__main__':
    # Testing OO backend
    movie_file = "./dat/movies.dat" 
    mdb = _movie_database()
    mdb.load_movies(movie_file)
