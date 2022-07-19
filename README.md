# Tracking a Movies
A SIMPLE SITE, AN EXAMPLE OF WORKING WITH DJANGO

With this site you can make a list of movies to watch. Available without authorization: viewing the general list of films and directors, as well as pages with detailed information about them.

After registration and authorization, it becomes possible to add favorite films to favorites from the general movie list and indicate their status (want to see, want to see again, completed, haven't seen). If necessary, you can change the status of the movie or remove it from favorites
```sh
import django
```
## Models DB

- Director
    - first_name
    - last_name
    - bio
    - date_of_birth
    - date_of_death


- Film
    - title
    - director
    - summary
    - year
    - genre

- FilmInstance
    - film 
    - viewer

