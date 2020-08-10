#
# Code made for bot PUC4, made by Androca/GandaFixe(Github)
#
import discord
from discord.ext import commands
import random
from discord.ext.commands import has_permissions, CheckFailure
import os
import json
from itertools import cycle

status= cycle([',help', 'Created with python', 'by Androca', 'https://github.com/GandaFixe/PUC4'])


# Change prefix code
def get_prefix(client, message):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]
    

client = commands.Bot(command_prefix = get_prefix)

@client.event
async def on_guild_join(guild):
    await guild.system.channel.send(f'Thank you for adding me\n Im a fun bot with lots of commands\n You can take a look at my source code here: https://github.com/GandaFixe/PUC4')
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = ','

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

@client.event
async def on_guild_remove(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes.pop(str(guild.id))

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

@client.command()
@commands.has_permissions(administrator=True)
async def changeprefix(ctx, prefix):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)
    await ctx.send(f'Prefix changed to {prefix}')
# End of change prefix code

# Print to check if your bot's ready and sets a status
@client.event
async def on_ready():
    change_status.start()
    print ('Logged in')

# Cycle to change status    
@tasks.loop(seconds=3.5)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))


# Console print to check who leaves server
@client.event
async def on_member_remove(member):
    print (f'{member} has left the server')

# Message on command error
@client.event
async def on_command_error(ctx, error):
    await ctx.send('I cant specify that command or you did it incorrectly please make sure that the command you typed exists or make sure that the command is typed correctly and with all the arguments if thats not the case please send me a message on discord M4luc0 da g4nz4#4390 or type ,help')



# Command for calculator
@client.command()
async def calc(ctx, primeiro, sinal, segundo):
    if sinal== '+':
        await ctx.send(float(primeiro)+float(segundo))

    elif sinal== '-':
        await ctx.send(float(primeiro)-float(segundo))

    elif sinal== 'x' or '*':
        await ctx.send(float(primeiro)*float(segundo))

    elif sinal== '/' or ':':
        await ctx.send(float(primeiro)+float(segundo))

# Command that spams a member's mention
@client.command()
@commands.has_permissions(administrator=True)
async def wake(ctx, member: discord.Member):
    while True:
        await ctx.send(f'Wake up {member.mention}')

# Command that shows the server's attributes (name, region, members...)
@client.command()
async def server(ctx):
    members= ctx.guild.member_count
    owner= ctx.guild.owner
    name= ctx.guild.name
    region= ctx.guild.region
    description= ctx.guild.description
    await ctx.send(f'Name: {name}')
    await ctx.send(f'Owner: {owner}')
    await ctx.send(f'Region: {region}')
    await ctx.send(f'Number of members: {members}')

# Commands to load cogs
@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'Sucessfully loaded {extension}')
    
@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send(f'Sucessfully unloaded {extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


client.run('TOKEN HERE')
