import discord
from discord.ext import commands

client = discord.Client()

@client.event  # event decorator/wrapper
async def on_ready():
	print(f"We have logged in as {client.user}")

@client.event
async def on_message(message):
	print(f"{message.channel}: {message.author} {message.author.name} {message.content}")

	if "ha" in message.content.lower():
		await message.channel.send("Answer `!yes` or `!no`")

@client.event
async def on_ready():
	await client.change_presence(status=discord.Status.idle, activity=discord.Game("Touhou 12.3: Hisoutensoku"))
	print("okeyyy")



client.run("YOU-TOKEN-BOT")
