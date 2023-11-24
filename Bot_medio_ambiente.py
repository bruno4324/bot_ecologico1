import discord
import random

intents = discord.Intents.default()

intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')
    
@client.event
async def on_message(message):
    
    if message.author == client.user:
        return
    if message.content.startswith('/si o no'):
        await message.channel.send("si")
