import os
from googleapiclient.discovery import build


class Video:
    def __init__(self, video_id: str):
        self.video_id: str = video_id
        self.video_info: dict = self.get_video_info(video_id)
        self.video_title: str = self.video_info['items'][0]['snippet']['title']
        self.video_url = "https://www.youtube.com/watch?v=" + f"{video_id}"
        self.view_count: int = int(self.video_info['items'][0]['statistics']['viewCount'])
        self.like_count: int = int(self.video_info['items'][0]['statistics']['likeCount'])


    def __str__(self):
        return self.video_title


    @classmethod
    def get_service(cls):
        api_key: str = os.getenv('YT_API_KEY')
        return build('youtube', 'v3', developerKey=api_key)
    @classmethod
    def get_video_info(cls, video_id):
        video_response = cls.get_service().videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                         id=video_id).execute()
        return video_response


class PLVideo(Video):
    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.playlist_id = playlist_id