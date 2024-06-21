import json

from pyrogram import Client

from bot.config import settings
from bot.utils import logger


async def register_sessions() -> None:
    session_name = input('\nEnter the session name (press Enter to exit): ')
    if not session_name:
        return None
    API_ID, API_HASH = get_token(session_name)

    if not API_ID or not API_HASH:
        raise ValueError("API_ID and API_HASH not found in the tokens file.")

    session = Client(
        name=session_name,
        api_id=API_ID,
        api_hash=API_HASH,
        workdir="sessions/"
    )

    async with session:
        user_data = await session.get_me()

    logger.success(f'Session added successfully @{user_data.username} | {user_data.first_name} {user_data.last_name}')


def get_token_json():
    with open('tokens.json') as f:
        return json.load(f)


def get_token(name):
    with open('tokens.json') as f:
        data = json.load(f)[name]
        return data['id'], data['hash']
