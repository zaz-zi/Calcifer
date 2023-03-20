import discord
import json
import io

async def proofreading(interaction: discord.Interaction):
    await interaction.response.send_message(content='.', ephemeral=True)

    with io.open('proofreading/proofreading.json', encoding='utf-8') as file:
        jsonProofreading = json.load(file)
        guides = jsonProofreading['guides']

    for id, guide in guides.items():
        for step, desc in guide['embeds'].items():
            embedStep = discord.Embed(color=0xffa440, type='rich', description=desc)
            try:
                file = discord.File(f'proofreading/{id}_{step}.png', filename=f'{step}.png')
                files = [file]
                embedStep.set_image(url=f'attachment://{step}.png')
                if step=='embed0':
                    icon = discord.File(f'proofreading/{id}_icon.png', filename=f'{id}_icon.png')
                    files.append(icon)
                    embedStep.set_author(name=guide['title'], icon_url=f'attachment://{id}_icon.png')
                await interaction.channel.send(files=files, embed=embedStep)
            except:
                await interaction.channel.send(embed=embedStep)


            
