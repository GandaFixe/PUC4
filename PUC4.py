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

# Commando to check the latency of the bot
@client.command()
async def ping(ctx):
    await ctx.send(f'Pong {round(client.latency * 1000)}ms')

# Just a command for fun
@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = ["It is certain.",
"It is decidedly so.",
"Without a doubt.",
"Yes - definitely.",
"You may rely on it.",
"As I see it, yes.",
"Most likely.",
"Outlook good.",
"Yes.",
"Signs point to yes.",
"Reply hazy, try again.",
"Ask again later.",
"Better not tell you now.",
"Cannot predict now.",
"Concentrate and ask again.",
"Don't count on it.",
"My reply is no.",
"My sources say no.",
"Outlook not so good.",
"Very doubtful."]
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

# Command that clears messages
@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=5):
    amount = amount+1
    await ctx.channel.purge(limit=amount)
    await ctx.send(f'{amount-1} messages got destroyed')
    await ctx.channel.purge(limit=1)

# Command that kicks members
@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'GOD kicked {member}\nReason: {reason}')

# Command that bans members
@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'GOD banned {member}\nReason: {reason}')

# Command that unbans members
@client.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'GOD unbanned {user.mention}')
            return

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
