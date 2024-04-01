import asyncio
import time
import sys
import os
import random

from utility import Utility
from log import get_logger, get_date_time

batch_count = 1 if len(sys.argv) < 2 else int(sys.argv[1])
logger = get_logger()
ts = get_date_time()
file_name = os.path.join(os.getcwd(), 'data', f'{ts}.csv')

util = Utility(logger, file_name)


def get_match_id(match):
    if type(match) is dict:
        id = match.get('match_id')
        return id
    return None


async def iterate_matches(parsed_matches):
    for match in parsed_matches:
        id = get_match_id(match)
        try:
            await util.get_match_chats(id) if id is not None else ''
        except Exception as e:
            logger.error(f'error getting match: {id} details. {e}')

        time.sleep(random.randint(1, 3))


async def start() -> None:
    logger.info('starting to collect in-game chats')
    for i in range(batch_count):
        logger.info(f'batch {i} started')

        try:
            parsed_matches = await util.get_parsed_matches()

            logger.info(f'matches {len(parsed_matches)}')
            await iterate_matches(parsed_matches)

        except Exception as e:
            logger.error(f'batch {i}: error getting parsed matches. {e}')

        time.sleep(random.randint(1, 3))

    logger.info(f'batch {i} ended')


loop = asyncio.get_event_loop()
loop.run_until_complete(start())
