import discord
import deepl
import io
import json

translator = deepl.Translator("e92f1b3d-8489-6817-b45d-d2ea86226a43:fx")

async def translate(interaction: discord.Interaction, target_lang: str, phrase: str, source_lang: str = 'auto'):
    # try:
        with io.open('help.json', encoding='utf-8') as file:
            jsonHelp = json.load(file)
            langs = jsonHelp['help_translate']['langs']
        target_lang = target_lang.lower()
        source_lang = source_lang.lower()
        if target_lang == 'english' :
            target_lang += ' (american)'
        if source_lang == 'english':
            source_lang += ' (american)'
        if target_lang == 'portuguese':
            target_lang += ' (brazilian)'
        if source_lang == 'portuguese':
            source_lang += ' (brazilian)'
        if target_lang == 'en':
            target_lang = 'en-us'
        if target_lang == 'pt':
            target_lang = 'pt-br'
        if source_lang == 'pt':
            source_lang = 'pt-br'
        if target_lang == 'norwegian':
            target_lang += ' (bokmal)'
        if source_lang == 'norwegian':
            source_lang += ' (bokmal)'
        if target_lang == 'chinese':
            target_lang += ' (simplified)'
        if source_lang == 'chinese':
            source_lang += ' (simplified)'
        for item in langs.keys():
            if target_lang == langs[item].lower():
                target_lang = item
            if source_lang == langs[item].lower():
                source_lang = item
        
        if source_lang == 'auto':
            result = translator.translate_text(phrase, target_lang=target_lang)
        else:
            await interaction.channel.send(source_lang)
            if source_lang.lower() == 'en-us' or source_lang.lower() == 'english (american)':
                source_lang = 'us'
            result = translator.translate_text(phrase, target_lang=target_lang, source_lang=source_lang)
        file = discord.File('deepl_icon.png', filename="deepl_icon.png")
        source = result.detected_source_lang.lower() 
        embed = discord.Embed(type="rich", description=f'Translated from {langs[source]}:\n**{phrase}**\n\nTranslated to {langs[target_lang]}:\n**{result}**', color=0x19264c)
        embed.set_author(name='DeepL', icon_url='attachment://deepl_icon.png')
        await interaction.response.send_message(file=file, embed=embed)
    # except:
    #     embed = discord.Embed(type="rich", title='Error', description='Something went wrong. Please make sure you have provided the correct language code. You can use the **/translate_help** command to view the full list of available language codes.', color=0x19264c)
    #     embed.set_author(name='DeepL', icon_url='attachment://deepl_icon.png')
    #     file = discord.File('deepl_icon.png', filename="deepl_icon.png")
    #     await interaction.response.send_message(file=file, embed=embed)

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