import discord
from discord.ext import commands
import random
from discord.ext.commands import has_permissions, CheckFailure
import os
import json


# Setup working function 
def setup(client):
    client.add_cog(Welcome(client))

# Official class for the Welcome.py
class Welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    # Cog event to welcome mebers to the server
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel= member.guild.system_channel
        if channel != None:
            await channel.send(f'Welcome {member.mention}, hope you enjoy this server!')

        else:
            owner= guild.owner
            await owner.send('You imported the welcome extension but you didnt set up a system channel, pls set up the system channel for me to welcome people when they join')
