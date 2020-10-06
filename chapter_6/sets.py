song_library = [
    ("Phantom Of The Opera", "Sarah Brightman"),
    ("knocking On The Heaven's Door", "Guns N' Roses"),
    ("Captain Nemo", "Sarah Brightman"),
    ("Patterns In The Ivy", "Opeth"),
    ("November Rain", "Guns N' Roses"),
    ("Beautiful", "Sarah Brightman"),
    ("Mal's Song", "Vixy and Tony"),
]

artists = set()
for song, artists in song_library:
    artists.add(artists)

print(artists)

"Opeth" in artists

for artist in artists:
    print("{} plays good music".format(artist))


alphabetical = list(artists)
alphabetical.sort()
alphabetical  # ["Guns N' Roses", 'Opeth', 'Sarah Brightman', 'Vixy and Tony']
