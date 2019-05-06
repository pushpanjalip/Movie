import Media
import fresh_tomatoes
toy_story = Media.Movie("Toy_Story", "Story of boy and his toys",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://youtu.be/wmiIUN-7qhE")
print(toy_story.storyline)


avatar = Media.Movie("Avatar", "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://youtu.be/6ziBFh3V1aM?t=7")

movies = [toy_story, avatar]

fresh_tomatoes.open_movies_page(movies)
