import media
import fresh_tomatoes



about_time = media.Movie("About Time", "https://www.aceshowbiz.com/images/still/about-time-poster02.jpg", "https://www.youtube.com/watch?v=T7A810duHvw")

lady_bird = media.Movie("Lady Bird", "https://images-na.ssl-images-amazon.com/images/I/81prIZTJ9JL._RI_.jpg", "https://www.youtube.com/watch?v=cNi_HC839Wo")

harry_potter = media.Movie("Harry Potter", "https://upload.wikimedia.org/wikipedia/tr/c/c1/Harrypotter1filmposter.jpg" ,"https://www.youtube.com/watch?v=9hXH0Ackz6w")

sound_of_music = media.Movie("Sounds of Music", "https://www.movieguide.org/wp-content/uploads/2012/08/The-Sound-of-Music-movie-poster1.jpg", "https://www.youtube.com/watch?v=lEcKXr3mJ_o")

the_brand_new_testament = media.Movie("The Brand New Testament", "http://images.fandango.com/r98.9/ImageRenderer/1040/650/redesign/areas/movie/moviesubpages/img/noimage_900x900.jpg/187658/images/masterrepository/fandango/187658/thebrandnewtestament.jpg", "https://www.youtube.com/watch?v=Dsh_wFI0uMU")

fight_club = media.Movie("Fight Club", "https://vignette.wikia.nocookie.net/filmguide/images/0/07/Fight-club-poster.jpg/revision/latest?cb=20111208111352", "https://www.youtube.com/watch?v=SUXWAEX2jlg")

#list of movies

movies = [about_time, lady_bird, harry_potter, sound_of_music, the_brand_new_testament, fight_club]

fresh_tomatoes.open_movies_page(movies)
