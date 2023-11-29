import os
from googleapiclient.discovery import build
import isodate
import datetime


class PlayList:
    api_key: str = os.getenv('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, playlist_id):
        self.__playlist_id = playlist_id
        self.playlist_response = self.youtube.playlists().list(part='snippet', id=self.__playlist_id).execute()
        self.playlist_videos = self.youtube.playlistItems().list(playlistId=playlist_id, part='contentDetails',
                                                                 maxResults=50, ).execute()
        self.video_ids = [video_id['contentDetails']['videoId'] for video_id in self.playlist_videos['items']]
        self.title = self.playlist_response['items'][0]['snippet']['title']
        self.url = "https://www.youtube.com/playlist?list=" + f"{self.__playlist_id}"

    @property
    def total_duration(self):
        video_response = self.youtube.videos().list(part='contentDetails,statistics',
                                                    id=','.join(self.video_ids)).execute()
        summ_duration = datetime.timedelta(seconds=0)
        for video in video_response['items']:
            # YouTube video duration is in ISO 8601 format
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            summ_duration += duration
        return summ_duration

    def show_best_video(self):
        max_like_count = []

        def key_like(key):
            return key["like_count"]

        for video in self.video_ids:
            video_response = self.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                        id=video).execute()
            max_like_count.append({"id": video, "like_count": video_response['items'][0]['statistics']['likeCount']})
        max_like = max(max_like_count, key=key_like)
        return f'https://youtu.be/{max_like["id"]}'