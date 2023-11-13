import json
import os
from googleapiclient.discovery import build
import isodate

class YoutubeParses:
    api_key: str = os.getenv('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    @classmethod
    def get_channel(cls, channel_id):
        channel_id = 'UC-OVMPlMA3-YCIeg4z5z23A'  # MoscowPython
        yt_channel_all_info = cls.youtube.channels().list(id=channel_id, part='snippet,statistics').execute
        return yt_channel_all_info

class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.id = channel_id
        self.info = YoutubeParses.get_channel(channel_id)


    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(self.id, self.info)
