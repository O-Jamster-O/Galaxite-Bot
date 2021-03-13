import discord
import datetime
from discord.ext import commands
from discord.utils import get
from pymongo import MongoClient

utc_time = datetime.datetime.utcnow()

ranked_channel = 816348090223165490
bot_channel = 816349382055690310
talk_channels = [736031756251299942, 627184200382021642, 707672339109904516, 707672525093470319, 623489709510885386, 707673187886039122, 707673404865511424, 816346546710249474, 599905406591959052, 816347201424457798, 816347303547764748, 735496917936767017, 816347398019743784, 708592090271187002, 708592629272674325, 709019858054152252, 816347994983104582, 816348044148211722, 816348135986036826, 816348718659010560, 816348743602536508, 816348770438479932, 816348795280293889, 707726492611641405, 708441833964830780, 735998833770889338, 764154879252889640, 731299838934777907, 735918031485796356]

level = ["Level 5", "Level 10", "Level 15"]
levelnum = [5, 10, 15]

cluster = MongoClient("mongodb+srv://Jamster:tigertim@cluster0.goj1e.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

levelling = cluster["discord"]["levelling"]

class levelsys(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Levelsys.py is ready.")

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.channel.id in talk_channels:
            stats = levelling.find_one({"id": message.author.id})
            if not message.author.bot:
                if stats is None:
                    newuser = {"id": message.author.id, "xp": 0, "pbcolour": ":blue_square:"}
                    levelling.insert_one(newuser)
                else:
                    xp = stats["xp"] + 5
                    levelling.update_one({"id": message.author.id}, {"$set":{"xp": xp}})
                    lvl = 0
                    while True:
                        if xp < ((50*(lvl**2))+(50*(lvl-1))):
                            break
                        lvl += 1
                    xp -= ((50*((lvl-1)**2))+(50*(lvl-1)))
                    if xp == 0:
                        await message.channel.send(f"Well done {message.author.mention}! You've leveled up to **level {lvl}**!")
                        for i in range(len(level)):
                            if lvl == levelnum[i]:
                                await message.author.add_roles(discord.utils.get(message.author.guild.roles, name=level[i]))
                                role = get(message.guild.roles, name=level[i])
                                embed = discord.Embed(description=f"{message.author.mention} you have recieved the **{role}** role!!!", colour=discord.Colour.green(), timestamp=datetime.datetime.utcnow())
                                await message.channel.send(embed=embed)

    @commands.command()
    async def rank(self, ctx, member: discord.Member = None):
        if ctx.channel.id in talk_channels:
            embed = discord.Embed(description="You must do this command in the bot commands channel.", colour=discord.Colour.red())
            await ctx.channel.send(embed=embed)
        elif ctx.channel.id == ranked_channel:
            embed = discord.Embed(description="You must do this command in the bot commands channel.", colour=discord.Colour.red())
            await ctx.channel.send(embed=embed)
        elif member == None:
            if ctx.channel.id == bot_channel:
                stats = levelling.find_one({"id": ctx.author.id})
                if stats is None:
                    embed = discord.Embed(description="You haven't sent any messages, so you do not have a rank.", colour=discord.Colour.red())
                    await ctx.channel.send(embed=embed)
                else:
                    xp = stats["xp"]
                    lvl = 0
                    rank = 0
                    while True:
                            if xp < ((50 * (lvl ** 2)) + (50 * (lvl - 1))):
                                break
                            lvl += 1
                    xp -= ((50 * ((lvl - 1) ** 2)) + (50 * (lvl - 1)))
                    boxes = int((xp/(200*((1/2)*lvl)))*10)
                    rankings = levelling.find().sort("xp", -1)
                    if lvl >= 15:
                        role = get(ctx.guild.roles, name="Level 15")
                        rolemention = role.mention
                    elif lvl >= 10:
                        role = get(ctx.guild.roles, name="Level 10")
                        rolemention = role.mention
                    elif lvl >= 5:
                        role = get(ctx.guild.roles, name="Level 5")
                        rolemention = role.mention
                    else:
                        rolemention = "N/A"
                    for x in rankings:
                        rank += 1
                        if stats["id"] == x["id"]:
                            break
                    embed = discord.Embed(title="__{}'s Level Stats__".format(ctx.author.name), colour=discord.Colour.blue(), timestamp=datetime.datetime.utcnow())
                    embed.add_field(name="Name:", value=ctx.author.mention, inline=True)
                    embed.add_field(name="Level:", value=lvl, inline=True)
                    embed.add_field(name="XP:", value=f"{xp}/{int(200*((1/2)*lvl))}", inline=True)
                    embed.add_field(name="Rank:", value=f"{rank}/{ctx.guild.member_count}", inline=True)
                    embed.add_field(name="Highest Level Role:", value=rolemention, inline=True)
                    embed.add_field(name="Progress Bar:", value=boxes*stats["pbcolour"]+(10-boxes)*":white_large_square:", inline=False)
                    embed.set_thumbnail(url=ctx.author.avatar_url)
                    embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}\u200b")
                    await ctx.channel.send(embed=embed)
        else:
            if ctx.channel.id in talk_channels:
                embed = discord.Embed(description="You must do this command in the bot commands channel.",
                                      colour=discord.Colour.red())
                await ctx.channel.send(embed=embed)
            elif ctx.channel.id == ranked_channel:
                embed = discord.Embed(description="You must do this command in the bot commands channel.",
                                      colour=discord.Colour.red())
                await ctx.channel.send(embed=embed)
            elif ctx.channel.id == bot_channel:
                stats = levelling.find_one({"id": member.id})
                if stats is None:
                    embed = discord.Embed(description="This member hasn't sent any messages, so they do not have a rank.", colour=discord.Colour.red())
                    await ctx.channel.send(embed=embed)
                else:
                    xp = stats["xp"]
                    lvl = 0
                    rank = 0
                    while True:
                            if xp < ((50 * (lvl ** 2)) + (50 * (lvl - 1))):
                                break
                            lvl += 1
                    xp -= ((50 * ((lvl - 1) ** 2)) + (50 * (lvl - 1)))
                    boxes = int((xp/(200*((1/2)*lvl)))*10)
                    rankings = levelling.find().sort("xp", -1)
                    if lvl >= 15:
                        role = get(ctx.guild.roles, name="Level 15")
                        rolemention = role.mention
                    elif lvl >= 10:
                        role = get(ctx.guild.roles, name="Level 10")
                        rolemention = role.mention
                    elif lvl >= 5:
                        role = get(ctx.guild.roles, name="Level 5")
                        rolemention = role.mention
                    else:
                        rolemention = "N/A"
                    for x in rankings:
                        rank += 1
                        if stats["id"] == x["id"]:
                            break
                    embed = discord.Embed(title="__{}'s Level Stats__".format(ctx.author.name), colour=discord.Colour.blue(), timestamp=datetime.datetime.utcnow())
                    embed.add_field(name="Name:", value=member.mention, inline=True)
                    embed.add_field(name="Level:", value=lvl, inline=True)
                    embed.add_field(name="XP:", value=f"{xp}/{int(200*((1/2)*lvl))}", inline=True)
                    embed.add_field(name="Rank:", value=f"{rank}/{ctx.guild.member_count}", inline=True)
                    embed.add_field(name="Highest Level Role:", value=rolemention, inline=True)
                    embed.add_field(name="Progress Bar:", value=boxes*stats["pbcolour"]+(10-boxes)*":white_large_square:", inline=False)
                    embed.set_thumbnail(url=member.avatar_url)
                    embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}\u200b")
                    await ctx.channel.send(embed=embed)

    @commands.command(aliases=["progressbarcolour", "progress_bar_colour", "pbcolour", "progressbarcolor", "progress_bar_color", "pbcolor"])
    async def pbc(self, ctx, colour = None):
        if ctx.channel.id in talk_channels:
            embed = discord.Embed(description="You must do this command in the bot commands channel.", colour=discord.Colour.red())
            await ctx.channel.send(embed=embed)
        elif ctx.channel.id == ranked_channel:
            embed = discord.Embed(description="You must do this command in the bot commands channel.", colour=discord.Colour.red())
            await ctx.channel.send(embed=embed)
        elif ctx.channel.id == bot_channel:
            if colour == "zsd,fgkzbsdkfbusgrfb743tws7irfge78awozubds":
                embed = discord.Embed(description="You must enter your desired colour, for example '-pbc (colour)'. The available colours are: red, orange, yellow, green, blue, purple, brown and black.", colour=discord.Colour.red())
                await ctx.send(embed=embed)
            elif colour == None:
                embed = discord.Embed(description="You must enter your desired colour, for example '-pbc (colour)'. The available colours are: red, orange, yellow, green, blue, purple, brown and black.", colour=discord.Colour.red())
                await ctx.send(embed=embed)
            elif colour == "Red":
                levelling.find_one({"id": ctx.author.id})
                levelling.update_one({"id": ctx.author.id}, {"$set":{"pbcolour": ":red_square:"}})
                embed = discord.Embed(description="Your progress bar colour has now been set to red.", colour=discord.Colour.green())
                await ctx.send(embed=embed)
            elif colour == "red":
                levelling.find_one({"id": ctx.author.id})
                levelling.update_one({"id": ctx.author.id}, {"$set":{"pbcolour": ":red_square:"}})
                embed = discord.Embed(description="Your progress bar colour has now been set to red.", colour=discord.Colour.green())
                await ctx.send(embed=embed)
            elif colour == "Orange":
                levelling.find_one({"id": ctx.author.id})
                levelling.update_one({"id": ctx.author.id}, {"$set":{"pbcolour": ":orange_square:"}})
                embed = discord.Embed(description="Your progress bar colour has now been set to orange.", colour=discord.Colour.green())
                await ctx.send(embed=embed)
            elif colour == "orange":
                levelling.find_one({"id": ctx.author.id})
                levelling.update_one({"id": ctx.author.id}, {"$set":{"pbcolour": ":orange_square:"}})
                embed = discord.Embed(description="Your progress bar colour has now been set to orange.", colour=discord.Colour.green())
                await ctx.send(embed=embed)
            elif colour == "Yellow":
                levelling.find_one({"id": ctx.author.id})
                levelling.update_one({"id": ctx.author.id}, {"$set":{"pbcolour": ":yellow_square:"}})
                embed = discord.Embed(description="Your progress bar colour has now been set to yellow.", colour=discord.Colour.green())
                await ctx.send(embed=embed)
            elif colour == "yellow":
                levelling.find_one({"id": ctx.author.id})
                levelling.update_one({"id": ctx.author.id}, {"$set":{"pbcolour": ":yellow_square:"}})
                embed = discord.Embed(description="Your progress bar colour has now been set to yellow.", colour=discord.Colour.green())
                await ctx.send(embed=embed)
            elif colour == "Green":
                levelling.find_one({"id": ctx.author.id})
                levelling.update_one({"id": ctx.author.id}, {"$set":{"pbcolour": ":green_square:"}})
                embed = discord.Embed(description="Your progress bar colour has now been set to green.", colour=discord.Colour.green())
                await ctx.send(embed=embed)
            elif colour == "green":
                levelling.find_one({"id": ctx.author.id})
                levelling.update_one({"id": ctx.author.id}, {"$set":{"pbcolour": ":green_square:"}})
                embed = discord.Embed(description="Your progress bar colour has now been set to green.", colour=discord.Colour.green())
                await ctx.send(embed=embed)
            elif colour == "Blue":
                levelling.find_one({"id": ctx.author.id})
                levelling.update_one({"id": ctx.author.id}, {"$set":{"pbcolour": ":blue_square:"}})
                embed = discord.Embed(description="Your progress bar colour has now been set to blue.", colour=discord.Colour.green())
                await ctx.send(embed=embed)
            elif colour == "blue":
                levelling.find_one({"id": ctx.author.id})
                levelling.update_one({"id": ctx.author.id}, {"$set":{"pbcolour": ":blue_square:"}})
                embed = discord.Embed(description="Your progress bar colour has now been set to blue.", colour=discord.Colour.green())
                await ctx.send(embed=embed)
            elif colour == "Purple":
                levelling.find_one({"id": ctx.author.id})
                levelling.update_one({"id": ctx.author.id}, {"$set":{"pbcolour": ":purple_square:"}})
                embed = discord.Embed(description="Your progress bar colour has now been set to purple.", colour=discord.Colour.green())
                await ctx.send(embed=embed)
            elif colour == "purple":
                levelling.find_one({"id": ctx.author.id})
                levelling.update_one({"id": ctx.author.id}, {"$set":{"pbcolour": ":purple_square:"}})
                embed = discord.Embed(description="Your progress bar colour has now been set to purple.", colour=discord.Colour.green())
                await ctx.send(embed=embed)
            elif colour == "Brown":
                levelling.find_one({"id": ctx.author.id})
                levelling.update_one({"id": ctx.author.id}, {"$set":{"pbcolour": ":brown_square:"}})
                embed = discord.Embed(description="Your progress bar colour has now been set to brown.", colour=discord.Colour.green())
                await ctx.send(embed=embed)
            elif colour == "brown":
                levelling.find_one({"id": ctx.author.id})
                levelling.update_one({"id": ctx.author.id}, {"$set":{"pbcolour": ":brown_square:"}})
                embed = discord.Embed(description="Your progress bar colour has now been set to brown.", colour=discord.Colour.green())
                await ctx.send(embed=embed)
            elif colour == "Black":
                levelling.find_one({"id": ctx.author.id})
                levelling.update_one({"id": ctx.author.id}, {"$set":{"pbcolour": ":black_large_square:"}})
                embed = discord.Embed(description="Your progress bar colour has now been set to black.", colour=discord.Colour.green())
                await ctx.send(embed=embed)
            elif colour == "black":
                levelling.find_one({"id": ctx.author.id})
                levelling.update_one({"id": ctx.author.id}, {"$set":{"pbcolour": ":black_large_square:"}})
                embed = discord.Embed(description="Your progress bar colour has now been set to black.", colour=discord.Colour.green())
                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(description="You must enter your desired colour, for example '-pbc (colour)'. The available colours are: red, orange, yellow, green, blue, purple, brown and black.", colour=discord.Colour.red())
                await ctx.send(embed=embed)

    @commands.command()
    async def levels(self, ctx):
        if ctx.channel.id in talk_channels:
            embed = discord.Embed(description="You must do this command in the bot commands channel.", colour=discord.Colour.red())
            await ctx.channel.send(embed=embed)
        elif ctx.channel.id == ranked_channel:
            embed = discord.Embed(description="You must do this command in the bot commands channel.", colour=discord.Colour.red())
            await ctx.channel.send(embed=embed)
        elif ctx.channel.id == bot_channel:
            rankings = levelling.find().sort("xp", -1)
            i = 1
            embed = discord.Embed(title="Top 10 Highest Ranks", colour=discord.Colour.blue(), timestamp=datetime.datetime.utcnow())
            for x in rankings:
                try:
                    temp = ctx.guild.get_member(x["id"])
                    tempxp = x["xp"]
                    embed.add_field(name=f"{i}: {temp.name}#{temp.discriminator}", value=f"Total XP: {tempxp}", inline=False)
                    i += 1
                except:
                    pass
                if i == 11:
                    break
            embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}\u200b")
            await ctx.channel.send(embed=embed)

def setup(client):
    client.add_cog(levelsys(client))
