import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

class ChatOpsBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=intents)

    async def setup_hook(self):
        await self.load_extension('cogs.slash_commands')
        await self.load_extension('cogs.message_listener')
    
        # FOR DEV PURPOSE: Sync to GUILD only
        GUILD_ID = discord.Object(id=1365611291846381579)  # replace YOUR_TEST_SERVER_ID
        await self.tree.sync(guild=GUILD_ID)

    print("Slash commands synced to guild.")


bot = ChatOpsBot()

@bot.event
async def on_ready():
    print(f'Bot is ready. Logged in as {bot.user}.')

bot.run(TOKEN)
