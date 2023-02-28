import ipdb

class Song:
    
    
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.count_songs()
        self.add_to_genres(genre)
        self.add_to_artists(artist)
        self.add_to_genre_count(genre)
        self.add_to_artist_count(artist)

       
    @classmethod
    def add_to_genre_count(cls, genre):
        if cls.genre_count.get(genre):
            cls.genre_count[genre] += 1 
        else:
            cls.genre_count[genre] = 1
        



    @classmethod
    def add_to_artist_count(cls, artist):
        if cls.artist_count.get(artist):
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1











    @classmethod
    def count_songs(cls, new_song=1):
        cls.count += new_song

    @classmethod
    def add_to_genres(cls, genre):
        if cls.genres != genre:
            cls.genres.append(genre)
   
    @classmethod
    def add_to_artists(cls, artist):
        if cls.artists != artist:
            cls.artists.append(artist)
            








    # @classmethod
    # def show_genres(self, cls, genre):
    #     if (self.genres == ""):
    #         print("aint no genres")
    #     else:
    #         for _ in range(self.genres):
    #             cls.append(genre)
    #             i += 1
    #             print("ayyy")