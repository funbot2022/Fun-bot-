#!/usr/bin/env python3

import os

from discord.ext import commands

bot = commands.Bot(command_prefix="$", help_command=None)

@bot.command(description="Reload bot", hidden=True)
async def reload(ctx):
    try:
        bot.reload_extension("cmds")
        # green checkmark
        await ctx.message.add_reaction("\u2705")
    except commands.errors.ExtensionNotLoaded:
        # red X
        await ctx.message.add_reaction("\u274C")
        raise

def main():
    token = os.environ.get("DISCORD_BOT_TOKEN")
    if token is None:
        raise RuntimeError("DISCORD_BOT_TOKEN environment variable not set")

    bot.run(token)

if __name__ == "__main__":
    main()
