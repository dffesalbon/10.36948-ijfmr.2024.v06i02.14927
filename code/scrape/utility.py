import json
import http3
import os

from data import Data
from log import get_date_time

from logging import Logger
from datetime import datetime


class Utility():
    def __init__(self, logger: Logger = None, file_name: str = None) -> None:
        self.__logger = logger
        self.__client = http3.AsyncClient()
        self.__data = Data(logger=logger)
        self.__file_name = file_name

    def date_time(self, timestamp: float) -> datetime:
        return datetime.fromtimestamp(timestamp)

    def get_file_name(self):
        ts = get_date_time()
        data_dir = os.path.join(os.getcwd(), 'data', f'{ts}.csv')
        return data_dir

    async def get_parsed_matches(self):
        url = 'https://api.opendota.com/api/parsedMatches'
        req = await self.__client.get(url=url)
        json_list = list(json.loads(req.content))
        return json_list

    async def get_match_chats(self, match_id):
        try:
            url = f'https://api.opendota.com/api/matches/{match_id}'
            req = await self.__client.get(url=url)
            content = req.content.decode('utf-8')
            json_data = json.loads(content)
            chats = json_data['chat']
            region = json_data['region']
            date_time = self.date_time(json_data['start_time'])

            for chat in chats:
                message = chat['key']
                player_slot = chat['player_slot']
                slot = chat['slot']
                time = chat['time']

                row_data = []
                row_data.append(date_time)
                row_data.append(match_id)
                row_data.append(region)
                row_data.append(time)
                row_data.append(slot)
                row_data.append(player_slot)
                row_data.append(message)

                if chat['type'] == 'chat':
                    self.__data.write(self.__file_name, row_data)

            res = f'chats from {match_id}: collected successfully'
            self.__logger.info(res)

        except Exception as e:
            print(str(e))
            res = f'chats from {match_id}: failed to collect'
            self.__logger.info(res)
