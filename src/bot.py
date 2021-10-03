import os
import hikari
import lightbulb
from lightbulb import slash_commands
from dotenv import load_dotenv

load_dotenv()

bot = lightbulb.Bot(
    token=os.getenv("DISCORD_TOKEN"),
    allow_color=True,
    intents=(
        hikari.Intents.GUILDS
        | hikari.Intents.GUILD_INTEGRATIONS
        | hikari.Intents.GUILD_MESSAGES
    ),
    logs={
        "version": 1,
        "incremental": True,
        "loggers": {
            "hikari.gateway": {"level": "DEBUG"},
            "hikari.ratelimits": {"level": "TRACE_HIKARI"},
        },
    },
    prefix="!",
)


class Echo(slash_commands.SlashCommand):
    description = "Repeats your input."
    text: str = slash_commands.Option("Text to repeat")

    async def callback(self, context):
        print(context.options.text)

        await context.respond(context.options.text)


bot.add_slash_command(Echo)
bot.run()
