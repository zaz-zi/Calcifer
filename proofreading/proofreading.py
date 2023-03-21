import discord
import json
import io
import asyncio

async def proofreading(interaction: discord.Interaction):
    role = discord.utils.find(
        lambda r: r.name == 'Moderator', interaction.guild.roles)
    if role not in interaction.user.roles:
        await interaction.response.send_message('You do not have permission to use this command!', ephemeral=True, delete_after=20)
    else:
        await interaction.response.send_message(content='Please stand by', ephemeral=True, delete_after=20)

        with io.open('proofreading/proofreading.json', encoding='utf-8') as file:
            jsonProofreading = json.load(file)
            intro = jsonProofreading['intro']
            guides = jsonProofreading['guides']
        
        with io.open('../channel_ids.json', encoding='utf-8') as file:
            channels = json.load(file)
            proofreading = interaction.guild.get_channel(channels['proofreading'])

        intro = intro.replace("#proofreading", proofreading.mention)

        embedIntro = discord.Embed(color=0xffa440, type='rich', description=intro)
        await interaction.channel.send(embed=embedIntro)
        await asyncio.sleep(60*10)

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
            await asyncio.sleep(60*10)


            
