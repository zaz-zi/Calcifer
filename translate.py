import discord
import deepl
import io
import json

translator = deepl.Translator("e92f1b3d-8489-6817-b45d-d2ea86226a43:fx")

async def translate(interaction: discord.Interaction, target_lang: str, phrase: str):
    result = translator.translate_text(phrase, target_lang=target_lang)
    await interaction.response.send_message(result)

async def help_translate(interaction: discord.Interaction):
    with io.open('help.json', encoding='utf-8') as file:
        jsonHelp = json.load(file)
        description = jsonHelp['help_translate']['description']
        langs = jsonHelp['help_translate']['langs']
    finalString = f'{description}\n\n'
    for i, item in enumerate(langs):
        finalString += f'{i+1}) {item}: {langs[item]}\n'
    embed = discord.Embed(type="rich", description=finalString, color=0xffa400)
    await interaction.response.send_message(embed=embed, ephemeral=True)
