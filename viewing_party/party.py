# ------------- WAVE 1 --------------------

from multiprocessing.sharedctypes import Value
from re import I

from tests.test_constants import GENRE_1, MOVIE_TITLE_1, RATING_1


def create_movie(title, genre, rating):
    
    new_movie = {}
    if title and genre and rating:
        new_movie = {
            "title" : title,
            "genre" : genre,
            "rating" : rating
        }
        return new_movie
    return None

def add_to_watched(user_data, movie):
    user_data = {"watched" : [movie]}
    return user_data

def add_to_watchlist(user_data, movie):
    user_data = {"watchlist" :[movie]}
    return user_data

def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watched"].append(movie)
            user_data["watchlist"].remove(movie)
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    average_rating = 0 
    sum_list = []
    for movie in user_data["watched"]:
        if movie["rating"]:
            sum_list.append(movie["rating"])
        average_rating = sum(sum_list)/len(user_data["watched"])
    return average_rating

    
def get_most_watched_genre(user_data):
    genre_list =[]
    for movie in user_data["watched"]:
        if movie["genre"]:
            genre_list.append(movie["genre"])
            most_popular = max(set(genre_list), key = genre_list.count)
        return most_popular
    return None

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_friends_movies_list(user_data):
    friend_list_movies = []
    for my_dict in user_data["friends"]:
        for friend_movie in my_dict["watched"]:
            if friend_movie not in friend_list_movies:
                friend_list_movies.append(friend_movie )
    return friend_list_movies


def get_unique_watched(user_data):
    unique_list =[]
    user_list_movie = user_data["watched"]
    friend_list_movies = get_friends_movies_list(user_data)

    for movie_dict in user_list_movie:
        if movie_dict not in friend_list_movies:
            unique_list.append(movie_dict)
    return unique_list

def get_friends_unique_watched(user_data):
    friends_unique_list = []
    user_list_movie = user_data["watched"]
    friend_list_movies =get_friends_movies_list(user_data)

    for movie_dict in friend_list_movies:
        if movie_dict not in user_list_movie:
            friends_unique_list.append(movie_dict)
    return friends_unique_list


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------


def get_available_recs(user_data):
    movie_with_subscriptions = []
    friend_list_movie =get_friends_movies_list(user_data)

    for movie in friend_list_movie:
        if movie["host"] in user_data["subscriptions"] and movie not in user_data["watched"]:
                movie_with_subscriptions.append(movie)
    return movie_with_subscriptions

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    most_popular_genre = get_most_watched_genre(user_data)
    friends_movies = get_friends_unique_watched(user_data)
    users_recommended_movie_list = []

    for movie in friends_movies:
        if movie["genre"] is most_popular_genre:
            users_recommended_movie_list.append(movie)
    return users_recommended_movie_list

def get_rec_from_favorites(user_data):
    user_favorites = user_data["favorites"]
    friend_list_movies =get_friends_movies_list(user_data)
    friends_recommended_movie_list = []

    for movie in user_favorites:
        if movie not in friend_list_movies:
            friends_recommended_movie_list.append(movie)
    return friends_recommended_movie_list