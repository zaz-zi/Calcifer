import discord
import json
import io



async def resources(interaction: discord.Interaction):
    await interaction.response.send_message(content='.', ephemeral=True)

    with io.open('resources/ru_resources.json', encoding='utf-8') as file:
        jsonResources = json.load(file)
        intro = jsonResources['intro']
        categories = jsonResources['categories']
        nav_items = jsonResources['nav_items']

    # await interaction.channel.send(content=intro)
    # embedIntro = discord.Embed=(color=0xffa400, type='rich', description=intro)

    for category, category_items_dict in categories.items():
        file = discord.File(f'resources/category_{category}.png', filename=f'category_{category}.png')
        await interaction.channel.send(file=file)
        for item, item_attr_dict in category_items_dict.items():
            file = discord.File(f'resources/banner_{item}.png', filename=f'banner_{item}.png')
            item_desc = f"[{item_attr_dict['title']}]({item_attr_dict['url']}) {item_attr_dict['desc']}"
            embedItem = discord.Embed(color=0x2c2d31, type='rich', description=item_desc)
            embedItem.set_image(url=f'attachment://banner_{item}.png')
            await interaction.channel.send(file=file, embed=embedItem)

    nav_desc = '<:nav:1087012547053490267> Quick Navigation\n\n'
    ids = ''

    async for message in interaction.channel.history(limit=50):
        if message.attachments and 'category_' in message.attachments[0].filename:
            ids = f' {message.id}' + ids

    for i, id in enumerate(ids.split()):
        nav_desc += f'[{nav_items[i]}](https://discord.com/channels/{interaction.guild_id}/{interaction.channel_id}/{id})\n'

    embedNav = discord.Embed(color=0xffa400, type='rich', description=nav_desc)
    embedNav.set_footer(text="Hit 'Esc' to get back down.")
    await interaction.channel.send(embed=embedNav)