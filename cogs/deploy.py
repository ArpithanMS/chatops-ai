import discord
from discord.ext import commands

class DeployCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("✅ DeployCog is ready.")

    @discord.app_commands.command(name="deploy", description="Deploy an application")
    async def deploy(self, interaction: discord.Interaction, app_name: str):
        await interaction.response.send_message(f"🚀 Deploying application: {app_name}...")

    @discord.app_commands.command(name="restart", description="Restart a service")
    async def restart(self, interaction: discord.Interaction, service_name: str):
        await interaction.response.send_message(f"♻️ Restarting service: {service_name}...")

async def setup(bot):
    await bot.add_cog(DeployCog(bot))
