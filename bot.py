# bot.py
import discord
import os
import asyncio
from dotenv import load_dotenv
from ev_checker import check_for_ev_plays

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
CHANNEL_ID = int(os.getenv('CHANNEL_ID'))

intents = discord.Intents.default()
client = discord.Client(intents=intents)

async def send_ev_alerts():
    await client.wait_until_ready()
    channel = client.get_channel(CHANNEL_ID)
    while not client.is_closed():
        alerts = check_for_ev_plays()
        if alerts:
            for alert in alerts:
                await channel.send(alert)
        await asyncio.sleep(300)

@client.event
def on_ready():
    print(f'{client.user} is online!')

client.loop.create_task(send_ev_alerts())
client.run(TOKEN)
