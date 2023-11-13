import os
from googleapiclient.discovery import build


channel_id = os.getenv('YT_API_KEY')

youtube = build('youtube', 'v3', developerKey = channel_id)

class Channel:
    """Класс для ютуб - канала"""


    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала.
        Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id


    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        request = youtube.channels().list(
            part = 'snippet, contentDetails, statistics',
            id = 'UC-OVMPlMA3-YCIeg4z5z23A')
        print(request)

