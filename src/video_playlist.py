"""A video playlist class."""


class Playlist:
    """A class used to represent a Playlist."""
    def __init__(self, playlist_name):
        self._playlist_name = playlist_name
        self._videos = []
    
    def clear(self):
        """Clears the playlist."""
        self._videos.clear()
        
    def remove(self, video):
        """
        Tries to remove a video from a playlist.
        Returns if it succeeds.

        Args:
            video: The video_id to be played.
        """         
        if video in self._videos:
            self._videos.remove(video)
            return True
        else:
            return False
        
    def add(self, video):
        """
        Tries to add a video to a playlist.
        Returns if it succeeds.

        Args:
            video: The video_id to be played.
        """         
        if video in self._videos:
            return False
        else:
            self._videos.append(video)
            return True
    
    @property
    def videos(self):
        """Returns the videos in the playlist."""         
        return self._videos
    
    @property
    def name(self) -> str:
        """Returns the title of a video."""
        return self._playlist_name