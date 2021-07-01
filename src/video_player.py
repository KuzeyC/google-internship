"""A video player class."""

from .video_library import VideoLibrary
from .video_playlist import Playlist
import random
import ast

class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self._playlists = {}
        self._currently_playing = None
        self._is_paused = False

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        sorted_videos = sorted(self._video_library.get_all_videos(), key=lambda x: x.title)
        print("Here's a list of all available videos:")
        for video in sorted_videos:
            if video.flag:
                print(f"{video.title} ({video.video_id}) [{' '.join(video.tags)}] - FLAGGED (reason: {video.flag})")
            else:
                print(f"{video.title} ({video.video_id}) [{' '.join(video.tags)}]")

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """            
        for video in self._video_library.get_all_videos():
            if video.video_id == video_id:
                if video.flag:
                    print(f"Cannot play video: Video is currently flagged (reason: {video.flag})")
                else:
                    self._is_paused = False
                    if self._currently_playing:
                        print(f"Stopping video: {self._currently_playing.title}")
                    self._currently_playing = video
                    print(f"Playing video: {video.title}")
                return
        print("Cannot play video: Video does not exist")

    def stop_video(self):
        """Stops the current video."""
        if self._currently_playing:
            print(f"Stopping video: {self._currently_playing.title}")
            self._currently_playing = None
        else:
            print("Cannot stop video: No video is currently playing")


    def play_random_video(self):
        """Plays a random video from the video library."""
        if self._currently_playing:
            print(f"Stopping video: {self._currently_playing.title}")
        
        videos = [video for video in self._video_library.get_all_videos() if not video.flag]
        if len(videos) == 0:
            print("No videos available")
        else:
            random_video = random.choice(videos)
            self._currently_playing = random_video
            print(f"Playing video: {random_video.title}")

    def pause_video(self):
        """Pauses the current video."""
        if self._is_paused:
            print(f"Video already paused: {self._currently_playing.title}")
        elif self._currently_playing:
            print(f"Pausing video: {self._currently_playing.title}")
            self._is_paused = True
        else:
            print("Cannot pause video: No video is currently playing")

    def continue_video(self):
        """Resumes playing the current video."""
        if self._is_paused:
            print(f"Continuing video: {self._currently_playing.title}")
            self._is_paused = False
        elif not self._currently_playing:
            print("Cannot continue video: No video is currently playing")
        else:
            print(f"Cannot continue video: Video is not paused")


    def show_playing(self):
        """Displays video currently playing."""
        if self._currently_playing:
            x = f"Currently playing: {self._currently_playing.title} ({self._currently_playing.video_id}) [{' '.join(self._currently_playing.tags)}]"
            if self._is_paused:
                x += " - PAUSED"
            print(x)
        else:
            print("No video is currently playing")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        if playlist_name.lower() not in self._playlists:
            self._playlists[playlist_name.lower()] = Playlist(playlist_name)
            print(f"Successfully created new playlist: {playlist_name}")
        else:
            print("Cannot create playlist: A playlist with the same name already exists")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        if playlist_name.lower() in self._playlists:
            video = self._video_library.get_video(video_id)
            if video:
                if video.flag:
                    print(f"Cannot add video to my_playlist: Video is currently flagged (reason: {video.flag})")
                else:
                    if self._playlists[playlist_name.lower()].add(video):
                        print(f"Added video to {playlist_name}: {video.title}")
                    else:
                        print(f"Cannot add video to {playlist_name}: Video already added")
            else:
                print(f"Cannot add video to {playlist_name}: Video does not exist")
        else:
            print(f"Cannot add video to {playlist_name}: Playlist does not exist")

    def show_all_playlists(self):
        """Display all playlists."""
        if len(self._playlists) == 0:
            print("No playlists exist yet")
        else:
            print("Showing all playlists:")
            for k, playlist in sorted(self._playlists.items(), key=lambda x: x[1].name):
                print(playlist.name)

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        if playlist_name.lower() in self._playlists:
            print(f"Showing playlist: {playlist_name}")
            videos = self._playlists[playlist_name.lower()].videos
            if len(videos) == 0:
                print("No videos here yet")
            else:
                for video in self._playlists[playlist_name.lower()].videos:
                    x = f"{video.title} ({video.video_id}) [{' '.join(video.tags)}]"
                    if video.flag:
                        x += f" - FLAGGED (reason: {video.flag})"
                    print(x)
        else:
            print("Cannot show playlist another_playlist: Playlist does not exist")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        if playlist_name.lower() in self._playlists:
            video = self._video_library.get_video(video_id)
            if video:
                if self._playlists[playlist_name.lower()].remove(video):
                    print(f"Removed video from {playlist_name}: {self._video_library.get_video(video_id).title}")
                else:
                    print(f"Cannot remove video from {playlist_name}: Video is not in playlist")
            else:
                    print(f"Cannot remove video from {playlist_name}: Video does not exist")
                
        else:
            print(f"Cannot remove video from {playlist_name}: Playlist does not exist")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        if playlist_name.lower() in self._playlists:
            self._playlists[playlist_name.lower()].clear()
            print(f"Successfully removed all videos from {playlist_name}")
        else:
            print(f"Cannot clear playlist {playlist_name}: Playlist does not exist")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        if playlist_name.lower() in self._playlists:
            del self._playlists[playlist_name.lower()]
            print(f"Deleted playlist: {playlist_name}")
        else:
            print(f"Cannot delete playlist {playlist_name}: Playlist does not exist")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        d = {}
        videos = self._video_library.get_all_videos()
        count = 0
        for video in videos:
            if search_term.lower() in video.title.lower():
                if not video.flag:
                    count += 1
                    if count == 1:
                        print(f"Here are the results for {search_term}:")
                    print(f"{count}) {video.title} ({video.video_id}) [{' '.join(video.tags)}]")
                    d[count] = video
                    
        if count == 0:
            print(f"No search results for {search_term}")
        else:
            print("Would you like to play any of the above? If yes, specify the number of the video.")
            print("If your answer is not a valid number, we will assume it's a no.")
            x = input()
            try:
                if 1 <= int(x) <= count:
                    print(f"Playing video: {d[int(x)].title}")
            except:
                return

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        d = {}
        videos = self._video_library.get_all_videos()
        count = 0
        for video in videos:
            if video_tag in video.tags:
                if not video.flag:
                    count += 1
                    if count == 1:
                        print(f"Here are the results for {video_tag}:")
                    print(f"{count}) {video.title} ({video.video_id}) [{' '.join(video.tags)}]")
                    d[count] = video
        if count == 0:
            print(f"No search results for {video_tag}")
        else:  
            print("Would you like to play any of the above? If yes, specify the number of the video.")
            print("If your answer is not a valid number, we will assume it's a no.")
            x = input()
            try:
                if 1 <= int(x) <= count:
                    print(f"Playing video: {d[int(x)].title}")
            except:
                return

    def flag_video(self, video_id, flag_reason="Not supplied"):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        video = self._video_library.get_video(video_id)
        if video:
            if self._currently_playing == video:
                self._currently_playing = None
                print(f"Stopping video: {video.title}")
            if not video.flag:
                video.set_flag(flag_reason)
                print(f"Successfully flagged video: {video.title} (reason: {flag_reason})")
            else:
                print("Cannot flag video: Video is already flagged")
        else:
            print("Cannot flag video: Video does not exist")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        video = self._video_library.get_video(video_id)
        if video:
            if video.flag:
                video.set_flag(None)
                print(f"Successfully removed flag from video: {video.title}")
            else:
                print("Cannot remove flag from video: Video is not flagged")
        else:
            print("Cannot remove flag from video: Video does not exist")
