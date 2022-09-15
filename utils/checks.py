"""Module for handling permission checks."""

from discord.ext import commands
import discord.utils

def check_is_owner(message):
    """Returns the Discord ID for the bot owner."""

    return message.author.id == "<Your Discord ID here>"

def is_owner():
    """Function to check if the message sender 
    is the bot owner.
    """
    
    return commands.check(lambda ctx: check_is_owner(ctx.message))