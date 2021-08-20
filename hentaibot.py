import discord  # discord lib
import time  # time lib
import asyncio  # asyncio(for keeping bot alive)
import json  # handling json

from discord import channel, guild
from discord.ext import commands
from discord.ext.commands import bot
from dotenv import load_dotenv  # env format handling
import hmtai #hmmm
import requests  # loading data from web
import os  # need for running bot



intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)





load_dotenv()  # initializing dotenv


##Load hentai
def load_content(index):


    if index == "ass":
        link = hmtai.useHM("v1", index)


    elif index == "neko":
        index = "nsfwNeko"
        link = hmtai.useHM("v1", index)


    elif index == "ero":
        link = hmtai.useHM("v1", index)

    elif index == "hentai":
        link = hmtai.useHM("v1", index)

    elif index == "femdom":
        link = hmtai.useHM("v1", index)

    else:
        link = hmtai.useHM("v1", "hentai")


    return link


print(load_content("hentai"))


def get_joke():
    response = requests.get("http://rzhunemogu.ru/RandJSON.aspx?CType=11")

    json_data = json.loads(response.text, strict = False)
    joke = json_data['content']
    return (joke)



# Function for loading jokes from webserver



# Startup

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))



@client.event
async def on_message_join(member):
    print("Bruh")
    channel = client.get_channel(842821265861509150)
    embed=discord.Embed(f"Welcome {member.name}", f"Thanks for joining {member.guild.name}!") # F-Strings!
    embed.set_thumbnail(member.avatar_url) # Set the embed's thumbnail to the member's avatar image!

    await channel.send(embed)


# if message was sent detector
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    #Hentai
    if message.content.startswith('$horny'):

        Message = str(message.content)
        print(Message)
        word_list = Message.split()
        try:
            index = word_list[1]
        except IndexError:
            index = "hentai"


        image = load_content(index)
        await message.channel.send(image)


    #Clearnewroles
    if message.content.startswith('$clearnewroles'):
        member = message.author
        guild = member.guild

        for role in guild.roles:
            if role.name == "new role" or role.name =="новая роль":

                await role.delete()
                print("Success")

        await message.channel.send('All unused roles were deleted!')



    if message.content.startswith('$leshapidoras'):
        for i in range(10):

            await message.channel.send(
            """
            ```diff
- У андрея писюн 3мм!
            ```
            """)


    #Анекдоты

    if message.content.startswith("$joke"):
        await message.channel.send(get_joke())



    #НЕ ОРАТЬ
    message_text = message.content

    if message_text.isupper()==True and message.author != client.user:
        await message.channel.send(
        """
        ```diff
- НЕ ОРАТЬ!
        ```
        """)



client.run(os.getenv('TOKEN'))

