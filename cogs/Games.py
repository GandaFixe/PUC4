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
    async def counter(ctx, number, signal= None):
        if number>10:
            await ctx.send('This may spam your channel do you want to proceed?')
            @commands.Cog.listener()
            async def on_message(message):
                if message== 'yes' or 'YES' or 'Yes':
                    if signal== '-':
                        for x in range(number):
                            
                            await ctx.send(number - x)
                    elif signal == '+':
                        for x in range(number):
                            await ctx.send(x)
                else:
                    await ctx.send('Stopping your counter')
        elif signal == None:
            await ctx.send('You didnt say how you want the counter to be. Write + for 1, 2, 3..., and write - for 3, 2, 1')

        else:
            if signal== '-':
                for x in range(number):
                            
                    await ctx.send(number - x)
            elif signal == '+':
                for x in range(number):
                    await ctx.send(x)
           
           
