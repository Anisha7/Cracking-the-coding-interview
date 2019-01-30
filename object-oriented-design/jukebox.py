#  Jukebox: Design a musical jukebox using object-oriented principles.

class jukebox(object):
    def __init__(self, music=[]):
        self.music = music

    def addSong(self, song):
        self.music.append(song)
    
    def removeSong(self, song):
        # remove song

    