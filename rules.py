import discord
import json
import io
import asyncio

# await rules.rule(interaction, rule_number=rule_number, lang=lang)
async def rule(interaction: discord.Interaction, rule_number: str, lang: str):
    with io.open('rules.json', encoding='utf-8') as file:
        jsonRules = json.load(file)
        rulesRus = jsonRules[0]
        rulesEng = jsonRules[1]
    guild = interaction.guild
    role = discord.utils.find(lambda r: r.name == 'Moderator', guild.roles)
    if role not in interaction.user.roles:
        await interaction.response.send_message('You do not have permmission to use this command!', ephemeral=True)
    else:
        if lang == 'ru':
            output = rulesRus[rule_number]
            embed = discord.Embed(
                type='rich', description=f"{rule_number}. {output}", color=0xffa400)
            await interaction.response.send_message(embed=embed)
        if lang == 'en':
            output = rulesEng[rule_number]
            embed = discord.Embed(
                type='rich', description=f"{rule_number}. {output}", color=0xffa400)
            await interaction.response.send_message(embed=embed)


async def rules(interaction: discord.Interaction):
    with io.open('rules.json', encoding='utf-8') as file:
        jsonRules = json.load(file)
        rulesRus = jsonRules[0]
        rulesEng = jsonRules[1]
        rulesIntro = jsonRules[2]
    guild = interaction.guild
    role = discord.utils.find(lambda r: r.name == 'Moderator', guild.roles)
    if role not in interaction.user.roles:
        await interaction.response.send_message('You do not have permmission to use this command!', ephemeral=True)
    else:
        await interaction.response.send_message('.', ephemeral=True)
        file = discord.File('rules.png', filename="rules.png")
        embedPicture = discord.Embed(type='rich', color=0xffa400)
        embedPicture.set_image(
            url='attachment://rules.png')
        await interaction.channel.send(file=file, embed=embedPicture)

        finalString = ''
        for key, item in rulesEng.items():
            finalString += f"{key}. {item}\n\n"
        embedIntro = discord.Embed(
            type="rich", description=rulesIntro['introEng'], color=0xffa400)
        embedRules = discord.Embed(
            type="rich", description=finalString, color=0xffa400)
        await interaction.channel.send(embed=embedIntro)
        await interaction.channel.send(embed=embedRules)

        await asyncio.sleep(600)

        finalString = ''
        for key, item in rulesRus.items():
            finalString += f"{key}. {item}\n\n"
        embedIntro = discord.Embed(
            type="rich", description=rulesIntro['introRus'], color=0xffa400)
        embedRules = discord.Embed(
            type="rich", description=finalString, color=0xffa400)
        await interaction.channel.send(embed=embedIntro)
        await interaction.channel.send(embed=embedRules)
