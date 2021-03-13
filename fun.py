import discord
import random
from discord.ext import commands
import datetime
from typing import Optional
from discord import Member
from aiohttp import request

utc_time = datetime.datetime.utcnow()

ranked_channel = 816348090223165490
bot_channel = 816349382055690310
talk_channels = [736031756251299942, 627184200382021642, 707672339109904516, 707672525093470319, 623489709510885386, 707673187886039122, 707673404865511424, 816346546710249474, 599905406591959052, 816347201424457798, 816347303547764748, 735496917936767017, 816347398019743784, 708592090271187002, 708592629272674325, 709019858054152252, 816347994983104582, 816348044148211722, 816348135986036826, 816348718659010560, 816348743602536508, 816348770438479932, 816348795280293889, 707726492611641405, 708441833964830780, 735998833770889338, 764154879252889640, 731299838934777907, 735918031485796356]

class fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Fun.py is ready.")

    @commands.command(aliases=["flip"])
    async def coin(self, ctx):
        if ctx.channel.id in talk_channels:
            embed = discord.Embed(description="You must do this command in the bot commands channel.", colour=discord.Colour.red())
            await ctx.channel.send(embed=embed)
        elif ctx.channel.id == ranked_channel:
            embed = discord.Embed(description="You must do this command in the bot commands channel.", colour=discord.Colour.red())
            await ctx.channel.send(embed=embed)
        else:
            coinFace = ('heads', 'tails')
            result = random.choice(coinFace)
            await ctx.send(f"The coin landed on {result}")

    @commands.command(aliases=["dice", "die"])
    async def roll(self, ctx, num = None):
        if ctx.channel.id in talk_channels:
            embed = discord.Embed(description="You must do this command in the bot commands channel.", colour=discord.Colour.red())
            await ctx.channel.send(embed=embed)
        elif ctx.channel.id == ranked_channel:
            embed = discord.Embed(description="You must do this command in the bot commands channel.", colour=discord.Colour.red())
            await ctx.channel.send(embed=embed)
        else:
            if num == None:
                r = random.randint(1, 6)
                await ctx.send(f"You rolled a {r}")
            elif num != None:
                r = random.randint(1, int(num))
                if r == 18:
                    await ctx.send(f"You rolled an {r}")
                elif str(r).startswith("8"):
                    await ctx.send(f"You rolled an {r}")
                else:
                    await ctx.send(f"You rolled a {r}")
            else:
                pass

    @commands.command(aliases=["animalfact", "af"])
    async def animal_fact(self, ctx, animal: str):
        if ctx.channel.id in talk_channels:
            embed = discord.Embed(description="You must do this command in the bot commands channel.", colour=discord.Colour.red())
            await ctx.channel.send(embed=embed)
        elif ctx.channel.id == ranked_channel:
            embed = discord.Embed(description="You must do this command in the bot commands channel.", colour=discord.Colour.red())
            await ctx.channel.send(embed=embed)
        else:
            if (animal := animal.lower()) in ("dog", "cat", "panda", "fox", "bird", "koala"):
                fact_url = f"https://some-random-api.ml/facts/{animal}"
                image_url = f"https://some-random-api.ml/img/{'birb' if animal == 'bird' else animal}"
                async with request("GET", image_url, headers={}) as response:
                    if response.status == 200:
                        data = await response.json()
                        image_link = data["link"]
                    else:
                        image_link = None
                async with request("GET", fact_url, headers={}) as response:
                    if response.status == 200:
                        data = await response.json()
                        embed = discord.Embed(title=f"{animal.title()} fact", description=data["fact"], colour=discord.Colour.blue(), timestamp=datetime.datetime.utcnow())
                        if image_link is not None:
                            embed.set_image(url=image_link)
                        embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}\u200b")
                        await ctx.send(embed=embed)
                    else:
                        await ctx.send(f"API returned a {response.status} status.")
            else:
                embed = discord.Embed(description="No facts are available for that animal. The available animals are: dog, cat, panda, fox, bird and koala.", colour=discord.Colour.red())
                await ctx.send(embed=embed)

    @commands.command(aliases=["userinfo", "memberinfo", "ui", "mi", "user_info", "member_info"])
    async def whois(self, ctx, target: Optional[Member]):
        if ctx.channel.id in talk_channels:
            embed = discord.Embed(description="You must do this command in the bot commands channel.", colour=discord.Colour.red())
            await ctx.channel.send(embed=embed)
        elif ctx.channel.id == ranked_channel:
            embed = discord.Embed(description="You must do this command in the bot commands channel.", colour=discord.Colour.red())
            await ctx.channel.send(embed=embed)
        else:
            target = target or ctx.author
            embed = discord.Embed(title=f"__{target.name}'s Information__", colour=discord.Colour.blue(), timestamp=datetime.datetime.utcnow())
            embed.set_thumbnail(url=target.avatar_url)
            if target.top_role.mention == ctx.guild.default_role.mention:
                fields = [("Name:", target.mention, True),
                          ("ID:", target.id, True),
                          ("Bot:", target.bot, True),
                          ("Top role:", "N/A", True),
                          ("Created at:", target.created_at.strftime("%d/%m/%Y %H:%M"), True),
                          ("Joined at:", target.joined_at.strftime("%d/%m/%Y %H:%M"), True)]
                for name, value, inline in fields:
                    embed.add_field(name=name, value=value, inline=inline)
                embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}\u200b")
                await ctx.send(embed=embed)
            else:
                fields = [("Name:", target.mention, True),
                          ("ID:", target.id, True),
                          ("Bot:", target.bot, True),
                          ("Top role:", target.top_role.mention, True),
                          ("Created at:", target.created_at.strftime("%d/%m/%Y %H:%M"), True),
                          ("Joined at:", target.joined_at.strftime("%d/%m/%Y %H:%M"), True)]
                for name, value, inline in fields:
                    embed.add_field(name=name, value=value, inline=inline)
                embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}\u200b")
                await ctx.send(embed=embed)

    @commands.command(aliases=["8ball", "eightball", "8_ball"])
    async def eight_ball(self, ctx, *args):
        if ctx.channel.id in talk_channels:
            embed = discord.Embed(description="You must do this command in the bot commands channel.", colour=discord.Colour.red())
            await ctx.channel.send(embed=embed)
        elif ctx.channel.id == ranked_channel:
            embed = discord.Embed(description="You must do this command in the bot commands channel.", colour=discord.Colour.red())
            await ctx.channel.send(embed=embed)
        else:
            answers = ['It is certain.', 'It is decidedly so.', 'You may rely on it.', 'Without a doubt.', 'Yes - definitely.', 'As I see, yes.', 'Most likely.', 'Outlook good.', 'Yes.', 'Signs point to yes.', 'Reply hazy, try again.', 'Ask again later.', 'Better not tell you now.', 'Cannot predict now.', 'Concentrate and ask again later.', 'Don\'t count on it.', 'My reply is no.', 'My sources say no.', 'Outlook not so good.', 'Very doubtful.']
            embed = discord.Embed(title="**My Answer:**", description=f"{answers[random.randint(0, len(answers))]}", color=discord.Colour.blue(), timestamp=datetime.datetime.utcnow())
            embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}\u200b")
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(fun(client))
