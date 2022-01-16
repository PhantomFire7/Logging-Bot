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
    
@client.event()
async def on_message_delete(self, msg):
    d = "deleted a message in"
    now = datetime.utcnow()
    if msg.author.bot:
        return
    logs = client.get_channel(int(log_channel))
    user = msg.author
    emb = Embed(title="**Message deleted**", description=f"{msg.author.mention} {d} {msg.channel.mention}", color=Color.blue(), timestamp=now)
    emb.add_field(name="**Message content:**", value=msg.content, inline=False)
    emb.set_author(name=msg.author, icon_url=msg.author.avatar_url)
    emb.set_thumbnail(url=user.avatar_url)
    emb.set_footer(text=f"User ID: {msg.author.id}\nChannel ID: {msg.channel.id}\nMessage ID: {msg.id}")
    await logs.send(embed=embed)

@client.event
async def on_message_edit(before, after):
    embed = discord.Embed(title="Message Edited", description=f"**Edited in {before.channel.mention}**\n\n**Message before**\n{before.content}\n**Message after**\n{after.content}", color=discord.Color.green())
    embed.set_footer(text=f"Message was sent by {before.author}", icon_url=before.author.avatar_url)
    logs = client.get_channel(int(log_channel))

    await logs.send(embed=embed)

@client.event
async def on_guild_role_create(role):
    logs = client.get_channel(int(log_channel))
    await logs.send(f"{role.name} {role.colour}}")

client.run(TOKEN)
