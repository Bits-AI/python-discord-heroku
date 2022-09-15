"""Admin cog module for Discord Bot."""

import discord
from discord.ext import commands
from utils import checks

class Admin(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(hidden=True)
    @checks.is_owner()
    async def load(self, ctx, *, module: str):
        """Load a cog module."""

        try:
            self.bot.load_extension(f"cogs.{module}")

        except Exception as error:
            print(f"{module} failed to load. Reason: [{type(error).__name__}: {error}")
        
        else:
            print(f"{module} cog loaded.")

    @commands.command(hidden=True)
    @checks.is_owner()
    async def unload(self, ctx, *, module: str):
        """Unload a cog module."""

        try:
            self.bot.unload_extension(f"cogs.{module}")

        except Exception as error:
            print(f"{module} failed to load. Reason: [{type(error).__name__}: {error}")

        else:
            print(f"{module} cog unloaded.")

    @commands.command(hidden=True)
    @checks.is_owner()
    async def reload(self, ctx, *, module: str):
        """Reload a cog module."""

        try:
            self.bot.unload_extension(f"cogs.{module}")
            self.bot.load_extension(f"cogs.{module}")

        except Exception as error:
            print(f"{module} failed to reload. Reason: [{type(error).__name__}: {error}")

        else:
            print(f"{module} cog reloaded.")

    @commands.command(hidden=True)
    @checks.is_owner()
    async def logout(self, ctx):
        """Disconnect from Discord."""

        print("Discord Bot is shutting down.")
        await self.bot.close()

    @load.error
    @unload.error
    @reload.error
    async def _generic_admin_error(self, ctx, error):
        """Function for handling exception when 
        permission checks failed (User does not have
        enough permission).
        """

        if isinstance(error, commands.CheckFailure):
            await ctx.send("You do not have the permission to do that!")

def setup(bot):
    bot.add_cog(Admin(bot))