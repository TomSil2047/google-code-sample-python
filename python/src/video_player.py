"""A video player class."""

from .video_library import VideoLibrary
import random


class VideoPlayer:
    """A class used to represent a Video Player."""

    

    def __init__(self):
        self._video_library = VideoLibrary()
        self.current_video_id = ''
        self.current_video_is_paused = False
        self.playlists = {}

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        print("Here's a list of all available videos:")
        
        videos = open('src/videos.txt', 'r')

        lines=[]
        line = videos.readline()

        while line:

            line = line.replace('| ', '(', 1)
            line = line.replace(' |  ', ') [',1)
            line = line.replace(' |', ') []',1)
            line = line.replace('\n',']')
            line = line.replace(',', '')
            lines.append(line)
            print(line)
            line=videos.readline()

        print(len(lines))

        videos.close()

    def play_video(self, video_id):

        try:
            video_name = self._video_library.get_video(video_id).title
        except AttributeError:
            print('Cannot play video: Video does not exist')
            return
        
        if self.current_video_id != '':
            current_video_name = self._video_library.get_video(self.current_video_id).title
            print('Stopping video: ' + current_video_name)

        self.current_video_id = video_id
        self.current_video_is_paused = False
        print('Playing video: ' + video_name)


    def stop_video(self):
        """Stops the current video."""

        try:
            current_video_name = self._video_library.get_video(self.current_video_id).title
        except AttributeError:
            print('Cannot stop video: No video is currently playing')
            return

        self.current_video_id = ''
        print('Stopping video: ' + current_video_name)
        

        

    def play_random_video(self):
        """Plays a random video from the video library."""

        num_videos = len(self._video_library.get_all_videos())



        video_list = []
            
        videos = open('src/videos.txt', 'r')

        line = videos.readline()

        while line:

            line = line.split(' | ')
            line[1] = line[1].replace(' |', '')
            video_list.append(line)
            line = videos.readline()

        random_video = random.choice(video_list)
        self.current_video_id = random_video[1]
        self.current_video_is_paused = False
        print('Playing video ' + random_video[0])
            
        videos.close()
        

    def pause_video(self):
        """Pauses the current video."""

        try:
            current_video_name = self._video_library.get_video(self.current_video_id).title
            if not self.current_video_is_paused:
                self.current_video_is_paused = True
                print('Pausing video: ' + current_video_name)
            else:
                print('Video already paused: ' + current_video_name)
                
        except AttributeError:
            print('Cannot pause video: No video is currently playing')
        

    def continue_video(self):
        """Resumes playing the current video."""

        try:
            current_video_name = self._video_library.get_video(self.current_video_id).title
            if self.current_video_is_paused:
                self.current_video_is_paused = False
                print('Continuing video: ' + current_video_name)
            else:
                print('Cannot continue video: Video is not paused')
                
        except AttributeError:
            print('Cannot continue video: No video is currently playing')
        

    def show_playing(self):
        """Displays video currently playing."""

        try:
            current_video_name = self._video_library.get_video(self.current_video_id).title
            current_video_tags = self._video_library.get_video(self.current_video_id).tags

            if not self.current_video_is_paused:
                print('Currently playing: ' + current_video_name + ' (' + self.current_video_id + ') [' + current_video_tags[0] + ' ' + current_video_tags[1] + ']')
            else:
                print('Currently playing: ' + current_video_name + ' (' + self.current_video_id + ') [' + current_video_tags[0] + ' ' + current_video_tags[1] + '] - PAUSED')
                
        except AttributeError:
            print('No video is currently playing')

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """

        lower_playlist_name = playlist_name.lower()

        if lower_playlist_name in self.playlists:
            print('Cannot create playlist: A playlist with the same name already exists')
        else:
            self.playlists[lower_playlist_name] = []
            print('Successfully created new playlist: ' + playlist_name)
        
    
        

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        lower_playlist_name = playlist_name.lower()
        
        if lower_playlist_name not in self.playlists:
            print('Cannot add video to ' + playlist_name + ': Playlist does not exist')
    

        try:
            video_title = self._video_library.get_video(video_id).title

            if video_id in self.playlists[lower_playlist_name]:
                print('Cannot add video to ' + playlist_name + ': Video already added')
            else:
                self.playlists[lower_playlist_name].append(video_id)
                print('Add video to ' + playlist_name + ': ' + video_title)

        except AttributeError:
            print('Cannot add video to ' + playlist_name + ': Video does not exist')
            

        

    def show_all_playlists(self):
        """Display all playlists."""

        
        

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
