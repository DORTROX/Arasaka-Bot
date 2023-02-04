import discord, os, openai
from dotenv import load_dotenv, find_dotenv
from os import name, system
from discord.ext import commands
from discord.ext.commands import CommandNotFound

load_dotenv(find_dotenv())

intents = discord.Intents().all()
Arasaka = commands.Bot(
    command_prefix=".",
    intents=intents,
                    )

for filename in os.listdir('./runs'):
    if filename.endswith('.py'):
        Arasaka.load_extension(f'runs.{filename[:-3]}')

if name == 'nt':
    _ = system('cls')
else:
    _ = system('clear')

@Arasaka.event
async def on_ready():
    print(f'{Arasaka.user} has connected to Discord!')

@Arasaka.event
async def on_message(message):
    x = []
    if message.author.id == 1066289004460392490:
        pass
    else:
        if message.channel.id == 1071080547713032282:
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=f"a simple sweet chat for the message above is povided with reply : {message.content}. make a nice friendly reply for it",
                max_tokens=2048,
                n=2,
                stop=None,
                temperature=1,
                top_p = 1,
                frequency_penalty=1.58,
            )

            generated_text = response["choices"][0]["text"].strip()
            await message.channel.send(generated_text)
        else:
            await Arasaka.process_commands(message)


# Response model for friendly chat not repititive bc temperature is set to 1

# response = openai.Completion.create(
#   model="text-davinci-003",
#   prompt="im sad...\n\nI'm sorry to hear that. Is there anything I can do to help?\n\ni just want to cry..\n\nIt's okay to cry. It can be a healthy way to express your emotions. Is there anything else I can do to help?\n\ni just want to cry..\nMaybe listening to music or watching a movie that comforts you can help.\nyes you are right maybe i ll do that\n\nI'm glad that might help. Is there anyone else that you can talk to about how you are feeling?",
#   temperature=1,
#   max_tokens=60,
#   top_p=1,
#   frequency_penalty=0.5,
#   presence_penalty=0
# )

@Arasaka.command()
async def hello(ctx):
    await ctx.send("Hi")

Arasaka.run(os.getenv("DiscordToken"))