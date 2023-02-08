# Open (create) a file:
album_songs = open("dusk_and_Her_Embrace.md", mode="w")


# Using write:
album_songs.write("Humana Inspired to Nightmare\n")
album_songs.write("Heaven Torn Asunder\n")
album_songs.write("Funeral in Carpathia\n")
album_songs.write("A Gothic Romance (Red Roses for the Devil's Whore)\n")
album_songs.write("Malice Through the Looking Glass\n")


# Using print:
print("Dusk and Her Embrace", file=album_songs)


# Using ligt
last_songs = ["The Graveyard by Moonlight\n", "Beauty Slept in Sodom\n", "Haunted Shores\n"]
album_songs.writelines(last_songs)


album_songs.close()


# Read a file:
list_songs = open("dusk_and_Her_Embrace.md", mode="r")
print(list_songs.read())
list_songs.close()


# Using iteration
list_songs = open("dusk_and_Her_Embrace.md", mode="r")
for index, song in enumerate(list_songs):
    print(f"{index + 1} - {song}")
list_songs.close()