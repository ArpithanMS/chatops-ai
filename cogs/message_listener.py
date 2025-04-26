import discord
from discord.ext import commands

class MessageListener(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        if "server slow" in message.content.lower():
            await message.channel.send("⚡ Let me check server performance...")

async def setup(bot):
    await bot.add_cog(MessageListener(bot))
