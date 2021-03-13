import discord
from discord.ext import commands
import datetime
from dpymenus import Page, PaginatedMenu

utc_time = datetime.datetime.utcnow()

ranked_channel = 816348090223165490
bot_channel = 816349382055690310
talk_channels = [736031756251299942, 627184200382021642, 707672339109904516, 707672525093470319, 623489709510885386, 707673187886039122, 707673404865511424, 816346546710249474, 599905406591959052, 816347201424457798, 816347303547764748, 735496917936767017, 816347398019743784, 708592090271187002, 708592629272674325, 709019858054152252, 816347994983104582, 816348044148211722, 816348135986036826, 816348718659010560, 816348743602536508, 816348770438479932, 816348795280293889, 707726492611641405, 708441833964830780, 735998833770889338, 764154879252889640, 731299838934777907, 735918031485796356]

class help(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Help.py is ready.")

    @commands.group(invoke_without_command=True)
    async def help(self, ctx):
        if ctx.channel.id in talk_channels:
            embed = discord.Embed(description="You must do this command in the bot commands channel.", colour=discord.Colour.red())
            await ctx.channel.send(embed=embed)
        elif ctx.channel.id == ranked_channel:
            embed = discord.Embed(description="You must do this command in the bot commands channel.", colour=discord.Colour.red())
            await ctx.channel.send(embed=embed)
        else:
            embed = discord.Embed(title="__Galaxite Bot Help Menu__", description="Use `-help (command)` for more info on a command\nUse `-help (category)` for more info on a category", colour=discord.Colour.blue(), timestamp=datetime.datetime.utcnow())
            embed.add_field(name="Matchmaking", value="Ranked matchmaking commands\n`ranked`, `accept`, `done`, `joined`, `ban1`, `ban2`, `ban3`, `ban4`, `ban5`, `ban6`, `ban7`, `ban8`, `pick1`, `pick2`, `pick3`, `pick4`, `pick5`, `pick6`, `pick7`, `pick8`, `win`, `confirm`, `dispute`, `points`, `leaderboard`, `richest`", inline=False)
            embed.add_field(name="Levelling", value="Commands for checking yours and others server experience\n`rank`, `levels`, `pbc`", inline=False)
            embed.add_field(name="Fun", value="A range of random/fun commands\n`coin`, `roll`, `8ball`, `animal_fact`, `whois`", inline=False)
            embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}\u200b")
            embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/772494907960328193/03efcb6d1a7b856da38c6f1366014561.webp?size=1024")
            await ctx.send(embed=embed)

    @help.command()
    async def matchmaking(self, ctx: commands.Context):
        if ctx.channel.id in talk_channels:
            embed = discord.Embed(description="You must do this command in the bot commands channel.", colour=discord.Colour.red())
            await ctx.channel.send(embed=embed)
        elif ctx.channel.id == ranked_channel:
            embed = discord.Embed(description="You must do this command in the bot commands channel.", colour=discord.Colour.red())
            await ctx.channel.send(embed=embed)
        else:
            page1 = Page(title="__Matchmaking (Page 1/3)__", description="Ranked Matchmaking Commands", colour=discord.Colour.blue(), timestamp=datetime.datetime.utcnow())
            page1.add_field(name="-ranked", value="This command will request for a ranked match", inline=False)
            page1.add_field(name="-accept (@member)", value="This command will accept a ranked match request, please make sure the request is not expired", inline=False)
            page1.add_field(name="-done", value="Use this command once you have set up an arena and given the code to your opponent", inline=False)
            page1.add_field(name="-joined", value="Use this command once you have joined your opponent's arena", inline=False)
            page1.add_field(name="-ban1", value="This command will ban Final Destination during stage striking", inline=False)
            page1.add_field(name="-ban2", value="This command will ban Battlefield during stage striking",inline=False)
            page1.add_field(name="-ban3", value="This command will ban Pokémon Stadium 2 during stage striking",inline=False)
            page1.add_field(name="-ban4", value="This command will ban Smashville during stage striking",inline=False)
            page1.add_field(name="-ban5", value="This command will ban Town & City during stage striking",inline=False)
            page1.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}\u200b")
            page1.set_thumbnail(url="https://cdn.discordapp.com/avatars/772494907960328193/03efcb6d1a7b856da38c6f1366014561.webp?size=1024")
            page2 = Page(title="__Matchmaking (Page 2/3)__", description="Ranked Matchmaking Commands", colour=discord.Colour.blue(), timestamp=datetime.datetime.utcnow())
            page2.add_field(name="-ban6", value="This command will ban Kalos Pokémon League during stage striking",inline=False)
            page2.add_field(name="-ban7", value="This command will ban Lylat Cruise during stage striking",inline=False)
            page2.add_field(name="-ban8", value="This command will ban Yoshi's Story during stage striking",inline=False)
            page2.add_field(name="-pick1", value="This command will pick Final Destination during stage striking", inline=False)
            page2.add_field(name="-pick2", value="This command will pick Battlefield during stage striking", inline=False)
            page2.add_field(name="-pick3", value="This command will pick Pokémon Stadium 2 during stage striking", inline=False)
            page2.add_field(name="-pick4", value="This command will pick Smashville during stage striking", inline=False)
            page2.add_field(name="-pick5", value="This command will pick Town & City during stage striking", inline=False)
            page2.add_field(name="-pick6", value="This command will pick Kalos Pokémon League during stage striking", inline=False)
            page2.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}\u200b")
            page2.set_thumbnail(url="https://cdn.discordapp.com/avatars/772494907960328193/03efcb6d1a7b856da38c6f1366014561.webp?size=1024")
            page3 = Page(title="__Matchmaking (Page 3/3)__", description="Ranked Matchmaking Commands", colour=discord.Colour.blue(), timestamp=datetime.datetime.utcnow())
            page3.add_field(name="-pick7", value="This command will pick Lylat Cruise during stage striking", inline=False)
            page3.add_field(name="-pick8", value="This command will pick Yoshi's Story during stage striking", inline=False)
            page3.add_field(name="-win (@member)", value="This command is used to say who wins each match, either player can do this command", inline=False)
            page3.add_field(name="-confirm", value="This is to confirm that the person who did the '-win (@member)' command told the truth about who won", inline=False)
            page3.add_field(name="-dispute", value="This command is used to dispute the match result your opponent gave", inline=False)
            page3.add_field(name="-points (@member)", value="This command shows you your/others points balances", inline=False)
            page3.add_field(name="-leaderboard", value="This command shows you the top 10 players' points balances", inline=False)
            page3.add_field(name="-richest", value="This command shows you the richest player's points balance", inline=False)
            page3.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}\u200b")
            page3.set_thumbnail(url="https://cdn.discordapp.com/avatars/772494907960328193/03efcb6d1a7b856da38c6f1366014561.webp?size=1024")
            menu = PaginatedMenu(ctx)
            menu.add_pages([page1, page2, page3])
            menu.hide_cancel_button()
            menu.show_command_message()
            await menu.open()

    @help.command()
    async def levelling(self, ctx):
        if ctx.channel.id in talk_channels:
            embed = discord.Embed(description="You must do this command in the bot commands channel.", colour=discord.Colour.red())
            await ctx.channel.send(embed=embed)
        elif ctx.channel.id == ranked_channel:
            embed = discord.Embed(description="You must do this command in the bot commands channel.", colour=discord.Colour.red())
            await ctx.channel.send(embed=embed)
        else:
            embed = discord.Embed(title="__Levelling__", description="Levelling System Commands", colour=discord.Colour.blue(), timestamp=datetime.datetime.utcnow())
            embed.add_field(name="-rank (@member)", value="This command will display your/others level stats", inline=False)
            embed.add_field(name="-levels", value="This command will display the top 10 users' experience", inline=False)
            embed.add_field(name="-pbc (colour)", value="This command will change the colour of your progress bar on your level stats", inline=False)
            embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}\u200b")
            embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/772494907960328193/03efcb6d1a7b856da38c6f1366014561.webp?size=1024")
            await ctx.send(embed=embed)

    @help.command()
    async def fun(self, ctx):
        if ctx.channel.id in talk_channels:
            embed = discord.Embed(description="You must do this command in the bot commands channel.", colour=discord.Colour.red())
            await ctx.channel.send(embed=embed)
        elif ctx.channel.id == ranked_channel:
            embed = discord.Embed(description="You must do this command in the bot commands channel.", colour=discord.Colour.red())
            await ctx.channel.send(embed=embed)
        else:
            embed = discord.Embed(title="__Fun__", description="Fun/Miscellaneous Commands", colour=discord.Colour.blue(), timestamp=datetime.datetime.utcnow())
            embed.add_field(name="-coin", value="This command will flip a coin and return a value (heads or tales)", inline=False)
            embed.add_field(name="-roll (number)", value="This command will roll a die with the amount of sides entered", inline=False)
            embed.add_field(name="-8ball", value="This command will answer all questions you desire to ask", inline=False)
            embed.add_field(name="-animal_fact (animal)", value="This command will display a random fact about the given animal", inline=False)
            embed.add_field(name="-whois (@member)", value="This command will display information on the given user", inline=False)
            embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}\u200b")
            embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/772494907960328193/03efcb6d1a7b856da38c6f1366014561.webp?size=1024")
            await ctx.send(embed=embed)

    @help.command(aliases=["-ranked"])
    async def ranked(self, ctx):
        if ctx.channel.id in talk_channels:
            embed = discord.Embed(description="You must do this command in the bot commands channel.", colour=discord.Colour.red())
            await ctx.channel.send(embed=embed)
        elif ctx.channel.id == ranked_channel:
            embed = discord.Embed(description="You must do this command in the bot commands channel.", colour=discord.Colour.red())
            await ctx.channel.send(embed=embed)
        else:
            em = discord.Embed(title="-ranked", description="This command will request for a ranked match", colour=discord.Colour.blue(), timestamp=datetime.datetime.utcnow())
            em.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}\u200b")
            await ctx.send(embed=em)

    @help.command(aliases=["-accept", "accept (@member)" "-accept (@member)", "accept @member" "-accept @member", "accept member", "-accept member"])
    async def accept(self, ctx):
        if ctx.channel.id in talk_channels:
            embed = discord.Embed(description="You must do this command in the bot commands channel.", colour=discord.Colour.red())
            await ctx.channel.send(embed=embed)
        elif ctx.channel.id == ranked_channel:
            embed = discord.Embed(description="You must do this command in the bot commands channel.", colour=discord.Colour.red())
            await ctx.channel.send(embed=embed)
        else:
            em = discord.Embed(title="-accept (@member)", description="This command will accept a ranked match request, please make sure the request is not expired", colour=discord.Colour.blue(), timestamp=datetime.datetime.utcnow())
            em.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}\u200b")
            await ctx.send(embed=em)

    @help.command(aliases=["-done"])
    async def done(self, ctx):
        if ctx.channel.id in talk_channels:
            embed = discord.Embed(description="You must do this command in the bot commands channel.",
                                  colour=discord.Colour.red())
            await ctx.channel.send(embed=embed)
        elif ctx.channel.id == ranked_channel:
            embed = discord.Embed(description="You must do this command in the bot commands channel.",
                                  colour=discord.Colour.red())
            await ctx.channel.send(embed=embed)
        else:
            em = discord.Embed(title="-done", description="Use this command when you have set up an arena and given the code to your opponent", colour=discord.Colour.blue(), timestamp=datetime.datetime.utcnow())
            em.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}\u200b")
            await ctx.send(embed=em)

    @help.command(aliases=["-joined"])
    async def joined(self, ctx):
        if ctx.channel.id in talk_channels:
            embed = discord.Embed(description="You must do this command in the bot commands channel.",
                                  colour=discord.Colour.red())
            await ctx.channel.send(embed=embed)
        elif ctx.channel.id == ranked_channel:
            embed = discord.Embed(description="You must do this command in the bot commands channel.",
                                  colour=discord.Colour.red())
            await ctx.channel.send(embed=embed)
        else:
            em = discord.Embed(title="-joined", description="Use this command when you have joined your opponent's arena", colour=discord.Colour.blue(), timestamp=datetime.datetime.utcnow())
            em.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}\u200b")
            await ctx.send(embed=em)

    @help.command(aliases=["-ban1"])
    async def ban1(self, ctx):
        if ctx.channel.id in talk_channels:
            embed = discord.Embed(description="You must do this command in the bot commands channel.",
                                  colour=discord.Colour.red())
            await ctx.channel.send(embed=embed)
        elif ctx.channel.id == ranked_channel:
            embed = discord.Embed(description="You must do this command in the bot commands channel.",
                                  colour=discord.Colour.red())
            await ctx.channel.send(embed=embed)
        else:
            em = discord.Embed(title="-ban1", description="This command will ban Final Destination during stage striking", colour=discord.Colour.blue(), timestamp=datetime.datetime.utcnow())
            em.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}\u200b")
            await ctx.send(embed=em)

    @help.command(aliases=["-ban2"])
    async def ban2(self, ctx):
        if ctx.channel.id in talk_channels:
            embed = discord.Embed(description="You must do this command in the bot commands channel.",
                                  colour=discord.Colour.red())
            await ctx.channel.send(embed=embed)
        elif ctx.channel.id == ranked_channel:
            embed = discord.Embed(description="You must do this command in the bot commands channel.",
                                  colour=discord.Colour.red())
            await ctx.channel.send(embed=embed)
        else:
            em = discord.Embed(title="-ban2", description="This command will ban Battlefield during stage striking", colour=discord.Colour.blue(), timestamp=datetime.datetime.utcnow())
            em.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}\u200b")
            await ctx.send(embed=em)

    @help.command(aliases=["-ban3"])
    async def ban3(self, ctx):
        if ctx.channel.id in talk_channels:
            embed = discord.Embed(description="You must do this command in the bot commands channel.",
                                  colour=discord.Colour.red())
            await ctx.channel.send(embed=embed)
        elif ctx.channel.id == ranked_channel:
            embed = discord.Embed(description="You must do this command in the bot commands channel.",
                                  colour=discord.Colour.red())
            await ctx.channel.send(embed=embed)
        else:
            em = discord.Embed(title="-ban3", description="This command will ban Pokémon Stadium 2 during stage striking", colour=discord.Colour.blue(), timestamp=datetime.datetime.utcnow())
            em.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}\u200b")
            await ctx.send(embed=em)

    @help.command(aliases=["-ban4"])
    async def ban4(self, ctx):
        if ctx.channel.id in talk_channels:
            embed = discord.Embed(description="You must do this command in the bot commands channel.",
                                  colour=discord.Colour.red())
            await ctx.channel.send(embed=embed)
        elif ctx.channel.id == ranked_channel:
            embed = discord.Embed(description="You must do this command in the bot commands channel.",
                                  colour=discord.Colour.red())
            await ctx.channel.send(embed=embed)
        else:
            em = discord.Embed(title="-ban4", description="This command will ban Smashville during stage striking", colour=discord.Colour.blue(), timestamp=datetime.datetime.utcnow())
            em.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}\u200b")
            await ctx.send(embed=em)

    @help.command(aliases=["-ban5"])
    async def ban5(self, ctx):
        if ctx.channel.id in talk_channels:
            embed = discord.Embed(description="You must do this command in the bot commands channel.",
                                  colour=discord.Colour.red())
            await ctx.channel.send(embed=embed)
        elif ctx.channel.id == ranked_channel:
            embed = discord.Embed(description="You must do this command in the bot commands channel.",
                                  colour=discord.Colour.red())
            await ctx.channel.send(embed=embed)
        else:
            em = discord.Embed(title="-ban5", description="This command will ban Town & City during stage striking", colour=discord.Colour.blue(), timestamp=datetime.datetime.utcnow())
            em.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}\u200b")
            await ctx.send(embed=em)

    @help.command(aliases=["-ban6"])
    async def ban6(self, ctx):
        if ctx.channel.id in talk_channels:
            embed = discord.Embed(description="You must do this command in the bot commands channel.",
                                  colour=discord.Colour.red())
            await ctx.channel.send(embed=embed)
        elif ctx.channel.id == ranked_channel:
            embed = discord.Embed(description="You must do this command in the bot commands channel.",
                                  colour=discord.Colour.red())
            await ctx.channel.send(embed=embed)
        else:
            em = discord.Embed(title="-ban6", description="This command will ban Kalos Pokémon League during stage striking", colour=discord.Colour.blue(), timestamp=datetime.datetime.utcnow())
            em.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}\u200b")
            await ctx.send(embed=em)

    @help.command(aliases=["-ban7"])
    async def ban7(self, ctx):
        if ctx.channel.id in talk_channels:
            embed = discord.Embed(description="You must do this command in the bot commands channel.",
                                  colour=discord.Colour.red())
            await ctx.channel.send(embed=embed)
        elif ctx.channel.id == ranked_channel:
            embed = discord.Embed(description="You must do this command in the bot commands channel.",
                                  colour=discord.Colour.red())
            await ctx.channel.send(embed=embed)
        else:
            em = discord.Embed(title="-ban7", description="This command will ban Lylat Cruise during stage striking", colour=discord.Colour.blue(), timestamp=datetime.datetime.utcnow())
            em.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}\u200b")
            await ctx.send(embed=em)

    @help.command(aliases=["-ban8"])
    async def ban8(self, ctx):
        if ctx.channel.id in talk_channels:
            embed = discord.Embed(description="You must do this command in the bot commands channel.",
                                  colour=discord.Colour.red())
            await ctx.channel.send(embed=embed)
        elif ctx.channel.id == ranked_channel:
            embed = discord.Embed(description="You must do this command in the bot commands channel.",
                                  colour=discord.Colour.red())
            await ctx.channel.send(embed=embed)
        else:
            em = discord.Embed(title="-ban8", description="This command will ban Yoshi's Story during stage striking", colour=discord.Colour.blue(), timestamp=datetime.datetime.utcnow())
            em.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}\u200b")
            await ctx.send(embed=em)

    @help.command(aliases=["-pick1"])
    async def pick1(self, ctx):
        if ctx.channel.id in talk_channels:
            embed = discord.Embed(description="You must do this command in the bot commands channel.",
                                  colour=discord.Colour.red())
            await ctx.channel.send(embed=embed)
        elif ctx.channel.id == ranked_channel:
            embed = discord.Embed(description="You must do this command in the bot commands channel.",
                                  colour=discord.Colour.red())
            await ctx.channel.send(embed=embed)
        else:
            em = discord.Embed(title="-pick1", description="This command will pick Final Destination during stage striking", colour=discord.Colour.blue(), timestamp=datetime.datetime.utcnow())
            em.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}\u200b")
            await ctx.send(embed=em)

    @help.command(aliases=["-pick2"])
    async def pick2(self, ctx):
        if ctx.channel.id in talk_channels:
            embed = discord.Embed(description="You must do this command in the bot commands channel.",
                                  colour=discord.Colour.red())
            await ctx.channel.send(embed=embed)
        elif ctx.channel.id == ranked_channel:
            embed = discord.Embed(description="You must do this command in the bot commands channel.",
                                  colour=discord.Colour.red())
            await ctx.channel.send(embed=embed)
        else:
            em = discord.Embed(title="-pick2", description="This command will pick Battlefield during stage striking", colour=discord.Colour.blue(), timestamp=datetime.datetime.utcnow())
            em.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}\u200b")
            await ctx.send(embed=em)

    @help.command(aliases=["-pick3"])
    async def pick3(self, ctx):
        if ctx.channel.id in talk_channels:
            embed = discord.Embed(description="You must do this command in the bot commands channel.",
                                  colour=discord.Colour.red())
            await ctx.channel.send(embed=embed)
        elif ctx.channel.id == ranked_channel:
            embed = discord.Embed(description="You must do this command in the bot commands channel.",
                                  colour=discord.Colour.red())
            await ctx.channel.send(embed=embed)
        else:
            em = discord.Embed(title="-pick3", description="This command will pick Pokémon Stadium 2 during stage striking", colour=discord.Colour.blue(), timestamp=datetime.datetime.utcnow())
            em.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}\u200b")
            await ctx.send(embed=em)

    @help.command(aliases=["-pick4"])
    async def pick4(self, ctx):
        if ctx.channel.id in talk_channels:
            embed = discord.Embed(description="You must do this command in the bot commands channel.",
                                  colour=discord.Colour.red())
            await ctx.channel.send(embed=embed)
        elif ctx.channel.id == ranked_channel:
            embed = discord.Embed(description="You must do this command in the bot commands channel.",
                                  colour=discord.Colour.red())
            await ctx.channel.send(embed=embed)
        else:
            em = discord.Embed(title="-pick4", description="This command will pick Smashville during stage striking", colour=discord.Colour.blue(), timestamp=datetime.datetime.utcnow())
            em.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}\u200b")
            await ctx.send(embed=em)

    @help.command(aliases=["-pick5"])
    async def pick5(self, ctx):
        if ctx.channel.id in talk_channels:
            embed = discord.Embed(description="You must do this command in the bot commands channel.",
                                  colour=discord.Colour.red())
            await ctx.channel.send(embed=embed)
        elif ctx.channel.id == ranked_channel:
            embed = discord.Embed(description="You must do this command in the bot commands channel.",
                                  colour=discord.Colour.red())
            await ctx.channel.send(embed=embed)
        else:
            em = discord.Embed(title="-pick5", description="This command will pick Town & City during stage striking", colour=discord.Colour.blue(), timestamp=datetime.datetime.utcnow())
            em.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}\u200b")
            await ctx.send(embed=em)

    @help.command(aliases=["-pick6"])
    async def pick6(self, ctx):
        if ctx.channel.id in talk_channels:
            embed = discord.Embed(description="You must do this command in the bot commands channel.",
                                  colour=discord.Colour.red())
            await ctx.channel.send(embed=embed)
        elif ctx.channel.id == ranked_channel:
            embed = discord.Embed(description="You must do this command in the bot commands channel.",
                                  colour=discord.Colour.red())
            await ctx.channel.send(embed=embed)
        else:
            em = discord.Embed(title="-pick6", description="This command will pick Kalos Pokémon League during stage striking", colour=discord.Colour.blue(), timestamp=datetime.datetime.utcnow())
            em.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}\u200b")
            await ctx.send(embed=em)

    @help.command(aliases=["-pick7"])
    async def pick7(self, ctx):
        if ctx.channel.id in talk_channels:
            embed = discord.Embed(description="You must do this command in the bot commands channel.",
                                  colour=discord.Colour.red())
            await ctx.channel.send(embed=embed)
        elif ctx.channel.id == ranked_channel:
            embed = discord.Embed(description="You must do this command in the bot commands channel.",
                                  colour=discord.Colour.red())
            await ctx.channel.send(embed=embed)
        else:
            em = discord.Embed(title="-pick7", description="This command will pick Lylat Cruise during stage striking", colour=discord.Colour.blue(), timestamp=datetime.datetime.utcnow())
            em.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}\u200b")
            await ctx.send(embed=em)

    @help.command(aliases=["-pick8"])
    async def pick8(self, ctx):
        if ctx.channel.id in talk_channels:
            embed = discord.Embed(description="You must do this command in the bot commands channel.",
                                  colour=discord.Colour.red())
            await ctx.channel.send(embed=embed)
        elif ctx.channel.id == ranked_channel:
            embed = discord.Embed(description="You must do this command in the bot commands channel.",
                                  colour=discord.Colour.red())
            await ctx.channel.send(embed=embed)
        else:
            em = discord.Embed(title="-pick8", description="This command will pick Yoshi's Story during stage striking", colour=discord.Colour.blue(), timestamp=datetime.datetime.utcnow())
            em.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}\u200b")
            await ctx.send(embed=em)

    @help.command(aliases=["-win", "win (@member)" "-win (@member)", "win @member" "-win @member", "win member", "-win member"])
    async def win(self, ctx):
        if ctx.channel.id in talk_channels:
            embed = discord.Embed(description="You must do this command in the bot commands channel.",
                                  colour=discord.Colour.red())
            await ctx.channel.send(embed=embed)
        elif ctx.channel.id == ranked_channel:
            embed = discord.Embed(description="You must do this command in the bot commands channel.",
                                  colour=discord.Colour.red())
            await ctx.channel.send(embed=embed)
        else:
            em = discord.Embed(title="-win (@member)", description="This command is used to say who wins each match, either player can do this command", colour=discord.Colour.blue(), timestamp=datetime.datetime.utcnow())
            em.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}\u200b")
            await ctx.send(embed=em)

    @help.command(aliases=["-confirm"])
    async def confirm(self, ctx):
        if ctx.channel.id in talk_channels:
            embed = discord.Embed(description="You must do this command in the bot commands channel.",
                                  colour=discord.Colour.red())
            await ctx.channel.send(embed=embed)
        elif ctx.channel.id == ranked_channel:
            embed = discord.Embed(description="You must do this command in the bot commands channel.",
                                  colour=discord.Colour.red())
            await ctx.channel.send(embed=embed)
        else:
            em = discord.Embed(title="-confirm", description="This is to confirm that the person who did the '-win (@member)' command told the truth about who won", colour=discord.Colour.blue(), timestamp=datetime.datetime.utcnow())
            em.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}\u200b")
            await ctx.send(embed=em)

    @help.command(aliases=["-dispute"])
    async def dispute(self, ctx):
        if ctx.channel.id in talk_channels:
            embed = discord.Embed(description="You must do this command in the bot commands channel.",
                                  colour=discord.Colour.red())
            await ctx.channel.send(embed=embed)
        elif ctx.channel.id == ranked_channel:
            embed = discord.Embed(description="You must do this command in the bot commands channel.",
                                  colour=discord.Colour.red())
            await ctx.channel.send(embed=embed)
        else:
            em = discord.Embed(title="-dispute", description="This command is used to dispute the match result your opponent gave", colour=discord.Colour.blue(), timestamp=datetime.datetime.utcnow())
            em.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}\u200b")
            await ctx.send(embed=em)

    @help.command(aliases=["-points", "points (@member)" "-points (@member)", "points @member" "-points @member", "points member", "-points member"])
    async def points(self, ctx):
        if ctx.channel.id in talk_channels:
            embed = discord.Embed(description="You must do this command in the bot commands channel.",
                                  colour=discord.Colour.red())
            await ctx.channel.send(embed=embed)
        elif ctx.channel.id == ranked_channel:
            embed = discord.Embed(description="You must do this command in the bot commands channel.",
                                  colour=discord.Colour.red())
            await ctx.channel.send(embed=embed)
        else:
            em = discord.Embed(title="-points", description="This command shows you your/others points balances", colour=discord.Colour.blue(), timestamp=datetime.datetime.utcnow())
            em.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}\u200b")
            await ctx.send(embed=em)

    @help.command(aliases=["-leaderboard", "lb", "-lb"])
    async def leaderboard(self, ctx):
        if ctx.channel.id in talk_channels:
            embed = discord.Embed(description="You must do this command in the bot commands channel.",
                                  colour=discord.Colour.red())
            await ctx.channel.send(embed=embed)
        elif ctx.channel.id == ranked_channel:
            embed = discord.Embed(description="You must do this command in the bot commands channel.",
                                  colour=discord.Colour.red())
            await ctx.channel.send(embed=embed)
        else:
            em = discord.Embed(title="-leaderboard", description="This command shows you the top 10 players' points balances", colour=discord.Colour.blue(), timestamp=datetime.datetime.utcnow())
            em.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}\u200b")
            await ctx.send(embed=em)

    @help.command(aliases=["-richest"])
    async def richest(self, ctx):
        if ctx.channel.id in talk_channels:
            embed = discord.Embed(description="You must do this command in the bot commands channel.",
                                  colour=discord.Colour.red())
            await ctx.channel.send(embed=embed)
        elif ctx.channel.id == ranked_channel:
            embed = discord.Embed(description="You must do this command in the bot commands channel.",
                                  colour=discord.Colour.red())
            await ctx.channel.send(embed=embed)
        else:
            em = discord.Embed(title="-richest", description="This command shows you the richest players points balance", colour=discord.Colour.blue(), timestamp=datetime.datetime.utcnow())
            em.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}\u200b")
            await ctx.send(embed=em)

    @help.command(aliases=["-rank", "rank (@member)" "-rank (@member)", "rank @member" "-rank @member", "rank member", "-rank member"])
    async def rank(self, ctx):
        if ctx.channel.id in talk_channels:
            embed = discord.Embed(description="You must do this command in the bot commands channel.",
                                  colour=discord.Colour.red())
            await ctx.channel.send(embed=embed)
        elif ctx.channel.id == ranked_channel:
            embed = discord.Embed(description="You must do this command in the bot commands channel.",
                                  colour=discord.Colour.red())
            await ctx.channel.send(embed=embed)
        else:
            em = discord.Embed(title="-rank (@member)", description="This command will display your/others level stats", colour=discord.Colour.blue(), timestamp=datetime.datetime.utcnow())
            em.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}\u200b")
            await ctx.send(embed=em)

    @help.command(aliases=["-levels"])
    async def levels(self, ctx):
        if ctx.channel.id in talk_channels:
            embed = discord.Embed(description="You must do this command in the bot commands channel.",
                                  colour=discord.Colour.red())
            await ctx.channel.send(embed=embed)
        elif ctx.channel.id == ranked_channel:
            embed = discord.Embed(description="You must do this command in the bot commands channel.",
                                  colour=discord.Colour.red())
            await ctx.channel.send(embed=embed)
        else:
            em = discord.Embed(title="-levels", description="This command will display the top 10 users' experience", colour=discord.Colour.blue(), timestamp=datetime.datetime.utcnow())
            em.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}\u200b")
            await ctx.send(embed=em)

    @help.command(aliases=["-pbc", "pbc (colour)", "-pbc (colour)", "pbc colour", "-pbc colour", "progressbarcolour", "-progressbarcolour", "progressbarcolour (colour)", "-progressbarcolour (colour)", "progressbarcolour colour", "-progressbarcolour colour", "progress_bar_colour", "-progress_bar_colour", "progress_bar_colour (colour)", "-progress_bar_colour (colour)", "progress_bar_colour colour", "-progress_bar_colour colour", "pbcolour", "-pbcolour", "pbcolour (colour)", "-pbcolour (colour)", "pbcolour colour", "-pbcolour colour", "progressbarcolor", "-progressbarcolor", "progressbarcolor (colour)", "-progressbarcolor (colour)", "progressbarcolor colour", "-progressbarcolor colour", "progress_bar_color", "-progress_bar_color", "progress_bar_color (colour)", "-progress_bar_color (colour)", "progress_bar_color colour", "-progress_bar_color colour", "-pbcolor", "pbcolor (colour)", "-pbcolor (colour)", "pbcolor colour", "progressbarcolour (color)", "-progressbarcolour (color)", "progressbarcolour color", "-progressbarcolour color", "progress_bar_colour (color)", "-progress_bar_colour (color)", "progress_bar_colour color", "-progress_bar_colour color", "pbcolour (color)", "-pbcolour (color)", "pbcolour color", "-pbcolour color", "progressbarcolor (color)", "-progressbarcolor (color)", "progressbarcolor color", "-progressbarcolor color", "progress_bar_color (color)", "-progress_bar_color (color)", "progress_bar_color color", "-progress_bar_color color", "pbcolor (color)", "-pbcolor (color)", "pbcolor color"])
    async def pbc(self, ctx):
        if ctx.channel.id in talk_channels:
            embed = discord.Embed(description="You must do this command in the bot commands channel.",
                                  colour=discord.Colour.red())
            await ctx.channel.send(embed=embed)
        elif ctx.channel.id == ranked_channel:
            embed = discord.Embed(description="You must do this command in the bot commands channel.",
                                  colour=discord.Colour.red())
            await ctx.channel.send(embed=embed)
        else:
            em = discord.Embed(title="-pbc (colour)", description="This command will change the colour of your progress bar on your level stats", colour=discord.Colour.blue(), timestamp=datetime.datetime.utcnow())
            em.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}\u200b")
            await ctx.send(embed=em)

    @help.command(aliases=["-coin", "flip", "-flip"])
    async def coin(self, ctx):
        if ctx.channel.id in talk_channels:
            embed = discord.Embed(description="You must do this command in the bot commands channel.",
                                  colour=discord.Colour.red())
            await ctx.channel.send(embed=embed)
        elif ctx.channel.id == ranked_channel:
            embed = discord.Embed(description="You must do this command in the bot commands channel.",
                                  colour=discord.Colour.red())
            await ctx.channel.send(embed=embed)
        else:
            em = discord.Embed(title="-coin", description="This command will flip a coin and return a value (heads or tales)", colour=discord.Colour.blue(), timestamp=datetime.datetime.utcnow())
            em.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}\u200b")
            await ctx.send(embed=em)

    @help.command(aliases=["-roll", "roll (number)", "-roll (number)", "roll number", "-roll number", "die", "-die", "die (number)", "-die (number)", "die number", "-die number", "dice", "-dice", "dice (number)", "-dice (number)", "dice number", "-dice number"])
    async def roll(self, ctx):
        if ctx.channel.id in talk_channels:
            embed = discord.Embed(description="You must do this command in the bot commands channel.",
                                  colour=discord.Colour.red())
            await ctx.channel.send(embed=embed)
        elif ctx.channel.id == ranked_channel:
            embed = discord.Embed(description="You must do this command in the bot commands channel.",
                                  colour=discord.Colour.red())
            await ctx.channel.send(embed=embed)
        else:
            em = discord.Embed(title="-roll (number)", description="This command will roll a die with the amount of sides entered", colour=discord.Colour.blue(), timestamp=datetime.datetime.utcnow())
            em.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}\u200b")
            await ctx.send(embed=em)

    @help.command(aliases=["-eight_ball", "8ball", "-8ball", "eightball", "-eightball", "8_ball", "-8_ball"])
    async def eight_ball(self, ctx):
        if ctx.channel.id in talk_channels:
            embed = discord.Embed(description="You must do this command in the bot commands channel.",
                                  colour=discord.Colour.red())
            await ctx.channel.send(embed=embed)
        elif ctx.channel.id == ranked_channel:
            embed = discord.Embed(description="You must do this command in the bot commands channel.",
                                  colour=discord.Colour.red())
            await ctx.channel.send(embed=embed)
        else:
            em = discord.Embed(title="-8ball", description="This command will answer all questions you desire to ask", colour=discord.Colour.blue(), timestamp=datetime.datetime.utcnow())
            em.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}\u200b")
            await ctx.send(embed=em)

    @help.command(aliases=["-animal_fact", "animal_fact (animal)", "-animal_fact (animal)", "animal_fact animal", "-animal_fact animal", "animalfact", "-animalfact", "animalfact (animal)", "-animalfact (animal)", "animalfact animal", "-animalfact animal", "af", "-af", "af (animal)", "-af (animal)", "af animal", "-af animal"])
    async def animal_fact(self, ctx):
        if ctx.channel.id in talk_channels:
            embed = discord.Embed(description="You must do this command in the bot commands channel.",
                                  colour=discord.Colour.red())
            await ctx.channel.send(embed=embed)
        elif ctx.channel.id == ranked_channel:
            embed = discord.Embed(description="You must do this command in the bot commands channel.",
                                  colour=discord.Colour.red())
            await ctx.channel.send(embed=embed)
        else:
            em = discord.Embed(title="-animal_fact (animal)", description="This command will display a random fact about the given animal", colour=discord.Colour.blue(), timestamp=datetime.datetime.utcnow())
            em.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}\u200b")
            await ctx.send(embed=em)

    @help.command(aliases=["-whois", "whois (@member)", "-whois (@member)", "whois @member", "-whois @member", "whois member", "-whois member", "userinfo", "-userinfo", "userinfo (@member)", "-userinfo (@member)", "userinfo @member", "-userinfo @member", "userinfo member", "-userinfo member", "-memberinfo", "memberinfo (@member)", "-memberinfo (@member)", "memberinfo @member", "-memberinfo @member", "memberinfo member", "-memberinfo member", "memberinfo", "ui", "-ui", "ui (@member)", "-ui (@member)", "ui @member", "-ui @member", "ui member", "-ui member", "mi", "-mi", "mi (@member)", "-mi (@member)", "mi @member", "-mi @member", "mi member", "-mi member", "user_info", "-user_info", "user_info (@member)", "-user_info (@member)", "user_info @member", "-user_info @member", "user_info member", "-user_info member", "member_info", "-member_info", "member_info (@member)", "-member_info (@member)", "member_info @member", "-member_info @member", "member_info member", "-member_info member"])
    async def whois(self, ctx):
        if ctx.channel.id in talk_channels:
            embed = discord.Embed(description="You must do this command in the bot commands channel.",
                                  colour=discord.Colour.red())
            await ctx.channel.send(embed=embed)
        elif ctx.channel.id == ranked_channel:
            embed = discord.Embed(description="You must do this command in the bot commands channel.",
                                  colour=discord.Colour.red())
            await ctx.channel.send(embed=embed)
        else:
            em = discord.Embed(title="-whois (@member)", description="This command will display information on the given user", colour=discord.Colour.blue(), timestamp=datetime.datetime.utcnow())
            em.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}\u200b")
            await ctx.send(embed=em)

def setup(client):
    client.add_cog(help(client))
