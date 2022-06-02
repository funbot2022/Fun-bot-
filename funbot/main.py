#!/usr/bin/env python3

import os

from discord.ext import commands

_EXTENSIONS = [
]

bot = commands.Bot(command_prefix="$")

@bot.command(description="Reload bot", hidden=True)
async def reload(ctx):
    for ext in _EXTENSIONS:
        try:
            bot.reload_extension(ext)
            # green checkmark
        except commands.errors.ExtensionNotLoaded:
            # red X
            await ctx.message.add_reaction("\u274C")
            raise

    await ctx.message.reply(f"\u2705 Reloaded {len(_EXTENSIONS)} extensions!")

def main():
    token = os.environ.get("DISCORD_BOT_TOKEN")
    if token is None:
        raise RuntimeError("DISCORD_BOT_TOKEN environment variable not set")

    bot.run(token)

if __name__ == "__main__":
    main()
