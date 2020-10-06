first_artists = {"Sarah Brightman", "Guns N' Roses", "Opeth", "Vixy and Tony"}
second_artists = {"Nickelback", "Guns N' Roses", "Opeth", "Vixy and Tony"}

print("All: {}".format(first_artists.union(second_artists)))  # All: {'Sarah Brightman', "Guns N' Roses",
# 'Vixy and Tony', 'Savage Garden', 'Opeth', 'Nickelback'}
print("Both: {}".format(second_artists.intersection(first_artists)))  # Both: {"Guns N' Roses"}
print("Either but not both: {}".format(
        first_artists.symmetric_difference(second_artists)))
# Either but not both: {'Savage Garden', 'Opeth', 'Nickelback', 'Sarah Brightman', 'Vixy and Tony'}


bands = {"Guns N' Roses", "Opeth"}

print("first_artists is to bands:")  # first_artists is to bands:
print("issuperset: {}".format(first_artists.issuperset(bands)))  # issuperset: True
print("issubset: {}".format(first_artists.issubset(bands)))  # issubset: False
print("difference: {}".format(first_artists.difference(bands)))  # difference: {'Sarah Brightman', 'Vixy and Tony'}
print("*"*20)
print("bands is to first_artists:")  # bands is to first_artists:
print("issuperset: {}".format(bands.issuperset(first_artists)))  # issuperset: False
print("issubset: {}".format(bands.issubset(first_artists)))  # issubset: True
print("difference: {}".format(bands.difference(first_artists)))  # difference: set()
