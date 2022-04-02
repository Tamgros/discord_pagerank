import discord
import json
import requests

with open("config.json") as f:
    conf = json.load(f)
    app_id = conf["application_id"]
    client_id = conf["client_id"]
    client_secret = conf["client_secret"]
    public_key = conf["public_key"]
    token = conf["token"]

bot_permissions = "29527993472"

bot_invite = f"https://discord.com/api/oauth2/authorize?client_id={client_id}&permissions={bot_permissions}&scope=bot%20applications.commands"
print(bot_invite)

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    print(message.content)
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run(token)
