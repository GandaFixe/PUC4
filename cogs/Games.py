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

    # Counter command
    @commands.command()
    async def counter(self, ctx, num, signal):
        number= int(num)
        if str(signal)== '-':
            for x in range(number):
                            
                await ctx.send(number - x)
                await asyncio.sleep(1)
        elif str(signal) == '+':
            for x in range(number):
                await ctx.send(x)
                await asyncio.sleep(1)
