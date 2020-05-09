# Return to your first homework assignments, when you described your favorite song.
# Refactor that code so all the variables are held as dictionary keys and value. 
# Then refactor your print statements so that it's a single loop
# that passes through each item in the dictionary and prints out it's key and then it's value.
FavoriteSong = {
    "Song":"Wake Up", 
    "Artist": "Arcade Fire", 
    "Album": "funeral", 
    "Year": "2004",
    "Genre": "alternative"
    }

for key in FavoriteSong:
    print("{0:s}: \"{1:s}\"".format(key, FavoriteSong[key]))
