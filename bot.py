import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Fetch the Discord bot token from the environment
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Load cogs
async def load_extensions():
    for extension in ["cogs.status", "cogs.deploy"]:
        try:
            await bot.load_extension(extension)
            print(f"Successfully loaded {extension}")
        except Exception as e:
            print(f"Error loading {extension}: {e}")

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    await load_extensions()

    # Sync the slash commands with Discord
    await bot.tree.sync()
    print("Slash commands synced with Discord!")


bot.run(TOKEN)
