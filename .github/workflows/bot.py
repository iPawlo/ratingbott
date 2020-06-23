import discord
from discord.ext    import commands
from discord.ext.commands   import Bot

bot = commands.Bot(command_prefix='#')

@bot.event
async def on_ready():
    print('Autoreact ready...')

@bot.event
async def on_message(message):
    if message.channel.id == 724984445450322050: # Hier Server ID einfügen
        await message.add_reaction("1️⃣")
        await message.add_reaction("2️⃣")
        await message.add_reaction("3️⃣")
        await message.add_reaction("4️⃣")
        await message.add_reaction("5️⃣")


bot.run("NzI0OTc2NjY4NTE0NDUxNTA3.XvIQ6Q.-nQBSbWilgQABohbOk62RuOqzEM") # Hier Token einfügen

#                               BLUE Discord: https://discord.gg/germany
#
#                               BLUE YouTube: https://www.youtube.com/bluek1ng
#
# To-Do
# 1. Channel ID einfügen (Zeile 13)
# 2. Emoji einfügen (zeile 14)
# 3. Bot Token einfügen (Zeile 16)
# 4. Bot starten und Spaß haben
# 5. BLUE Server lieben und boosten! xD
#
#
#                               Python benutzen und Bot erstellen? Einleitung dazu findest du hier: https://youtu.be/RYbHpqHCjrY