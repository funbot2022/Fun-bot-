import random

from discord.ext import commands

class Casual(commands.Cog):

    @commands.command()
    async def hello(self, ctx):
        timeofday = random.choice(["morning", "afternoon", "evening", "night"])
        await ctx.send(f"Good {timeofday} {ctx.author.mention}...I think!")

def setup(bot):
    bot.add_cog(Casual())