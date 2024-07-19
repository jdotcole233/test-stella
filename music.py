"""
- Name
- Genre
- Bio
- Number of songs
"""

class Artiste:
  def __init__(self, name, genre, bio, numberOfSongs):
    self.name = name
    self.genre = genre
    self.bio = bio
    self.numberOfSongs = numberOfSongs
    self.listOfSongs = []


  def addSong (self, song):
    self.listOfSongs.append(song)



"""
- Title song
- duration
- description
"""

class Song:
  """
    title
    duration - duration should be specified in seconds
  """
  def __init__ (self, title, duration, description):
    self.title = title
    self.duration = duration
    self.description = description

  def convertDurationToMinutes (self):
    return self.duration / 60



artiste1 = Artiste("Enoch Nuertey", "Hip Hop", "Great Musician", 5)
song1 = Song("Happiness", 360, "Great song")
song2 = Song("Joy", 180, "Great song")
song3 = Song("Food", 240, "Great song")
song4 = Song("More Money", 240, "Great song")

artiste1.addSong(song1)
artiste1.addSong(song2)
artiste1.addSong(song3)
artiste1.addSong(song4)

artiste2 = Artiste("Richard Lamptey", "Gospel", "Awesome musician", 7)


print(f'Artiste Name: {artiste1.name}\nArtiste Genre: {artiste1.genre}')

print(f"List of {artiste1.name}'s songs:")
for song in artiste1.listOfSongs:
  print(song.title)

print("End of song list\n")


print(f'Artiste Name: {artiste2.name}\nArtiste Genre: {artiste2.genre}')

songs = artiste2.listOfSongs

if len(songs) > 0:
  print(f"List of {artiste2.name}'s songs:")
  for song in artiste2.listOfSongs:
    print(song.title)

  print("End of song list\n")
else:
  print(f"Found no songs for {artiste2.name}")

