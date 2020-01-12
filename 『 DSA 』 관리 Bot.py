pip install asyncio
pip install discord
import asyncio
import discord
import os


app = discord.Client()

access_token = os.environ["BOT_TOKEN"]
token = "(access_token)"

@app.event
async def on_ready():
    print("다음으로 로그인합니다 : ")
    print(app.user.name)
    print(app.user.id)
    print("==========")
    await app.change_presence(game=discord.Game(name="『 DSA 』 서버 관리중", type=1))

@app.event
async def on_message(message):
    if message.author.bot:
        return None
    if message.content == "안녕하세요":
        await app.send_message(message.channel, "안녕하세요. :)")

app.run(token)
