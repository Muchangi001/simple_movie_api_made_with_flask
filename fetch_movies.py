import requests

API_KEY = "" #replace with your actual api key
BASE_URL = "https://api.themoviedb.org"

def fetch_movies(endpoint):
    url = f"{BASE_URL}/{endpoint}?api_key={API_KEY}&language=en-US&page=1"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx, 5xx)
        data = response.json()
        movies = [movie for movie in data.get("results", [])]
        return movies
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return []
        
def fetch_upcoming():
    return fetch_movies("3/movie/upcoming")

def fetch_now_playing():
    return fetch_movies("3/movie/now_playing")
    
def fetch_trending():
    return fetch_movies("3/movie/popular")
    
def fetch_top_rated():
    return fetch_movies("3/movie/top_rated")
