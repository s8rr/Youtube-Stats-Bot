# Youtube-API-Bot
The YouTube Stats Bot is a handy Discord bot that allows users to fetch statistics for YouTube videos directly within a Discord server. With this bot, you can quickly check the view count and dislike count of any YouTube video by simply providing its URL.

Features:

- Automatic URL Detection: The bot automatically detects YouTube video links shared in the server's chat and responds with relevant information.

- YouTube API Integration: It utilizes the YouTube Data API to fetch up-to-date statistics, ensuring accuracy.

- Informative Responses: When a user shares a YouTube link, the bot replies with the video's title, view count, and dislike count. If the video doesn't have any dislikes, it gracefully reports "N/A."

- Customizable Prefix: You can customize the bot's command prefix to align with your server's needs.






# YouTube Stats Bot Setup Guide

1. Create a Discord Bot:

   - Go to the [Discord Developer Portal](https://discord.com/developers/applications).
   - Create a new application.
   - Under the "Bot" tab, create a bot user.
   - Copy the bot token for later use.

2. Obtain a YouTube Data API Key:

   - Go to the [Google Cloud Console](https://console.cloud.google.com/).
   - Create a new project.
   - Enable the YouTube Data API v3 in the Library.
   - Create an API key from the "Credentials" section.
   
3. Set Up Your Python Environment:

   - Ensure you have Python installed on your system.
   - Install the required libraries using pip:
```
pip install discord.py google-auth google-auth-httplib2 google-api-python-client
```

4. Customize the Bot:

   - Replace 'YOUR_DISCORD_BOT_TOKEN' in the Python code with your Discord bot token.
   - Replace 'YOUR_YOUTUBE_API_KEY' with your YouTube Data API key.
   - Customize the bot's command prefix in the code if needed.

5. Run the Bot:

   - Save the Python code to a file, e.g., youtube_bot.py.
   - Run the script using your Python environment.
   - The bot will join your Discord server and respond to YouTube links with video statistics.

