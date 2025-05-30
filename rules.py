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
        await interaction.response.send_message('You do not have permmission to use this command!', ephemeral=True, delete_after=20)
    else:
        if lang == 'ru':
            with io.open('channel_ids.json', encoding='utf-8') as file:
                channels = json.load(file)
                otherLanguages = interaction.guild.get_channel(channels['other-languages'])
                languageQuestions = interaction.guild.get_channel(channels['language-questions'])
            output = rulesRus[rule_number].replace(
                "other-languages", f"{otherLanguages.mention}").replace("language-questions", f"{languageQuestions.mention}")
            embed = discord.Embed(
                type='rich', description=f"**{rule_number}.** {output}", color=0xffa400)
            embed.set_footer(text='Practice Your Russian & English', icon_url=interaction.guild.icon.url)
            await interaction.response.send_message(embed=embed)
        if lang == 'en':
            with io.open('channel_ids.json', encoding='utf-8') as file:
                channels = json.load(file)
                otherLanguages = interaction.guild.get_channel(channels['other-languages'])
                languageQuestions = interaction.guild.get_channel(channels['language-questions'])
            output = rulesEng[rule_number].replace(
                "other-languages", f"{otherLanguages.mention}").replace("language-questions", f"{languageQuestions.mention}")
            embed = discord.Embed(
                type='rich', description=f"**{rule_number}.** {output}", color=0xffa400)
            embed.set_footer(text='Practice Your Russian & English', icon_url=interaction.guild.icon.url)
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
        await interaction.response.send_message('Please stand by', ephemeral=True, delete_after=20)
        file = discord.File('rules.png', filename="rules.png")
        embedPicture = discord.Embed(type='rich', color=0xffa400)
        embedPicture.set_image(
            url='attachment://rules.png')
        await interaction.channel.send(file=file, embed=embedPicture)

        finalString = f'{rulesIntro["introEng"]}\n\n'
        for key, item in rulesEng.items():
            with io.open('channel_ids.json', encoding='utf-8') as file:
                channels = json.load(file)
                otherLanguages = interaction.guild.get_channel(channels['other-languages'])
                languageQuestions = interaction.guild.get_channel(channels['language-questions'])
            mentioned = item.replace("other-languages", f"{otherLanguages.mention}").replace("language-questions", f"{languageQuestions.mention}")
            finalString += f"**{key}.** {mentioned}\n\n"
#        embedIntro = discord.Embed(type="rich", description=rulesIntro['introEng'], color=0xffa400)
        embedRules = discord.Embed(
            type="rich", description=finalString, color=0xffa400)
        embedRules.set_author(
            name="Practice Your Russian & English", icon_url=interaction.guild.icon.url)
#        await interaction.channel.send(embed=embedIntro)
        await interaction.channel.send(embed=embedRules)

#        await asyncio.sleep(600)

        finalString = f'{rulesIntro["introRus"]}\n\n'
        for key, item in rulesRus.items():
            with io.open('channel_ids.json', encoding='utf-8') as file:
                channels = json.load(file)
                otherLanguages = interaction.guild.get_channel(channels['other-languages'])
                languageQuestions = interaction.guild.get_channel(channels['language-questions'])
            mentioned = item.replace("other-languages", f"{otherLanguages.mention}").replace("language-questions", f"{languageQuestions.mention}")
            finalString += f"**{key}.** {mentioned}\n\n"
#        embedIntro = discord.Embed(type="rich", description=rulesIntro['introRus'], color=0xffa400)
        embedRules = discord.Embed(
            type="rich", description=finalString, color=0xffa400)
        embedRules.set_author(
            name="Practice Your Russian & English", icon_url=interaction.guild.icon.url)
#        await interaction.channel.send(embed=embedIntro)
        await interaction.channel.send(embed=embedRules)

        top = ''
        async for message in interaction.channel.history(limit=1, oldest_first=True):
            top = message.jump_url
        
        embedBacktoTop = discord.Embed(color=0x2c2d31, type='rich', description=f'[<:top:1088116402679975956> Get to the top]({top})')
        await interaction.channel.send(embed=embedBacktoTop)