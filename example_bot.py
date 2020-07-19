import discord

client = discord.Client()
PREFIX = ':'

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(PREFIX + 'hello'):
        await message.channel.send('Hello, ' + '@' + str(message.author))

    # if message.content.startswith(PREFIX + 'changeprefix'):
        

client.run('NzMzNzI2MjIwNDQ0NzYyMTQz.XxLGlw.HTfIUjT4sTs8m-fn8GNgOw4YJTU')
