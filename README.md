# movie-store-app
This is the repository for a movie store app


## Home Route:
> / or /home for main page.

## Movie Search Routes:
1. Get count of all the movies:
> /movies/total-count"
2. Search movie by title:
> /movies/title/<<string:title>>
3. Search movies by price range:
> /movies/price-range           [params: max_price, min_price]
4. Search movies by director name:
> /movies/directors/<<string:director_name>>
5. Search movies by rating:
> /movies/rated/<<string:rated>>
6. Search movies by purchase date:
> /movies/purchase-date [params: low_date, up_date]

## User Search Routes:
1. Get movies transaction and movie details of movies purchased by a user using the user_id:
> /users/<<int:user_id>>/movies
2. Get movies transaction and movie details of movies purchased by a user using the username:
> /users/<<string:username>>/movies

## Movie Data Editing Routes:
1. Add or delete a movie from the record using 'POST' or 'DELETE' methods 
> /movies [json with 'imdb_id', 'price', 'quantity' required for 'POST'] [json with 'imdb_id' required for 'DELETE']
2. Set quantity of movies:
> /movies/<<string:imdb_id>>/quantity [json with 'quantity' required]
3. Set price of movies:
> /movies/<<string:imdb_id>>/price [json with 'price' required]
4. Set year of movie:
> /movies/<<string:imdb_id>>/year [json with 'year' required]

## External API Routes:
1. Get movie description: 
> /movies/<<int:movie_id>>/description
2. Get movie poster link
> /movies/<<int:movie_id>>/poster

## User Data Editing Routes:
1. Add or delete a user from the record using 'POST' or 'DELETE' methods
> /users [json with 'name' required or 'POST'] [json with 'user_id' required for 'DELETE']
2. Change username:
> /users/<int:user_id>/username [json with 'username' required]

## Transaction Route:
> /movies/transaction [json with 'user_id', 'imdb_id', 'quantity' required]