
from lib.album_repository import AlbumRepository
from lib.artist_repository import ArtistRepository
from lib.database_connection import DatabaseConnection

class Application():
    def __init__(self):
        self._connection = DatabaseConnection()
        self._connection.connect()
        self._connection.seed("seeds/music_library.sql")

    def get_all_artists(self):
        artist_repository = ArtistRepository(self._connection)
        artists = artist_repository.all()
        return [(artist.id, artist.name) for artist in artists]

    def get_all_albums(self):
        album_repository = AlbumRepository(self._connection)
        albums = album_repository.all()
        return [(album.id, album.title) for album in albums]

    def run(self):
        print("What would you like to do?\n  1 - List all albums\n  2 - List all artists\n")
        choice = input('Enter you choice: ').strip()
        if choice == '1':
            data, choice = self.get_all_albums(), 'albums'
        elif choice == '2':
            data, choice = self.get_all_artists(), 'artists'
        else:
            print("\nInvalid choice\n")
            return False
        
        print(f"\nHere is the list of {choice}:")
        print('  * ' + '\n  * '.join(f"{entry[0]} - {entry[1]}" for entry in data))
        return True


if __name__ == '__main__':
    app = Application()
    while not app.run():
        app.run()
