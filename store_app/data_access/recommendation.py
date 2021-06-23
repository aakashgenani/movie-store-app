from tables.models import User, Movie
from collections import Counter


def _get_list_of_genres(user_id):
    user = User.query.get(user_id)
    purchases = user.purchases
    imdb_ids = [pur.imdb_id for pur in purchases]
    genres = [Movie.query.filter_by(imdb_id=x).first().genre for x in imdb_ids]
    genres = [genre.split() for genre in genres]
    flat_list = [item for sublist in genres for item in sublist]
    flat_list_wo_comma = [s.replace(',', '') for s in flat_list]
    return flat_list_wo_comma


def _get_most_watched_genres_by_user(user_id):
    list_genres = _get_list_of_genres(user_id)
    dict_w_count = Counter(list_genres)
    sorted_genres = dict(sorted(dict_w_count.items(), key=lambda item: item[1], reverse=True))
    count_list = [sorted_genres[genre] for genre in sorted_genres]
    count_list_top_2 = count_list[0:2]
    genres = [genre for genre in sorted_genres if sorted_genres[genre] == count_list_top_2[0]
              or sorted_genres[genre] == count_list_top_2[1]]
    return genres


def _get_all_movie_by_genres(genres):
    list_movies = list()
    for genre in genres:
        movies = Movie.query.filter(Movie.genre.like(f'%{genre}%')).all()
        for movie in movies:
            if movie not in list_movies:
                list_movies.append(movie.serialize())
    return list_movies


def _get_unique_movies_from_repeated_movies(repeated_movies):
    recommended_movies = list()
    for movie in repeated_movies:
        if movie not in recommended_movies:
            recommended_movies.append(movie)
    return recommended_movies


def recommend_movie(user_id):
    genres = _get_most_watched_genres_by_user(user_id)
    recommended_movies_repeated = _get_all_movie_by_genres(genres)
    recommended_movies = _get_unique_movies_from_repeated_movies(recommended_movies_repeated)
    return recommended_movies
