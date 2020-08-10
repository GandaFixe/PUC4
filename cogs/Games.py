import discord
from discord.ext import commands
import random
from discord.ext.commands import has_permissions, CheckFailure
import os
import json
from itertools import cycle
import asyncio

# Setup working function 
def setup(client):
    client.add_cog(Games(client))

# Official class for the Games.py
class Games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    # Force Counter command
    @commands.has_permissions(administrator=True)
    @commands.command()
    async def fcounter(self, ctx, num, signal):
        number= int(num)
        if str(signal)== '-':
            for x in range(number):
                            
                await ctx.send(number - x)
                await asyncio.sleep(1)
        elif str(signal) == '+':
            for x in range(number):
                await ctx.send(x)
                await asyncio.sleep(1)
    
    @commands.command()
    async def counter(self, ctx, num, signal):
        number= int(num)
        if str(signal)== '-' and number<10:
            for x in range(number):
                            
                await ctx.send(number - x)
                await asyncio.sleep(1)
        elif str(signal) == '+' and number<10:
            for x in range(number):
                await ctx.send(x+1)
                await asyncio.sleep(1)
        else:
            await ctx.send('Your number is too high! if you have administrator perms and want to count to 1000000... use ,fcounter')
 import discord
from discord.ext import commands
import random
from discord.ext.commands import has_permissions, CheckFailure
import os
import json
from itertools import cycle
import asyncio

# Setup working function 
def setup(client):
    client.add_cog(Games(client))

# Official class for the Games.py
class Games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    # Force Counter command
    @commands.has_permissions(administrator=True)
    @commands.command()
    async def fcounter(self, ctx, num, signal):
        number= int(num)
        if str(signal)== '-':
            for x in range(number):
                            
                await ctx.send(number - x)
                await asyncio.sleep(1)
        elif str(signal) == '+':
            for x in range(number):
                await ctx.send(x)
                await asyncio.sleep(1)
    
    @commands.command()
    async def counter(self, ctx, num, signal):
        number= int(num)
        if str(signal)== '-' and number<10:
            for x in range(number):
                            
                await ctx.send(number - x)
                await asyncio.sleep(1)
        elif str(signal) == '+' and number<10:
            for x in range(number):
                await ctx.send(x+1)
                await asyncio.sleep(1)
        else:
            await ctx.send('Your number is too high! if you have administrator perms and want to count to 1000000... use ,fcounter')
           
    # Command to check the latency of the bot
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Pong {round(client.latency * 1000)}ms')

    # Just a command for fun
    @commands.command(aliases=['8ball'])
    async def _8ball(self, ctx, *, question):
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
        await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)
