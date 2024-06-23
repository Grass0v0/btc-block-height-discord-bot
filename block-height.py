import discord
import requests
import asyncio
from datetime import datetime

# Place 'TOKEN' with your actual bot token
TOKEN = ''

API = 'https://mempool.space/api/blocks/tip/height'

intents = discord.Intents.default()
client = discord.Client(intents=intents)

async def update_activity():
    await client.wait_until_ready()
    while not client.is_closed():
        try:
            response = requests.get(API)
            response.raise_for_status()
            current_block = response.text  
            now = datetime.now()
            print(f"{now} - Current Block: {current_block}")

            activity = discord.Activity(
                type=discord.ActivityType.watching,
                name=f"Block: {current_block}"
            )
            await client.change_presence(activity=activity)
        except Exception as e:
            now = datetime.now()
            print(f"{now} - Error fetching block data: {e}")

        # delay ( Update every 3 seconds)
        await asyncio.sleep(3)

@client.event
async def on_ready():
    print(f'Bot is ready as {client.user}')

client.loop.create_task(update_activity())
client.run(TOKEN)
