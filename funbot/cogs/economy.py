import random

import discord
from discord.ext import commands

class EconomySystem(commands.Cog):

    def __init__(self, bot):
        self._bot = bot
        self._balance = {}

    def _add_bal(self, user_id, amount):
        self._balance[user_id] = self._balance.get(user_id, 0) + amount

    @commands.command()
    async def balance(self, ctx):
        bal = self._balance.setdefault(ctx.author.id, 0)
        if not bal:
            resp_text = "Uh, do you really want me to tell you?"
        else:
            resp_text = str(bal)

        embed = discord.Embed(
            colour = discord.Colour.random(),
            description = resp_text
        )
        await ctx.send(embed=embed)

    @commands.command()
    async def work(self, ctx):
        amount = random.randrange(10, 20)
        self._add_bal(ctx.author.id, amount)

        embed = discord.Embed(
            color=discord.Colour.random(),
            description=f"You worked for {amount} coins!"
        )
        await ctx.send(embed=embed)

    @commands.command()
    async def beg(self, ctx):
        if 0.01 > random.random():
            self._add_bal(ctx.author.id, 200)
            resp_text = "Fine, have 200 coins."
        else:
            resp_text = "How pitiful."
            
        embed = discord.Embed(
            color=discord.Colour.random(),
            description=resp_text
        )
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(EconomySystem(bot))