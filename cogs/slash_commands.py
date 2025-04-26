import discord
from discord import app_commands
from discord.ext import commands

class SlashCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="status", description="Check the server status.")
    async def status(self, interaction: discord.Interaction):
        await interaction.response.send_message("✅ Server is running smoothly!")

async def setup(bot):
    await bot.add_cog(SlashCommands(bot))
