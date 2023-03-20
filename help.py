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

        embedEn = discord.Embed(color=0xffa440, type='rich', description=guideEn)
        embedRu = discord.Embed(color=0xffa440, type='rich', description=guideRu)
        embedEn.set_author(name="Practice Your Russian & English", icon_url=interaction.guild.icon.url)
        embedRu.set_author(name="Practice Your Russian & English", icon_url=interaction.guild.icon.url)
        post = await languageQuestions.create_thread(name='How to properly use the #language-questions channel // Корректное использование канала', content='How to properly use the #language-questions channel // Корректное использование канала')
        await post.send(embed=embedEn)
        await post.send(embed=embedRu)

