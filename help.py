import discord
import json
import io
import asyncio

async def can_do(interaction: discord.Interaction):
    role = discord.utils.find(
        lambda r: r.name == 'Moderator', interaction.guild.roles)
    if role not in interaction.user.roles:
        await interaction.response.send_message('You do not have permission to use this command!', ephemeral=True, delete_after=20)
    else:
        with io.open('help.json', encoding='utf-8') as file:
            jsonHelp = json.load(file)
            enText = jsonHelp['can_do'][0]
            ruText = jsonHelp['can_do'][1]
            noteEn = jsonHelp['can_do'][2]
            noteRu = jsonHelp['can_do'][3] 
        with io.open('channel_ids.json', encoding='utf-8') as file:
            channels = json.load(file)
            botInfo = interaction.guild.get_channel(channels['bot-info'])
            botCommands = interaction.guild.get_channel(channels['bot-commands'])
        finalNoteEn = noteEn.replace('#bot-info', f"{botInfo.mention}").replace('#bot-commands', f"{botCommands.mention}")
        finalNoteRu = noteRu.replace('#bot-info', f"{botInfo.mention}").replace('#bot-commands', f"{botCommands.mention}")
        finalString = f'{finalNoteEn}\n\n{finalNoteRu}'
        embedEn = discord.Embed(type='rich', title='What I can do:', description=enText, color=0xffa400)
        embedRu = discord.Embed(type='rich', title='Что я умею:', description=ruText, color=0xffa400)
        embedEn.set_author(name="Practice Your Russian & English", icon_url=interaction.guild.icon.url)
        embedRu.set_author(name="Practice Your Russian & English", icon_url=interaction.guild.icon.url)
        await interaction.response.send_message('Please stand by', ephemeral=True, delete_after=10)
        await interaction.channel.send(finalString)
        await asyncio.sleep(60*10)
        await interaction.channel.send(embed=embedEn)
        await interaction.channel.send(embed=embedRu)
        top = ''
        async for message in interaction.channel.history(limit=1, oldest_first=True):
            top = str(message.jump_url)
        
        embedBacktoTop = discord.Embed(color=0x2c2d31, type='rich', description=f'[<:top:1088116402679975956> Get to the top]({top})')
        await interaction.channel.send(embed=embedBacktoTop)


async def help(interaction: discord.Interaction):
    with io.open('channel_ids.json', encoding='utf-8') as file:
        channels = json.load(file)
        botInfo = interaction.guild.get_channel(channels['bot-info'])
    await interaction.response.send_message(f'For the full list of available commands, please refer to {botInfo.mention}')


async def nigger(interaction: discord.Interaction):
    role = discord.utils.find(
        lambda r: r.name == 'Moderator', interaction.guild.roles)
    if role not in interaction.user.roles:
        await interaction.response.send_message('You do not have permission to use this command!', ephemeral=True, delete_after=20)
    else:
        await interaction.response.send_message('Please stand by', ephemeral=True, delete_after=20)
        with io.open('help.json', encoding='utf-8') as file:
            jsonHelp = json.load(file)
            guideEn = jsonHelp['nigger']['en']
            guideRu = jsonHelp['nigger']['ru']
        with io.open('channel_ids.json', encoding='utf-8') as file:
            channels = json.load(file)
            languageQuestions = interaction.guild.get_channel(channels['language-questions'])
            proofreading = interaction.guild.get_channel(channels['proofreading'])

        guideEn = guideEn.replace("#proofreading", proofreading.mention).replace("#language-questions", languageQuestions.mention)
        guideRu = guideRu.replace("#proofreading", proofreading.mention)

        embedEn = discord.Embed(color=0xffa440, type='rich', description=guideEn)
        embedRu = discord.Embed(color=0xffa440, type='rich', description=guideRu)
        embedEn.set_author(name="Practice Your Russian & English", icon_url=interaction.guild.icon.url)
        embedRu.set_author(name="Practice Your Russian & English", icon_url=interaction.guild.icon.url)
        post = await languageQuestions.create_thread(name='How to properly use the #language-questions channel // Руководство по использованию канала', content='Don\'t forget to check this out! // Обязательно ознакомьтесь!')
        await post.thread.send(embed=embedEn)
        await post.thread.send(embed=embedRu)


async def createPost(interaction: discord.Interaction,  name: str, description: str):
    role = discord.utils.find(
        lambda r: r.name == 'Moderator', interaction.guild.roles)
    if role not in interaction.user.roles:
        await interaction.response.send_message('You do not have permission to use this command!', ephemeral=True, delete_after=20)
    else:
        await interaction.response.send_message('Please stand by', ephemeral=True, delete_after=20)
        with io.open('channel_ids.json', encoding='utf-8') as file:
            channels = json.load(file)
            media = interaction.guild.get_channel(channels['media'])
        await media.create_thread(name=name, content=f'# {description}\n')


async def defaultPost(interaction: discord.Interaction):
    role = discord.utils.find(
        lambda r: r.name == 'Moderator', interaction.guild.roles)
    if role not in interaction.user.roles:
        await interaction.response.send_message('You do not have permission to use this command!', ephemeral=True, delete_after=20)
    else:
        await interaction.response.send_message('Please stand by', ephemeral=True, delete_after=20)
        with io.open('channel_ids.json', encoding='utf-8') as file:
            channels = json.load(file)
            media = interaction.guild.get_channel(channels['media'])
        await media.create_thread(name='🍝 Food', content='# Share mouthwatering dishes you\'ve cooked, discover new recipes, and discuss all things culinary')    
        await media.create_thread(name='🐶 Pets', content='# Share your adorable pets, their antics, and your love for your furry, feathery, or scaly companions')
        await media.create_thread(name='📷 Travel & Photography', content='# Showcase your adventures and stunning shots from around the world')
        await media.create_thread(name='🎶 Music', content='# Discover new tunes and discuss your favorite tracks, albums, or artists')
        await media.create_thread(name='🤡 Memes', content='# Unleash your creativity and humor with memes and funny content')
        await media.create_thread(name='🪁 Hobbies', content='# Share and discuss your favorite hobbies, from movies, TV shows, books, and video games, to sports, personal artwork, coding projects, and even your beloved plants')