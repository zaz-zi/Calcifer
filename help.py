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
        await interaction.response.send_message('.', ephemeral=True)
        await interaction.channel.send(embed=embedEn)
        await interaction.channel.send(embed=embedRu)