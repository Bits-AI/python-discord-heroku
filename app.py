from discord.ext import commands
import signal
import os
from utils import config_util

bot = commands.Bot(command_prefix = config_util.get_prefix())

initial_cogs = [
    'cogs.startup',
    'cogs.admin',
]

#This class is made for heroku force shut down (Experimental)
class GracefulExit:
    
    def __init__(self, bot):
        self.bot = bot
        signal.signal(signal.SIGTERM, self.exit_gracefully)

    def exit_gracefully(self):
        print("Exiting...")
        exit(0)

if __name__ == '__main__':
    try:
        grace = GracefulExit(bot)

        bot.token = config_util.get_token()

        for cog in initial_cogs:
            try:
                bot.load_extension(cog)

            except Exception as error:
                print(f"Failed to load cog {cog}\n{type(error).__name__}: {error}")

        bot.run(bot.token)

    except KeyboardInterrupt as error:
        print("Detect Keyboard Interruption!")
        try:
            exit(1)

        except SystemExit:
            os._exit(0)