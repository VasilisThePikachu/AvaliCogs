# Required to use
import discord
from redbot.core import commands


class privatechannel(commands.Cog):

    def __init__(self, bot) -> None:
        self.bot = bot

    # Commands
    @commands.hybrid_command()
    async def create(self, ctx, name):
        guild = ctx.guild
        category = discord.utils.get(guild.categories, name='Private Channels')
        if category is None:  # If there's no category matching with the `name`
            await guild.create_category('Private Channels')  # Creates the category

        await ctx.send('Creating...')
        member = ctx.author
        overwrites = {
            guild.default_role: discord.PermissionOverwrite(read_messages=False, send_messages=False),
            guild.me: discord.PermissionOverwrite(read_messages=True, send_messages=True),
            member: discord.PermissionOverwrite(read_messages=True, send_messages=True)
        }
        channelcat = discord.utils.get(ctx.guild.channels, name="Private Channels")
        await guild.create_text_channel(name, category=channelcat, overwrites=overwrites)
        myembed = discord.Embed(title=":white_check_mark: Done!", description="It should be at the botom of the "
                                                                              "channel list", color=0x6136c2)
        await ctx.send(embed=myembed)

    @commands.hybrid_command()
    async def adduser(self, ctx, user: discord.User):
        overwrite = ctx.channel.overwrites_for(ctx.author)
        if not overwrite.read_messages:
            myembed = discord.Embed(title=":x: Error!", description="You dont have the permission to edit this "
                                                                    "channel. Please run this command in your private"
                                                                    " channel",
                                    color=0x6136c2)
            await ctx.send(embed=myembed)
        else:
            await ctx.channel.set_permissions(user, read_messages=True, send_messages=True)
            myembed = discord.Embed(title=":white_check_mark: Done!", description="They now have access", color=0x6136c2)
            await ctx.send(embed=myembed)

    @commands.hybrid_command()
    async def deluser(self, ctx, user: discord.User):
        overwrite = ctx.channel.overwrites_for(ctx.author)
        if not overwrite.read_messages:
            myembed = discord.Embed(title=":x: Error!", description="You dont have the permission to edit this "
                                                                    "channel. Please run this command in your private"
                                                                    " channel",
                                    color=0x6136c2)
            await ctx.send(embed=myembed)
        else:
            await ctx.channel.set_permissions(user, read_messages=False, send_messages=False)
            myembed = discord.Embed(title=":white_check_mark: Done!", description="They now no longer have access", color=0x6136c2)
            await ctx.send(embed=myembed)