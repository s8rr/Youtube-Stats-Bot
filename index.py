import discord
from discord.ext import commands
from googleapiclient.discovery import build

# Set up the Discord bot
bot = commands.Bot(command_prefix='!')

# Set up the YouTube Data API
youtube = build('youtube', 'v3', developerKey='YOUR_YOUTUBE_API_KEY')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if 'youtube.com' in message.content:
        video_id = extract_video_id(message.content)
        if video_id:
            video_info = get_video_info(video_id)
            if video_info:
                await message.channel.send(video_info)

    await bot.process_commands(message)

def extract_video_id(url):
    # Extract the video ID from a YouTube URL
    # You can use regular expressions or other methods
    # For simplicity, this example assumes a straightforward URL structure
    return url.split('?v=')[-1]

def get_video_info(video_id):
    try:
        request = youtube.videos().list(part='snippet,statistics', id=video_id)
        response = request.execute()
        video = response['items'][0]
        snippet = video['snippet']
        statistics = video['statistics']
        title = snippet['title']
        views = statistics['viewCount']
        dislikes = statistics.get('dislikeCount', 'N/A')
        return f'Title: {title}\nViews: {views}\nDislikes: {dislikes}'
    except Exception as e:
        print(f'Error: {e}')
        return 'Error fetching video information.'

# Start the bot
bot.run('YOUR_DISCORD_BOT_TOKEN')
