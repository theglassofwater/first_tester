import discord
import os
import dotenv

dotenv.load_dotenv()

client = discord.Client()

@client.event
async def on_ready():
    print("logged in yay {0.user}".format(client))



@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('hello'):
        await message.channel.send("hello to u")

client.run(os.getenv('STFU'))
