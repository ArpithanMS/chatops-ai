import discord
from discord.ext import commands, tasks
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Fetch the Discord bot token from the environment
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# This task will run periodically to sync commands automatically
@tasks.loop(hours=1)  # Sync every 1 hour or adjust as needed
async def sync_commands():
    try:
        synced = await bot.tree.sync()
        print(f"✅ Synced {len(synced)} commands.")
    except Exception as e:
        print(f"❌ Error syncing commands: {e}")

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    # Start the sync task
    sync_commands.start()

# Load cogs
async def load_extensions():
    for extension in ["cogs.status", "cogs.deploy"]:
        try:
            await bot.load_extension(extension)
            print(f"Successfully loaded {extension}")
        except Exception as e:
            print(f"Error loading {extension}: {e}")

bot.run(TOKEN)
