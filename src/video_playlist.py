"""A video playlist class."""


class Playlist:
    """A class used to represent a Playlist."""
    def __init__(self, name):
        self.name = name
        self.videos = []
    
    def clear(self):
        self.videos.clear()
        
    def remove(self, video):
        if video in self.videos:
            self.videos.remove(video)
            return True
        else:
            return False
        
    def add(self, video):
        if video in self.videos:
            return False
        else:
            self.videos.append(video)
            return True
    
    def get_videos(self):
        return self.videos