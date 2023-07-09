import discord
import re

def emojext(message):
    if type(message.channel) != discord.DMChannel:
        server_emoji = [e for e in message.guild.emojis]
    else:
        server_emoji = []
    pattern = r':[a-zA-Z0-9_]+:'
    text = message.content
    m = re.findall(pattern, text)
            if len(m) != 0:
                allb = []
                pattern = r'[a-zA-Z0-9_]+'
                for i in m:
                    n = re.search(pattern, i)
                    if n != None:
                        n = n.group()
                        allb.append(n)
                for n in allb:
                    for se in server_emoji:
                        if se.name == n:
                            em = [e for e in message.guild.emojis if e.name == n]
                            await message.add_reaction(f'<:{em[0].name}:{em[0].id}>')
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