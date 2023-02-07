# FOR
cradle_of_filth_albums = [
    {'title': 'Dusk and Her Embrace', 'rate': 86, 'year': 1996},
    {'title': 'Cruelty and the Beast', 'rate': 83, 'year': 1998},
    {'title': 'Darkly, Darkly, Venus Aversa', 'rate': 75, 'year': 2010},
    {'title': 'Hammer of the Witches', 'rate': 92, 'year': 2015},
    {'title': 'Existence Is Futile', 'rate': 82, 'year': 2021}
]


# Best Albums:
best_albums = []
min_rating = 85
for album in cradle_of_filth_albums:
    if album['rate'] > min_rating:
        best_albums.append(album['title'])
print('Best Cradle of Filth albums:', best_albums)


# By number:
for index in range(5):
    print(cradle_of_filth_albums[index]['title'])


# Other way (list comprehension), get new albums:
album_year = 2000
filtred_albums = [album['title']
                  for album in cradle_of_filth_albums
                  if album['year'] > album_year]
print(filtred_albums)


# List comprehension in string:
# check if 'u' exists in albums name
title_names_with_u = [title for title in filtred_albums if 'u' in title]
print(title_names_with_u)


# WHILE:
#Decrease n to 0
n = 6
while n > 0:
    n -= 1
    print(n)


# ENUMERATE:
x = enumerate(filtred_albums)
print(list(x))


# F-STRING:
for album in cradle_of_filth_albums:
    print(f"The album {album['title']} was released in {album['year']}")