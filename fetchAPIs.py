import requests

def fetch_upcoming():
    url='https://api.themoviedb.org/3/movie/upcoming?api_key=91a7eeea6e733b77c3e8d9d7c41cc143&language=en-US&page=1'
    response=requests.get(url)
    data=response.json()
    movies=[]
    for movie in data["results"]:
        movies.append(movie)
    return movies

def fetch_now_playing():
    url='https://api.themoviedb.org/3/movie/now_playing?api_key=91a7eeea6e733b77c3e8d9d7c41cc143&language=en-US&page=1'
    response=requests.get(url)
    data=response.json()
    movies=[]
    for movie in data["results"]:
        movies.append(movie)
    return movies
    

def fetch_trending():
    url='https://api.themoviedb.org/3/movie/popular?api_key=91a7eeea6e733b77c3e8d9d7c41cc143&language=en-US&page=1'
    response=requests.get(url)
    data=response.json()
    movies=[]
    for movie in data["results"]:
        movies.append(movie)
    return movies
    

def fetch_top_rated():
    url='https://api.themoviedb.org/3/movie/top_rated?api_key=91a7eeea6e733b77c3e8d9d7c41cc143&language=en-US&page=1'
    response=requests.get(url)
    data=response.json()
    movies=[]
    for movie in data["results"]:
        movies.append(movie)
    return movies
