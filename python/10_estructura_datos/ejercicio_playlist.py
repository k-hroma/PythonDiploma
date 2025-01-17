playlist = []
number_songs = int(input("Ingrese cantidad de canciones a agregar a la lista: "))

for x in range(1, number_songs + 1):
    songs = input("Ingrese titulo de la cancion: ")
    playslit = playlist.append(songs)

playlist.sort()

for song in playlist:
    print(song)
