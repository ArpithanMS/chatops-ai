import discord
from discord.ext import commands

class StatusCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("✅ StatusCog is ready.")

    @discord.app_commands.command(name="status", description="Check server status")
    async def status(self, interaction: discord.Interaction):
        await interaction.response.send_message("✅ Server is running smoothly!")

    @discord.app_commands.command(name="analyze", description="Analyze server performance")
    async def analyze(self, interaction: discord.Interaction):
        await interaction.response.send_message("🔎 Analyzing server metrics...")

    @discord.app_commands.command(name="recommend", description="Recommend action based on server status")
    async def recommend(self, interaction: discord.Interaction):
        await interaction.response.send_message("🧠 Recommendation: All systems nominal!")

async def setup(bot):
    await bot.add_cog(StatusCog(bot))
