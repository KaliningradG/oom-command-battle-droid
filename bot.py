import discord
from discord.ext import commands

client = discord.Client()
client = commands.Bot(command_prefix = '!')
client.remove_command('help')

@client.command()
async def test(ctx):
    await ctx.send("This is a test!")

client.run("NjUyMjU0MDM5MTg2MDc5ODA1.XepdjA.QhpDsuYMVCupGZHjETdQl3MZF34")
