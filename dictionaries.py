import discord
import json
import requests


async def define(interaction: discord.Interaction, word: str):
    resp = requests.get(
        f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}')
    jsonresp = json.loads(resp.text)[0]
    finalString = f"**{jsonresp['word']}**"
    for item in jsonresp['meanings']:
        finalString += '\n\n\n'
        finalString += f"**{item['partOfSpeech']}**"
        for i, item2 in enumerate(item['definitions']):
            if i < 5:
                finalString += '\n\n'
                finalString += f"{i+1}. {item2['definition']}"
    embed = discord.Embed(type="rich", description=finalString, color=0xffa400)
    await interaction.response.send_message(embed=embed)


async def urban(interaction: discord.Interaction, word: str):
    url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"
    querystring = {"term": f"{word}"}
    headers = {
        'x-rapidapi-key': "aead2685c6msh47f48636f6c085ep162a2ajsn89e4aac8fade",
        'x-rapidapi-host': "mashape-community-urban-dictionary.p.rapidapi.com"
    }
    response = requests.request(
        "GET", url, headers=headers, params=querystring)

    jsonresp = json.loads(response.text)['list']
    definition = jsonresp[0]['definition'].replace('[', '').replace(']', '')
    example = jsonresp[0]['example'].replace('[', '').replace(']', '')
    finalString = ''
    finalString += f'\n\n\n\n**Definition:**\n {definition}\n'
    finalString += f'\n**Example:** \n{example}'
    urlWord = word.replace(' ', '+')
    file = discord.File('urbandict_icon.png', filename="urbandict_icon.png")
    embed = discord.Embed(
        type="rich", title=f'{word}', url=f'https://www.urbandictionary.com/define.php?term={urlWord}', description=finalString, color=0xffa400)
    embed.set_author(name='Urban Dictionary', icon_url='attachment://urbandict_icon.png')
    await interaction.response.send_message(file=file, embed=embed)
