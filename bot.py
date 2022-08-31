import discord
import os
import keep_alive
from discord.ext import commands
import OpenAi
intents = discord.Intents().all()
client = commands.Bot(command_prefix="!")

BOT_TOKEN = os.getenv("BOT_TOKEN")

@client.event
async def on_ready():
    print("Bot is now alive.")

@client.command()
async def hello(ctx):
    await ctx.send("Hi")

@client.event
async def on_ready():
    pass;

responses = 0
list_user = []


@client.event
async def on_message(message):
    if message.author.id == client.user.id:
        pass;# dm only
    else:
        #await message.channel.send('ping')
        chat_log=''
        list_user.append(message.author.id)
        question = message.content
        answer = OpenAi.ask(question, chat_log)
        print(answer)
        if not answer:
            await message.channel.send("Sorry I couldn't process that :P")
        else:
            chat_log = OpenAi.append_interaction_to_chat_log(question, answer,chat_log)
            await message.channel.send(answer)
            f = open("log_user.txt", "w")
            for it in list_user:
            	f.write("%i\n" % it)
            f.close()

@client.command()
@commands.is_owner()
async def shutdown(context):
    exit()


keep_alive.keep_alive()
client.run(BOT_TOKEN)
