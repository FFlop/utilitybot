import discord
from discord.ext import commands
from utilitybot import Utilitybot
import asyncio
import asyncpg
import dotenv

bot = Utilitybot(
    command_prefix="u!"
    status=discord.Status.idle
)