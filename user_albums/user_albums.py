def make_album(album_name, artist):
    """asd"""
    album = {'name': album_name, 'maker': artist}
    return album.title()

while True:
    print("\nPlease write album name:")
    print("(enter 'q' at any time to quit)")
    alb_name = input("Album name: ")
    if alb_name == 'q':
        break
    art_name = input("Artist name: ")
    if art_name == 'q':
        break

album_stuff = make_album(alb_name, art_name)
print({album_stuff})
