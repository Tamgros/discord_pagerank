
import json
import discord


with open("config.json") as f:
    conf = json.load(f)
    app_id = conf["application_id"]
    client_id = conf["client_id"]
    client_secret = conf["client_secret"]
    public_key = conf["public_key"]
    token = conf["token"]


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))


client = MyClient()
client.run(token)
