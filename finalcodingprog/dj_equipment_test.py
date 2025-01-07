import unittest
from unittest import TestCase
from dj_equipment import Artist,Album,Track

# Step 1 TODO Stub your test classes here and hit mark
class TestArtist(TestCase):
    '''I'm gonna write these tests:
    1. test that __str__ returns the correct statement
    2. test the constructor, see that the name and albums instances are set to what was passed
    as parameters
    3. test that the add_album function is actually adding albums to the list and that the album is the 
    correct length
    4. checks that the set_id function is giving the correct value to the parameter'''
    def test_constructor(self):
        '''test the constructor, see that the title and artist instances are set to what was passed
        as parameters'''
        name = "Artist Name"
        a = Artist(name)
        self.assertEqual(a.name, name) 
        self.assertEqual(a._id, None)
               

    def test_str(self):
        '''Checks to see if the string returns the print statement in the correct format'''
        artist = Artist('Kaytranada')

        artist.albums.append("alb1")
        artist.albums.append("alb2")
        artist.albums.append("alb3")

        expected_output = f"{artist.name} has {len(artist.albums)} albums"

        self.assertEqual(str(artist), expected_output), "The string function isn't returning correctly"
         

    def test_add_album(self):
        '''test that the add_album function is actually adding albums to the list and that the album is the 
        correct length'''
        artist_name = 'Bob'
        artist = Artist(artist_name)

        album_title = "A title"
        album = Album(album_title, artist)

        artist.add_album(album)

        self.assertIn(album, artist.albums,f"{album} should have been in list")

        self.assertEqual(1, len(artist.albums), "there should only be one album in the list")
        
        album_title = "Another title"
        artist.add_album(album)
        album = Album(album_title, artist)
        self.assertEqual(2, len(artist.albums), "there should only be two albums in the list")

    def test_set_id(self):
        ''' checks that the set_id function is giving the correct value to the parameter '''
        iD = '0zsw'
        artist = Artist("Beyonce")
        artist._id = iD
        self.assertEqual(artist.set_id(), iD), "The value of iD is not None, check Artist func set_id"

        # TODO implement test_get_id(...) Hint look at test_set_id and reuse!
    def test_get_id(self):
        ''' checks that the get_id function is returning the correct value'''
        iD = '03skf'
        artist = Artist("Steve Lacy")
        artist._id = iD
        self.assertEqual(artist.get_id(), iD), "the value of iD is not none, check Artist func get_id"

class TestAlbum(TestCase):
    '''I'm gonna write these tests:
    1. test that __str__ returns the correct statement
    2. test the constructor, see that the title and artist instances are set to what was passed
    as parameters
    3. test that add track is actually adding tracks to the list, and that the length of the list 
    is correct
    4. test to check that the set_id function is giving the correct value to the parameter'''
    
    def test_constructor(self):
        '''test the constructor, see that the title and artist instances are set to what was passed
        as parameters'''
        title = "GNX"
        artist = "Kendrick Lamar"
        album = Album(title, artist)
        self.assertEqual(album.title, title)
        self.assertEqual(album.artist, artist)
        self.assertEqual(album.tracks, [])
        self.assertEqual(album.release_date, None)
        self.assertEqual(album.url, None)
        self.assertEqual(album._id, None)


    def test_str(self):
        '''test that __str__ returns the correct statement'''
        title = "KOD"
        artist = "J Cole"
        album = Album(title, artist)
        album.release_date = "11/07/2013"
        
        self.assertEqual(str(album),f"{album.title} has 0 tracks")
        expected_output = f"{album.title} was released on {self.release_date}"
        self.assertEqual(str(album.release_date), expected_output), "The string function isn't returning correctly"
        

    def test_add_track(self):
        '''test that add track is actually adding tracks to the list, and that the length of the list 
        is correct'''
        artist_name = 'Bob'
        artist = Artist(artist_name)

        album_title = "A title"
        album = Album(album_title, artist)

        artist.add_album(album)

        self.assertIn(album, artist.albums,f"{album} should have been in list")

        self.assertEqual(1, len(artist.albums), "there should only be one album in the list")
        
        album_title = "Another title"
        artist.add_album(album)
        album = Album(album_title, artist)
        self.assertEqual(2, len(artist.albums), "there should only be two albums in the list")


    def test_set_id(self):
        '''test to check that the set_id function is giving the correct value to the parameter'''
        iD = '3wgs'
        album = Album("Love On Top", "Beyonce")
        album._id= iD
        self.assertEqual(album.set_id(), iD), "The value of iD is not None, check Album func set_id"
    
    def test_get_id(self):
        ''' checks that the get_id function is returning the correct value'''
        iD = '03skf'
        album = Album("The Lo-Fis", "Steve Lacy")
        album._id = iD
        self.assertEqual(album.get_id(), iD), "the value of iD is not none, check Album func get_id"


class TestTrack(TestCase):
    ''''I'm gonna write these tests:
    1. test that __str__ returns the correct statement
    2. test the constructor, see that the title artist, and album instances are set to what was passed
    as parameters
    3. test that the set_popularity function is giving the correct value to the parameter
    4. test to check that the set_id function is giving the correct value to the parameter '''

    def test_constructor(self):
        '''test the constructor, see that the title artist, and album instances are set to what was passed
        as parameters'''
        title = "Amandla's Interlude"
        artist = "Steve Lacy"
        album = "Apollo XXI"
        track = Track(title, artist, album)

        self.assertEqual(track.title, title)
        self.assertEqual(track.artist, artist)
        self.assertEqual(track.album, album)
        self.assertEqual(track.popularity, -1)
        self.assertEqual(track.url, None)
        self.assertEqual(track._id, None)

    def test_str(self):
        '''test that __str__ returns the correct statement'''
        title = "CATFISH"
        artist = "Doechii"
        album = "Alligator Bites Never Heal"
        
        track = Track(title, artist, album)

        track.popularity = 102
        expected_output = f"{track.title} has popularity {track.popularity}"
        self.assertEqual(str(track), expected_output), "The string function isn't returning correctly"

        track2 = Track(title,artist,album)
        self.assertEqual(str(track2),f"{track2.title}")
        
        
    def test_set_id(self):
        '''test to check that the set_id function is giving the correct value to the parameter'''
        iD = '09sk'
        track = Track("Be Here", "Raphael Saadaiq, D'Angelo", "Instant Vintage")
        track._id= iD
        self.assertEqual(track.set_id(), iD), "The value of iD is not None, check Track func set_id"

    def test_get_id(self):
        ''' checks that the get_id function is returning the correct value'''
        iD = '03skf'
        track = Track("Infrunami", "Steve Lacy", "The Lo-Fis")
        track._id = iD
        self.assertEqual(track.get_id(), iD), "the value of iD is not none, check Track func get_id"

    def test_set_popularity(self):
        '''test to check that the set_popularity function is giving the correct value to the parameter '''
        popularity = 2043
        track = Track("War Pigs", "Black Sabbath", "Paranoid")
        track.popularity = popularity
        self.assertEqual(track.popularity, popularity), "The value of popularity is not -1, check Track func set_popularity"

    # TODO implement test_get_id(...) Hint look at previos test_set_id and reuse!

if __name__ == "__main__":
    #unittest.main()
    pass
    
