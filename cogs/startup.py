"""Sample startup cog module for Discord Bot."""

import discord
from discord.ext import commands, tasks
import os
from utils import status_util

class Startup(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.status_file = os.path.abspath(os.path.join(os.path.dirname(__file__), f"../config/status.csv"))
        self.status = status_util.StatusUtil(self.status_file)

    @commands.Cog.listener()
    async def on_ready(self):
        """Function to run when the bot is connected to Discord server."""

        self.presence_handler.start()
        print("Discord Bot is online.")

    @tasks.loop(seconds=30)
    async def presence_handler(self):
        """Function for handling the loops of the status from 
        status.csv file.
        """

        status = self.status.get()
        await self.bot.change_presence(status=discord.Status.idle, activity=discord.Game(name=status))

def setup(bot):
    bot.add_cog(Startup(bot))