#!/usr/bin/env python3

import os

import discord
from discord.ext import commands

_EXTENSIONS = [
    "funbot.cogs.action",
    "funbot.cogs.casual",
    "funbot.cogs.economy"
]

_CHECKMK = "\u2705"
_FAILMK = "\u274C"

bot = commands.Bot(command_prefix="$")
for ext in _EXTENSIONS:
    bot.load_extension(ext)

@bot.event
async def on_ready():
    print("Connected to Discord")
    await bot.change_presence(
        activity=discord.Game(
            name="$help",
        )
    )

@bot.command(description="Reload bot", hidden=True)
async def reload(ctx):
    for ext in _EXTENSIONS:
        try:
            bot.reload_extension(ext)
        except commands.errors.ExtensionNotLoaded:
            await ctx.message.add_reaction(_FAILMK)
            raise

    await ctx.message.reply(
        f"{_CHECKMK} Reloaded {len(_EXTENSIONS)} extensions!"
    )

def main():
    token = os.environ.get("DISCORD_BOT_TOKEN")
    if token is None:
        raise RuntimeError("DISCORD_BOT_TOKEN environment variable not set")

    bot.run(token)

if __name__ == "__main__":
    main()
