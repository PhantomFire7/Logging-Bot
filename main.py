from cmath import log
import discord
import json
from discord.ext import commands

client = commands.Bot(command_prefix='.', intents = discord.Intents.all())

with open('config.json') as json_file:
    data = json.load(json_file)

log_channel = data["log_channel"]
TOKEN = data["bot_token"]

@client.event
async def on_ready():
    print(f"Connected to {client.user}")

@client.event
async def on_message_delete(message):
    embed = discord.Embed(title="Message deleted", description=f"**Deleted in {message.channel.mention}**\n\n{message.content}\n\n", color=discord.Color.red())
    embed.set_footer(text=f"Message was sent by {message.author}", icon_url=message.author.avatar_url)


    logs = client.get_channel(int(log_channel))

    await logs.send(embed=embed)

client.run(TOKEN)