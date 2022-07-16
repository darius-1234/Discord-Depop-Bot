import os
import discord
from dotenv import load_dotenv
from DepopBot import scrape_site, clean_data, summary_of_prices, findInfo


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    itemRequested = message.content
    print(itemRequested)
    avg, max, min,  std, num_available = findInfo(itemRequested)
    bot_reply = (f'DEPOP: max:{max1}, min: {min1}, average: {av1}, standard_deviation: {std1}, number_of_listings: {number_of_shoes}')
    await message.channel.send(bot_reply)
client.run(TOKEN)




