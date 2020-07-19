import discord
from discord.ext import commands
import random
from discord.ext.commands import has_permissions, CheckFailure
import os


client = commands.Bot(command_prefix = ',')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Created with Python, by Androca'))
    print ('Logged in')

@client.event
async def on_member_join(member):
    print (f'{member} joined the server')

@client.event
async def on_member_remove(member):
    print (f'{member} has left the server')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong {round(client.latency * 1000)}ms')

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

@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=5):
    amount = amount+1
    await ctx.channel.purge(limit=amount)

@client.command()
@commands.has_permissions(administrator=True)
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'A very good person kicked {member}\nReason: {reason}')

@client.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'A VERY GOOD PERSON banned {member}\nReason: {reason}')

@client.command()
@commands.has_permissions(  administrator=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return

#@client.command()
#async def load(ctx, extension):
#    client.load_extension()

#@client.command()
#async def load(ctx, extension):
#    client.load_extension(f'cogs.{extension}')

#@client.command()
#async def unload(ctx, extension):
#    client.unload_extension(f'cogs.{extension}')

#for filename in os.listdir('./cogs'):
#    if filename.endswith('.py'):
#        client.load_extension(f'cogs.{filename[:-3]}')

client.run('NzMzNzI2MjIwNDQ0NzYyMTQz.XxLGlw.HTfIUjT4sTs8m-fn8GNgOw4YJTU')

