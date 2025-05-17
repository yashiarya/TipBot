import discord
import logging
import logging.handlers

intents = discord.Intents.all()
##intents.members = True
##intents.voice_states = True
##intents.messages = True

julieUserId = 879809989189980161
gabeUserId = 612385958217908264
wallyUserId = 480772749518831617
vcTextChannelId = 1327813409852362794
token = 'MTM3MzEyNjYyOTI1NzM3OTg2MA.G8zu5C.DfQ9l7jJU6PH-8c1IHsvOEk4n6cDTKsFhJ_OVk'
from discord.ext import commands

bot = commands.Bot(command_prefix="!",intents=discord.Intents.default()) # prefix is the bot command

@bot.event
async def on_voice_state_update(member, before, after):
    channel = bot.get_channel(vcTextChannelId)
    # Only act when the member leaves a voice channel
    if before.channel is not None and after.channel is None:
        if member.id in [julieUserId, gabeUserId]:
            name_upper = member.display_name.upper()

            embed = discord.Embed(
                title="Did you enjoy VC? We know you did ;)",
                description=f"**{name_upper} OUT**\n\n*Leave a TIP!*",
                color=discord.Color.purple()
            )
            embed.set_image(url="attachment://TipJar.png")  # This will be the uploaded file
            embed.set_footer(text=f"ID: {member.id} • {discord.utils.format_dt(discord.utils.utcnow(), style='t')}")
            embed.set_author(name=member.name, icon_url=member.avatar.url if member.avatar else None)

            # Attach image file
            file = discord.File(r"D:\Downloads\TipJar.png", filename="TipJar.png")
            await channel.send(embed=embed, file=file)


logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
logging.getLogger('discord.http').setLevel(logging.INFO)

handler = logging.handlers.RotatingFileHandler(
    filename='discord.log',
    encoding='utf-8',
    maxBytes=32 * 1024 * 1024,  # 32 MiB
    backupCount=5,  # Rotate through 5 files
)
dt_fmt = '%Y-%m-%d %H:%M:%S'
formatter = logging.Formatter('[{asctime}] [{levelname:<8}] {name}: {message}', dt_fmt, style='{')
handler.setFormatter(formatter)
logger.addHandler(handler)

# Assume client refers to a discord.Client subclass...
# Suppress the default configuration since we have our own
bot.run(token, log_handler=None)
