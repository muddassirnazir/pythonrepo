import media

toy_story = media.Movie("Toy Story", "A Story of a boy and his toys that come to life", "https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg", "https://www.youtube.com/watch?v=KYz2wyBy3kc")
print (toy_story.storyline)
toy_story.show_trailer()

avatar = media.Movie("Avatar", "A Marine on an Alien Planet", "https://en.wikipedia.org/wiki/Avatar_(2009_film)#/media/File:Avatar-Teaser-Poster.jpg", "https://www.youtube.com/watch?v=5PSNL1qE6VY")
print (avatar.storyline)
avatar.show_trailer()

godfather = media.Movie("The Godfather", "A story of power, family and revenge", "https://en.wikipedia.org/wiki/The_Godfather#/media/File:Godfather_ver1.jpg", "https://www.youtube.com/watch?v=sY1S34973zA")
print (godfather.storyline)
godfather.show_trailer()
