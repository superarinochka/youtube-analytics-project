from googleapiclient.discovery import build
import json
import os
class Channel:
    """Класс для ютуб-канала"""
    api_key: str = os.getenv('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)



    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        self.info = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        self.title = self.info["items"][0]["snippet"]["title"]
        self.description= self.info["items"][0]["snippet"]["description"]
        self.url = self.info["items"][0]["snippet"]["thumbnails"]["default"]["url"]
        self.subscriber_count = self.info["items"][0]["statistics"]["subscriberCount"]
        self.view_count = self.info["items"][0]["statistics"]["viewCount"]
        self.video_count = self.info["items"][0]["statistics"]["videoCount"]


    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel_info = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        print(json.dumps(channel_info, indent=2, ensure_ascii=False))


    @classmethod
    def get_service(cls):
        return cls.youtube



    def to_json(self, file_name):
        data = {
            'channel_id' : self.channel_id,
            'channel_name' : self.title,
            'channel_description' : self.description,
            'channel_url' : self.url,
            'channel_subscriber_count ' : self.subscriber_count,
            'channel_video_count' : self.video_count,
            'channel_view_count' : self.view_count,
           }

        with open(file_name, 'w', encoding='utf-8') as file:
            json.dump(data, file)