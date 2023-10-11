import discord
import io
import json

class ReadingMenu(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label='Interested', style=discord.ButtonStyle.red, custom_id='he1')
    async def selfReading(self, interaction: discord.Interaction, Button: discord.ui.Button):
        role = interaction.user.guild.get_role(1161749443087970354)
        if role in interaction.user.roles:
            await interaction.user.remove_roles(role)
            await interaction.response.send_message('Role revoked', ephemeral=True, delete_after=20)
        else:
            await interaction.user.add_roles(role)
            await interaction.response.send_message('Role granted', ephemeral=True, delete_after=20)


async def readingMenu(interaction: discord.Interaction):
    role = discord.utils.find(
        lambda r: r.name == 'Moderator', interaction.guild.roles)
    if role not in interaction.user.roles:
        await interaction.response.send_message('You do not have permission to use this command!', ephemeral=True, delete_after=20)
    else:
        with io.open('roles.json', encoding='utf-8') as file:
            jsonRoles = json.load(file)
            text = jsonRoles["description_reading_club"]
        fileRu = discord.File('ru_circle_icon.png', filename="ru_circle_icon.png")
        embed = discord.Embed(type="rich", description=text, color=0xffa400)
        embed.set_author(name='Russian Events', icon_url='attachment://ru_circle_icon.png')
        await interaction.channel.send(file=fileRu, embed=embed, view=ReadingMenu())
        await interaction.response.send_message(".", delete_after=20, ephemeral=True)