import discord
import re

class Emojext:
    def __init__(self, message):
        self.dm = []
        self.public = []
        self.server = []
        self.do_emojis = self.play_emoji(message)
        
    def play_emoji(self, message):
        if type(message.channel) != discord.DMChannel:
            server_emoji = [e for e in message.guild.emojis]
        else:
            server_emoji = []


def emojext(message):
    if type(message.channel) != discord.DMChannel:
        server_emoji = [e for e in message.guild.emojis]
    else:
        server_emoji = []
    origin_pattern = r':[a-zA-Z0-9_]+:'
    text = message.content
    origin_emoji = re.findall(origin_pattern, text)
    i = r'<:[a-zA-Z0-9_]+:\d+>'
    s = re.sub(i,"",s)
    a_list = []
    a_list.append(s)
    q = re.findall(r'[^\w\s,]', a_list[0])
            if len(q) != 0:
                for i in q:
                    try:
                        await message.add_reaction(i)
                    except:
                        continue
