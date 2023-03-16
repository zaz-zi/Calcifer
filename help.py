import discord
import json
import io

async def can_do(interaction: discord.Interaction):
    role = discord.utils.find(
        lambda r: r.name == 'Moderator', interaction.guild.roles)
    if role not in interaction.user.roles:
        await interaction.response.send_message('You do not have permission to use this command!', ephemeral=True)
    else:
        with io.open('help.json', encoding='utf-8') as file:
            jsonHelp = json.load(file)
            enText = jsonHelp['can_do'][0]
            ruText = jsonHelp['can_do'][1]
        embedEn = discord.Embed(type='rich', title='What I can do:', description=enText, color=0xffa400)
        embedRu = discord.Embed(type='rich', title='Что я умею:', description=ruText, color=0xffa400)
        embedEn.set_author(name="Practice Your Russian & English", icon_url=interaction.guild.icon.url)
        embedRu.set_author(name="Practice Your Russian & English", icon_url=interaction.guild.icon.url)
        await interaction.response.send_message('Please stand by', ephemeral=True, delete_after=10)
        await interaction.channel.send(embed=embedEn)
        await interaction.channel.send(embed=embedRu)


async def help(interaction: discord.Interaction):
    botInfo = interaction.guild.get_channel(1081670787699855412)
    await interaction.response.send_message(f'For the full list of available commands, please refer to {botInfo.mention}')
