import webbrowser

#Creating a class (movie) and using a initilizing function
class Movie():
	def __init__(self, movie_title, poster_image, trailer_youtube):
		self.title = movie_title
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
		
#show trailer opens a youtube video using the url and the webbrowser feature
	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)
