from random import randint as ri
import string,random

class SerializeMixin:
    """Provides basic serialization and deserialization"""
    delimiter = "|" #delimiter to use when serializing

    def serialize(self):
        """Subclasses should overwrite this but do something similar!"""
        #return self.create_string_for_serialize([])
        pass

    @staticmethod
    def deserialize(encoded):
        """Subclasses should overwrite this but do something similar!"""
        list_of_attributes = SerializeMixin.get_deserialized_list(encoded)
        # construct the specific class using these attributes!
        pass

    def create_string_for_serialize(self,attributes_to_serialize):
        """Given a list of attributes, ensures they are all strings, and returns a list of them"""
        list_of_string = [str(obj) if obj is not None else '' for obj in attributes_to_serialize]
        return SerializeMixin.delimiter.join(list_of_string)
    @staticmethod
    def get_deserialized_list(encoded_string):
        """Given a string, returns a list of strings split by the delimiter. 
            If the element is the empty string replace with None.
        """
        if encoded_string:
            return [val if val else None for val in encoded_string.split(SerializeMixin.delimiter)]
        else:
            pass
        

class Track(SerializeMixin):
    '''Gathers information about a song, such as it's popularity ranking, URL, title, and artist'''

    def __init__(self, title, artist, album):
        '''initializes attributes in the Track class '''
        self.title = title
        self.artist = artist
        self.album = album

        self.popularity = -1
        self.url = None
        self._id = None

    def set_popularity(self, popularity):
        '''takes an int as a parameter, and returns none '''
        self.popularity = popularity

    def __str__(self):
        '''returns the formatted string version of the compiled information in this class'''
        if self.popularity != -1:
            return f"{self.title} has popularity {self.popularity}"
        else:
            return f"{self.title}"

    def set_id(self, iD):
        '''takes a string as a parameter and returns None '''
        self._id = iD

    def get_id(self):
        ''' returns the private attribute self._id so that we can see it'''
        return self._id
    

    def serialize(self):
        """Subclasses should overwrite this but do something similar!"""
        artist_id = self.artist._id if self.artist else ''
        album_id = self.album._id if self.album else ''
        return self.create_string_for_serialize([self._id, self.title, self.popularity, self.url, artist_id, album_id])

    @staticmethod
    def deserialize(encoded):
        """Subclasses should overwrite this but do something similar!"""
        try:
            list_of_attributes = SerializeMixin.get_deserialized_list(encoded)
            # construct the specific class using these attributes!
            artist = Artist(None)
            artist_id = list_of_attributes[-2]
            if None == artist_id:
                artist = None
            else:
                artist._id = artist_id
            album = Album(None, artist)
            album_id = list_of_attributes[-1]
            if None == album_id:
                album = None
            else:
                album._id = album_id
            track = Track(list_of_attributes[1], artist, album)
            track._id = list_of_attributes[0]
            track.popularity = list_of_attributes[2]
            track.url = list_of_attributes[3]
            return track

        except Exception as e:
            print(e)
            return None
        

        

class Album(SerializeMixin):
    '''Gathers and manipulates information about an album like it's release date, title, and artist''' 

    def __init__(self, title, artist):
        '''initializes the attributes in class Album '''
        self.title = title
        self.artist = artist
        self.tracks = []

        self.release_date = None
        self.url = None
        self._id = None

    def add_track(self, trac_k):
        '''takes a track name, artist, and title from class Track as a parameter'''
        self.tracks.append(trac_k)


    def __str__(self):
        '''returns the formatted string version of the compiled information in this class'''
        if self.release_date:
            return f"{self.title} was released {self.release_date}"
        else:
            return f"{self.title} has {len(self.tracks)} tracks"

    
    def set_id(self, iD):
        '''takes a string as a parameter, most likely the song ID '''
        self._id = iD

    def get_id(self):
        ''' returns the private attribute self._id so that we can see it'''
        return self._id

    def set_release_date(self, date):
        '''takes a date as a parameter and sets it as the album's release date'''
        self.release_date = date

    def serialize(self):
        """Subclasses should overwrite this but do something similar!"""
        artist_id = None
        if self.artist != None:
            #print("here",type(self.artist))
            artist_id = self.artist._id
        atts = []
        atts.append(self._id)
        atts.append(self.title) 
        atts.append(self.release_date) 
        atts.append(self.url)
        atts.append(artist_id)
        return self.create_string_for_serialize(atts)

    @staticmethod
    def deserialize(encoded):
        """Subclasses should overwrite this but do something similar!"""
        try:
            list_of_attributes = SerializeMixin.get_deserialized_list(encoded) #split the encoded string
            # construct the specific class using these attributes!
            print(list_of_attributes)
            artist = Artist(None)
            artist_id = list_of_attributes[-1]
            if None == artist_id:
                artist = None
            else:
                artist._id = artist_id

            album = Album(list_of_attributes[1], artist)
            album._id = list_of_attributes[0]
            album.release_date = list_of_attributes[2]
            album.url = list_of_attributes[3]
            #in static method there is no concept of self
            return album

        except Exception as e:
            print("encoding was borked {encoded} error {e}")

        

class Artist(SerializeMixin):
    '''gathers and manipulates information about an artist such as their name and albums that they
    have. ''' 
    def __init__(self, name):
        '''initializes the attributes in class Artist '''
        self.name = name
        self.albums = []

        self.url = None
        self._id = None

    def add_album(self, albu_m):
        '''Takes the Album information from class album and compiles it into a list'''
        self.albums.append(albu_m)

    def __str__(self):
        '''returns the formatted string version of the compiled information in this class'''
        return f"{self.name} has {len(self.albums)} albums"

    def set_id(self, iD):
        '''takes a string as a parameter, most likely the album ID'''
        self._id = iD
    
    def get_id(self):
        ''' returns the private attribute self._id so that we can see it'''
        return self._id

    def serialize(self):
        """Subclasses should overwrite this but do something similar!"""
        return self.create_string_for_serialize([self._id, self.name, self.url])
    
    @staticmethod
    def deserialize(encoded):
        """Subclasses should overwrite this but do something similar!"""
        try:
            list_of_attributes = SerializeMixin.get_deserialized_list(encoded)
            # construct the specific class using these attributes!
            print(list_of_attributes)
            
            a = Artist(list_of_attributes[1])
            a._id = list_of_attributes[0]
            a.url = list_of_attributes[2]
            return a

        except Exception as e:
            print(f"cannot decode {encoded} bc of error {e}")
            return None

if __name__ == "__main__":

    bryson_tiller = Artist("Bryson Tiller")
    bryson_tiller.set_id(ri(1,10000000))
    bryson_tiller._url = "https://"+ ''.join(random.choice(string.ascii_letters) for i in range(ri(5,10)))

    album1 = Album("Trapsoul", bryson_tiller)
    album1.set_id(ri(1,10000000))
    album1._url = "https://"+ ''.join(random.choice(string.ascii_letters) for i in range(ri(5,10)))

    track1 = Track("Don't", bryson_tiller, album1)
    track1.set_id(ri(1,10000000))
    track1._url = "https://"+ ''.join(random.choice(string.ascii_letters) for i in range(ri(5,10)))

    album1.add_track(track1)
    bryson_tiller.add_album(album1)

    drake = Artist("Drake")
    drake.set_id(ri(1,10000000))
    drake._url = "https://"+ ''.join(random.choice(string.ascii_letters) for i in range(ri(5,10)))

    album2 = Album("Take Care", drake)
    album2.set_id(ri(1,10000000))
    album2._url = "https://"+ ''.join(random.choice(string.ascii_letters) for i in range(ri(5,10)))

    track2 = Track("Headlines", drake, album2)
    track2.set_id(ri(1,10000000))
    track2._url = "https://"+ ''.join(random.choice(string.ascii_letters) for i in range(ri(5,10)))

    album2.add_track(track2)
    drake.add_album(album2)

    artists = [bryson_tiller,drake]
    for artist in artists:
        print(artist)
        for i,album in enumerate(artist.albums):
            print(f"\t{i+1}.",album)
            for j, track in enumerate(album.tracks):
                print(f"\t\t{j+1}:",track)

    # Serializing a few things
    print(f"{'Artists':*^30}")
    for artist in artists:
        encoded = artist.serialize()
        print(encoded)
    print(f"{'Albums':*^30}")
    for artist in artists:
        for album in artist.albums:
            encoded = album.serialize()
            print(encoded)
    print(f"{'Tracks':*^30}")
    for artist in artists:
        for album in artist.albums:
            for track in album.tracks:
                encoded = track.serialize()
            print(encoded)
