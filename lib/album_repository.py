from lib.album import Album

class AlbumRepository:
    def __init__(self, connection):
        self._connection = connection


    def all(self):
        # Return a list of Album objects from the db
        rows = self._connection.execute('SELECT * from albums')
        albums = []
        for row in rows:
            item = Album(row["id"], row["title"], row["release_year"], row["artist_id"])
            albums.append(item)
        
        return albums