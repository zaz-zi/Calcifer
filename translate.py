import discord
import deepl
import io
import json

translator = deepl.Translator("e92f1b3d-8489-6817-b45d-d2ea86226a43:fx")

async def translate(interaction: discord.Interaction, target_lang: str, phrase: str, source_lang: str = 'auto'):
    try:
        if source_lang == 'auto':
            result = translator.translate_text(phrase, target_lang=target_lang)
        else:
            result = result = translator.translate_text(phrase, target_lang=target_lang, source_lang=source_lang)
        with io.open('help.json', encoding='utf-8') as file:
            jsonHelp = json.load(file)
            langs = jsonHelp['help_translate']['langs']
        file = discord.File('deepl_icon.png', filename="deepl_icon.png")
        source = result.detected_source_lang
        embed = discord.Embed(type="rich", description=f'Translated from {langs[source.lower()]}:\n**{phrase}**\n\nTranslated to {langs[target_lang]}:\n**{result}**', color=0x19264c)
        embed.set_author(name='DeepL', icon_url='attachment://deepl_icon.png')
        await interaction.response.send_message(file=file, embed=embed)
    except:
        embed = discord.Embed(type="rich", title='Error', description='Something went wrong. Please make sure you have provided the correct language code. You can use the **/help_translate** command to view the full list of available language codes.', color=0x19264c)
        embed.set_author(name='DeepL', icon_url='attachment://deepl_icon.png')
        file = discord.File('deepl_icon.png', filename="deepl_icon.png")
        await interaction.response.send_message(file=file, embed=embed)

async def help_translate(interaction: discord.Interaction):
    with io.open('help.json', encoding='utf-8') as file:
        jsonHelp = json.load(file)
        description = jsonHelp['help_translate']['description']
        langs = jsonHelp['help_translate']['langs']
    finalString = f'{description}\n\n'
    for i, item in enumerate(langs):
        finalString += f'{i+1}) {item}: {langs[item]}\n'
    embed = discord.Embed(type="rich", description=finalString, color=0x19264c)
    embed.set_author(name='DeepL', icon_url='attachment://deepl_icon.png')
    file = discord.File('deepl_icon.png', filename="deepl_icon.png")
    await interaction.response.send_message(file=file, embed=embed, ephemeral=True)