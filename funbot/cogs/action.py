import random

import discord
from discord.ext import commands

_ACTIONS = {
    "punch" : {
        "names" : ["**Punched** You!"],
        "gifs" : ["https://c.tenor.com/_IHzkpDlArQAAAAM/punch-baby-yoda.gif"]
    },
    "kick" : {
        "names" : ["**Kicked** You!"],
        "gifs" : ["https://c.tenor.com/EcdG5oq7MHYAAAAC/shut-up-hit.gif"]
    },
    "slap" : {
        "names" : ["**Slapped** You!"],
        "gifs" : ["https://c.tenor.com/PeJyQRCSHHkAAAAC/saki-saki-mukai-naoya.gif"]
    },
    "stomp" : {
        "names" : ["**Stomped** on You!"],
        "gifs" : ["https://c.tenor.com/nm8yR6Xh39EAAAAC/udagawa-ako-bang-dream.gif"]
    },
    "dance" : {
        "names" : ["**Danced** on You!"],
        "gifs" : ["https://c.tenor.com/uN6dnIXT96sAAAAd/dancinganime-anime.gif"]
    },
    "confused" : {
        "names" : ["is **Confused!**"],
        "gifs" : ["https://c.tenor.com/dIkrwQL-24sAAAAC/anime-confused.gif"]
    },
    "interested" : {
        "names" : ["is **Interested**"],
        "gifs" : ["https://c.tenor.com/qp7g9UD7UeAAAAAC/anime-wow.gif"]
    }
}

class Action(commands.Cog):

    @commands.command(description="say hello")
    async def hello(self, ctx):
        await ctx.send(f"Hello {ctx.author.mention}!")

    async def _send_action_embed(self, ctx, action):
        names = _ACTIONS[action]["names"]
        gifs = _ACTIONS[action]["gifs"]

        embed = discord.Embed(
            colour=(discord.Colour.random()),
            description=f"{ctx.author.mention} {random.choice(names)}"

        )
        embed.set_image(url=(random.choice(gifs)))

        await ctx.send(embed=embed)

    @commands.command(description="Punch someone")
    async def punch(self, ctx):
        await self._send_action_embed(ctx, "punch")

    @commands.command(description="Kick someone")
    async def kick(self, ctx):
        await self._send_action_embed(ctx, "kick")

    @commands.command(description="Slap someone")
    async def slap(self, ctx):
        await self._send_action_embed(ctx, "slap")

    @commands.command(description="Stomp on someone")
    async def stomp(self, ctx):
        await self._send_action_embed(ctx, "stomp")

    @commands.command(description="Dance on someone")
    async def dance(self, ctx):
        await self._send_action_embed(ctx, "dance")

    @commands.command(description="Confused about something")
    async def confusion(self, ctx):
        await self._send_action_embed(ctx, "confused")

    @commands.command(description="Interested in something")
    async def interest(self, ctx):
        await self._send_action_embed(ctx, "interested")

def setup(bot):
    bot.add_cog(Action())