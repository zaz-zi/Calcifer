import discord
import io
import json


class EnglishMenu(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label='Beginner', style=discord.ButtonStyle.red, custom_id='en1')
    async def selfEnBeginner(self, interaction: discord.Interaction, Button: discord.ui.Button):
        roleLocked = interaction.user.guild.get_role(1085620656332349490)
        if roleLocked in interaction.user.roles:
            await interaction.response.send_message('You do not have permission to use this command!', ephemeral=True, delete_after=20)
        else:
            with io.open('roles.json', encoding='utf-8') as file:
                jsonRoles = json.load(file)
                ruRoles = jsonRoles['ru']
                enRoles = jsonRoles['en']
                unverifiedID = jsonRoles['unverified']
            role = interaction.user.guild.get_role(enRoles[0])
            unverified = interaction.user.guild.get_role(unverifiedID)

            if role in interaction.user.roles:
                await interaction.user.remove_roles(role)
                await interaction.user.add_roles(unverified)
                await interaction.response.send_message('Role revoked. You no longer have full access to the server because you do not have roles for both Russian and English. You must select an English role to get verified once again.', ephemeral=True, delete_after=20)
            else:
                alreadyHas = False
                for item in enRoles:
                    otherRole = interaction.user.guild.get_role(item)
                    if otherRole in interaction.user.roles:
                        alreadyHas = True
                        await interaction.user.remove_roles(otherRole)
                        await interaction.response.send_message('Role changed', ephemeral=True, delete_after=20)
                verified = False
                for item in ruRoles:
                    if interaction.user.guild.get_role(item) in interaction.user.roles:
                        if unverified in interaction.user.roles:
                            await interaction.user.remove_roles(unverified)
                            
                            verified = True
                await interaction.user.add_roles(role)
                if verified == False and alreadyHas == False:
                    await interaction.response.send_message('Role granted', ephemeral=True, delete_after=20)
                elif verified == True and alreadyHas == False:
                    with io.open('channel_ids.json', encoding='utf-8') as file:
                        channels = json.load(file)
                        introductions = interaction.guild.get_channel(channels['introductions'])
                        general = interaction.guild.get_channel(channels['general'])
                        languageQuestions = interaction.guild.get_channel(channels['language-questions'])
                    await interaction.response.send_message(f"Role granted. Congrats on getting verified {interaction.user.mention}!\nDon't forget to {introductions.mention}, and check out {general.mention} to say hi to the others! If you have any questions related to Russian or English, you can refer to {languageQuestions.mention}.\nEnjoy your stay!", ephemeral=True, delete_after=60*60)

    @discord.ui.button(label='Intermediate', style=discord.ButtonStyle.red, custom_id='en2')
    async def selfEnIntermediate(self, interaction: discord.Interaction, Button: discord.ui.Button):
        roleLocked = interaction.user.guild.get_role(1085620656332349490)
        if roleLocked in interaction.user.roles:
            await interaction.response.send_message('You do not have permission to use this command!', ephemeral=True, delete_after=20)
        else:
            with io.open('roles.json', encoding='utf-8') as file:
                jsonRoles = json.load(file)
                ruRoles = jsonRoles['ru']
                enRoles = jsonRoles['en']
                unverifiedID = jsonRoles['unverified']
            role = interaction.user.guild.get_role(enRoles[1])
            unverified = interaction.user.guild.get_role(unverifiedID)

            if role in interaction.user.roles:
                await interaction.user.remove_roles(role)
                await interaction.user.add_roles(unverified)
                await interaction.response.send_message('Role revoked. You no longer have full access to the server because you do not have roles for both Russian and English. You must select an English role to get verified once again.', ephemeral=True, delete_after=20)
            else:
                alreadyHas = False
                for item in enRoles:
                    otherRole = interaction.user.guild.get_role(item)
                    if otherRole in interaction.user.roles:
                        alreadyHas = True
                        await interaction.user.remove_roles(otherRole)
                        await interaction.response.send_message('Role changed', ephemeral=True, delete_after=20)
                verified = False
                for item in ruRoles:
                    if interaction.user.guild.get_role(item) in interaction.user.roles:
                        if unverified in interaction.user.roles:
                            await interaction.user.remove_roles(unverified)
                            
                            verified = True
                await interaction.user.add_roles(role)
                if verified == False and alreadyHas == False:
                    await interaction.response.send_message('Role granted', ephemeral=True, delete_after=20)
                elif verified == True and alreadyHas == False:
                    with io.open('channel_ids.json', encoding='utf-8') as file:
                        channels = json.load(file)
                        introductions = interaction.guild.get_channel(channels['introductions'])
                        general = interaction.guild.get_channel(channels['general'])
                        languageQuestions = interaction.guild.get_channel(channels['language-questions'])
                    await interaction.response.send_message(f"Role granted. Congrats on getting verified {interaction.user.mention}!\nDon't forget to {introductions.mention}, and check out {general.mention} to say hi to the others! If you have any questions related to Russian or English, you can refer to {languageQuestions.mention}.\nEnjoy your stay!", ephemeral=True, delete_after=60*60)

    @discord.ui.button(label='Advanced', style=discord.ButtonStyle.red, custom_id='en3')
    async def selfEnAdvanced(self, interaction: discord.Interaction, Button: discord.ui.Button):
        roleLocked = interaction.user.guild.get_role(1085620656332349490)
        if roleLocked in interaction.user.roles:
            await interaction.response.send_message('You do not have permission to use this command!', ephemeral=True, delete_after=10)
        else:
            with io.open('roles.json', encoding='utf-8') as file:
                jsonRoles = json.load(file)
                ruRoles = jsonRoles['ru']
                enRoles = jsonRoles['en']
                unverifiedID = jsonRoles['unverified']
            role = interaction.user.guild.get_role(enRoles[2])
            unverified = interaction.user.guild.get_role(unverifiedID)

            if role in interaction.user.roles:
                await interaction.user.remove_roles(role)
                await interaction.user.add_roles(unverified)
                await interaction.response.send_message('Role revoked. You no longer have full access to the server because you do not have roles for both Russian and English. You must select an English role to get verified once again.', ephemeral=True, delete_after=20)
            else:
                alreadyHas = False
                for item in enRoles:
                    otherRole = interaction.user.guild.get_role(item)
                    if otherRole in interaction.user.roles:
                        alreadyHas = True
                        await interaction.user.remove_roles(otherRole)
                        await interaction.response.send_message('Role changed', ephemeral=True, delete_after=20)
                verified = False
                for item in ruRoles:
                    if interaction.user.guild.get_role(item) in interaction.user.roles:
                        if unverified in interaction.user.roles:
                            await interaction.user.remove_roles(unverified)
                            
                            verified = True
                await interaction.user.add_roles(role)
                if verified == False and alreadyHas == False:
                    await interaction.response.send_message('Role granted', ephemeral=True, delete_after=20)
                elif verified == True and alreadyHas == False:
                    with io.open('channel_ids.json', encoding='utf-8') as file:
                        channels = json.load(file)
                        introductions = interaction.guild.get_channel(channels['introductions'])
                        general = interaction.guild.get_channel(channels['general'])
                        languageQuestions = interaction.guild.get_channel(channels['language-questions'])
                    await interaction.response.send_message(f"Role granted. Congrats on getting verified {interaction.user.mention}!\nDon't forget to {introductions.mention}, and check out {general.mention} to say hi to the others! If you have any questions related to Russian or English, you can refer to {languageQuestions.mention}.\nEnjoy your stay!", ephemeral=True, delete_after=60*60)

    @discord.ui.button(label='Native Speaker', style=discord.ButtonStyle.red, custom_id='en4')
    async def selfEnNative(self, interaction: discord.Interaction, Button: discord.ui.Button):
        roleLocked = interaction.user.guild.get_role(1085620656332349490)
        if roleLocked in interaction.user.roles:
            await interaction.response.send_message('You do not have permission to use this command!', ephemeral=True, delete_after=20)
        else:
            with io.open('roles.json', encoding='utf-8') as file:
                jsonRoles = json.load(file)
                ruRoles = jsonRoles['ru']
                enRoles = jsonRoles['en']
                unverifiedID = jsonRoles['unverified']
            role = interaction.user.guild.get_role(enRoles[3])
            unverified = interaction.user.guild.get_role(unverifiedID)

            if role in interaction.user.roles:
                await interaction.user.remove_roles(role)
                await interaction.user.add_roles(unverified)
                await interaction.response.send_message('Role revoked. You no longer have full access to the server because you do not have roles for both Russian and English. You must select an English role to get verified once again.', ephemeral=True, delete_after=20)
            else:
                alreadyHas = False
                for item in enRoles:
                    otherRole = interaction.user.guild.get_role(item)
                    if otherRole in interaction.user.roles:
                        alreadyHas = True
                        await interaction.user.remove_roles(otherRole)
                        await interaction.response.send_message('Role changed', ephemeral=True, delete_after=20)
                verified = False
                for item in ruRoles:
                    if interaction.user.guild.get_role(item) in interaction.user.roles:
                        if unverified in interaction.user.roles:
                            await interaction.user.remove_roles(unverified)
                            
                            verified = True
                await interaction.user.add_roles(role)
                if verified == False and alreadyHas == False:
                    await interaction.response.send_message('Role granted', ephemeral=True, delete_after=20)
                elif verified == True and alreadyHas == False:
                    with io.open('channel_ids.json', encoding='utf-8') as file:
                        channels = json.load(file)
                        introductions = interaction.guild.get_channel(channels['introductions'])
                        general = interaction.guild.get_channel(channels['general'])
                        languageQuestions = interaction.guild.get_channel(channels['language-questions'])
                    await interaction.response.send_message(f"Role granted. Congrats on getting verified {interaction.user.mention}!\nDon't forget to {introductions.mention}, and check out {general.mention} to say hi to the others! If you have any questions related to Russian or English, you can refer to {languageQuestions.mention}.\nEnjoy your stay!", ephemeral=True, delete_after=60*60)


class RussianMenu(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label='Beginner', style=discord.ButtonStyle.red, custom_id='ru1')
    async def selfRuBeginner(self, interaction: discord.Interaction, Button: discord.ui.Button):
        roleLocked = interaction.user.guild.get_role(1085620656332349490)
        if roleLocked in interaction.user.roles:
            await interaction.response.send_message('You do not have permission to use this command!', ephemeral=True, delete_after=20)
        else:
            with io.open('roles.json', encoding='utf-8') as file:
                jsonRoles = json.load(file)
                ruRoles = jsonRoles['ru']
                enRoles = jsonRoles['en']
                unverifiedID = jsonRoles['unverified']
            role = interaction.user.guild.get_role(ruRoles[0])
            unverified = interaction.user.guild.get_role(unverifiedID)

            if role in interaction.user.roles:
                await interaction.user.remove_roles(role)
                await interaction.user.add_roles(unverified)
                await interaction.response.send_message('Role revoked. You no longer have full access to the server because you do not have roles for both Russian and English. You must select a Russian role to get verified once again.', ephemeral=True, delete_after=20)
            else:
                alreadyHas = False
                for item in ruRoles:
                    otherRole = interaction.user.guild.get_role(item)
                    if otherRole in interaction.user.roles:
                        alreadyHas = True
                        await interaction.user.remove_roles(otherRole)
                        await interaction.response.send_message('Role changed', ephemeral=True, delete_after=20)
                verified = False
                for item in enRoles:
                    if interaction.user.guild.get_role(item) in interaction.user.roles:
                        if unverified in interaction.user.roles:
                            await interaction.user.remove_roles(unverified)
                            
                            verified = True
                await interaction.user.add_roles(role)
                if verified == False and alreadyHas == False:
                    await interaction.response.send_message('Role granted', ephemeral=True, delete_after=20)
                elif verified == True and alreadyHas == False:
                    with io.open('channel_ids.json', encoding='utf-8') as file:
                        channels = json.load(file)
                        introductions = interaction.guild.get_channel(channels['introductions'])
                        general = interaction.guild.get_channel(channels['general'])
                        languageQuestions = interaction.guild.get_channel(channels['language-questions'])
                    await interaction.response.send_message(f"Role granted. Congrats on getting verified {interaction.user.mention}!\nDon't forget to {introductions.mention}, and check out {general.mention} to say hi to the others! If you have any questions related to Russian or English, you can refer to {languageQuestions.mention}.\nEnjoy your stay!", ephemeral=True, delete_after=60*60)

    @discord.ui.button(label='Intermediate', style=discord.ButtonStyle.red, custom_id='ru2')
    async def selfRuIntermediate(self, interaction: discord.Interaction, Button: discord.ui.Button):
        roleLocked = interaction.user.guild.get_role(1085620656332349490)
        if roleLocked in interaction.user.roles:
            await interaction.response.send_message('You do not have permission to use this command!', ephemeral=True, delete_after=20)
        else:
            with io.open('roles.json', encoding='utf-8') as file:
                jsonRoles = json.load(file)
                ruRoles = jsonRoles['ru']
                enRoles = jsonRoles['en']
                unverifiedID = jsonRoles['unverified']
            role = interaction.user.guild.get_role(ruRoles[1])
            unverified = interaction.user.guild.get_role(unverifiedID)

            if role in interaction.user.roles:
                await interaction.user.remove_roles(role)
                await interaction.user.add_roles(unverified)
                await interaction.response.send_message('Role revoked. You no longer have full access to the server because you do not have roles for both Russian and English. You must select a Russian role to get verified once again.', ephemeral=True, delete_after=20)
            else:
                alreadyHas = False
                for item in ruRoles:
                    otherRole = interaction.user.guild.get_role(item)
                    if otherRole in interaction.user.roles:
                        alreadyHas = True
                        await interaction.user.remove_roles(otherRole)
                        await interaction.response.send_message('Role changed', ephemeral=True, delete_after=20)
                verified = False
                for item in enRoles:
                    if interaction.user.guild.get_role(item) in interaction.user.roles:
                        if unverified in interaction.user.roles:
                            await interaction.user.remove_roles(unverified)
                            
                            verified = True
                await interaction.user.add_roles(role)
                if verified == False and alreadyHas == False:
                    await interaction.response.send_message('Role granted', ephemeral=True, delete_after=20)
                elif verified == True and alreadyHas == False:
                    with io.open('channel_ids.json', encoding='utf-8') as file:
                        channels = json.load(file)
                        introductions = interaction.guild.get_channel(channels['introductions'])
                        general = interaction.guild.get_channel(channels['general'])
                        languageQuestions = interaction.guild.get_channel(channels['language-questions'])
                    await interaction.response.send_message(f"Role granted. Congrats on getting verified {interaction.user.mention}!\nDon't forget to {introductions.mention}, and check out {general.mention} to say hi to the others! If you have any questions related to Russian or English, you can refer to {languageQuestions.mention}.\nEnjoy your stay!", ephemeral=True, delete_after=60*60)

    @discord.ui.button(label='Advanced', style=discord.ButtonStyle.red, custom_id='ru3')
    async def selfRuAdvanced(self, interaction: discord.Interaction, Button: discord.ui.Button):
        roleLocked = interaction.user.guild.get_role(1085620656332349490)
        if roleLocked in interaction.user.roles:
            await interaction.response.send_message('You do not have permission to use this command!', ephemeral=True, delete_after=20)
        else:
            with io.open('roles.json', encoding='utf-8') as file:
                jsonRoles = json.load(file)
                ruRoles = jsonRoles['ru']
                enRoles = jsonRoles['en']
                unverifiedID = jsonRoles['unverified']
            role = interaction.user.guild.get_role(ruRoles[2])
            unverified = interaction.user.guild.get_role(unverifiedID)

            if role in interaction.user.roles:
                await interaction.user.remove_roles(role)
                await interaction.user.add_roles(unverified)
                await interaction.response.send_message('Role revoked. You no longer have full access to the server because you do not have roles for both Russian and English. You must select a Russian role to get verified once again.', ephemeral=True, delete_after=20)
            else:
                alreadyHas = False
                for item in ruRoles:
                    otherRole = interaction.user.guild.get_role(item)
                    if otherRole in interaction.user.roles:
                        alreadyHas = True
                        await interaction.user.remove_roles(otherRole)
                        await interaction.response.send_message('Role changed', ephemeral=True, delete_after=20)
                verified = False
                for item in enRoles:
                    if interaction.user.guild.get_role(item) in interaction.user.roles:
                        if unverified in interaction.user.roles:
                            await interaction.user.remove_roles(unverified)                     
                            verified = True
                await interaction.user.add_roles(role)
                if verified == False and alreadyHas == False:
                    await interaction.response.send_message('Role granted', ephemeral=True, delete_after=20)
                elif verified == True and alreadyHas == False:
                    with io.open('channel_ids.json', encoding='utf-8') as file:
                        channels = json.load(file)
                        introductions = interaction.guild.get_channel(channels['introductions'])
                        general = interaction.guild.get_channel(channels['general'])
                        languageQuestions = interaction.guild.get_channel(channels['language-questions'])
                    await interaction.response.send_message(f"Role granted. Congrats on getting verified {interaction.user.mention}!\nDon't forget to {introductions.mention}, and check out {general.mention} to say hi to the others! If you have any questions related to Russian or English, you can refer to {languageQuestions.mention}.\nEnjoy your stay!", ephemeral=True, delete_after=60*60)

    @discord.ui.button(label='Native Speaker', style=discord.ButtonStyle.red, custom_id='ru4')
    async def selfRuNative(self, interaction: discord.Interaction, Button: discord.ui.Button):
        roleLocked = interaction.user.guild.get_role(1085620656332349490)
        if roleLocked in interaction.user.roles:
            await interaction.response.send_message('You do not have permission to use this command!', ephemeral=True, delete_after=20)
        else:
            with io.open('roles.json', encoding='utf-8') as file:
                jsonRoles = json.load(file)
                ruRoles = jsonRoles['ru']
                enRoles = jsonRoles['en']
                unverifiedID = jsonRoles['unverified']
            role = interaction.user.guild.get_role(ruRoles[3])
            unverified = interaction.user.guild.get_role(unverifiedID)

            if role in interaction.user.roles:
                await interaction.user.remove_roles(role)
                await interaction.user.add_roles(unverified)
                await interaction.response.send_message('Role revoked. You no longer have full access to the server because you do not have roles for both Russian and English. You must select a Russian role to get verified once again.', ephemeral=True, delete_after=20)
            else:
                alreadyHas = False
                for item in ruRoles:
                    otherRole = interaction.user.guild.get_role(item)
                    if otherRole in interaction.user.roles:
                        alreadyHas = True
                        await interaction.user.remove_roles(otherRole)
                        await interaction.response.send_message('Role changed', ephemeral=True, delete_after=20)
                verified = False
                for item in enRoles:
                    if interaction.user.guild.get_role(item) in interaction.user.roles:
                        if unverified in interaction.user.roles:
                            await interaction.user.remove_roles(unverified) 
                            verified = True
                await interaction.user.add_roles(role)
                if verified == False and alreadyHas == False:
                    await interaction.response.send_message('Role granted', ephemeral=True, delete_after=20)
                elif verified == True and alreadyHas == False:
                    with io.open('channel_ids.json', encoding='utf-8') as file:
                        channels = json.load(file)
                        introductions = interaction.guild.get_channel(channels['introductions'])
                        general = interaction.guild.get_channel(channels['general'])
                        languageQuestions = interaction.guild.get_channel(channels['language-questions'])
                    await interaction.response.send_message(f"Role granted. Congrats on getting verified {interaction.user.mention}!\nDon't forget to {introductions.mention}, and check out {general.mention} to say hi to the others! If you have any questions related to Russian or English, you can refer to {languageQuestions.mention}.\nEnjoy your stay!", ephemeral=True, delete_after=60*60)


class HeritageMenu(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label='Heritage Speaker', style=discord.ButtonStyle.red, custom_id='he1')
    async def selfHeritage(self, interaction: discord.Interaction, Button: discord.ui.Button):
        role = interaction.user.guild.get_role(1079413567209611304)
        roleLocked = interaction.user.guild.get_role(1085620656332349490)
        if roleLocked in interaction.user.roles:
            await interaction.response.send_message('You do not have permission to use this command!', ephemeral=True, delete_after=20)
        else:
            if role in interaction.user.roles:
                await interaction.user.remove_roles(role)
                await interaction.response.send_message('Role revoked', ephemeral=True, delete_after=20)
            else:
                await interaction.user.add_roles(role)
                await interaction.response.send_message('Role granted', ephemeral=True, delete_after=20)


async def menuLangs(interaction: discord.Interaction):
    role = discord.utils.find(
        lambda r: r.name == 'Moderator', interaction.guild.roles)
    if role not in interaction.user.roles:
        await interaction.response.send_message('You do not have permission to use this command!', ephemeral=True)
    else:

        with io.open('roles.json', encoding='utf-8') as file:
            jsonRoles = json.load(file)
            rolesHe = jsonRoles['he_preamble_en'] + jsonRoles['he_en'] + jsonRoles['he_preamble_ru'] + jsonRoles['he_ru']
            rundownEn = jsonRoles['description_en']
            rundownRu = jsonRoles['description_ru']
        file = discord.File('roles.png', filename="roles.png")
        embedPicture = discord.Embed(type='rich', color=0xffa400)
        embedPicture.set_image(url='attachment://roles.png')
        await interaction.channel.send(file=file, embed=embedPicture)
        embedRundownEn = discord.Embed(
            type="rich", description=rundownEn, color=0xffa400)
        embedRundownEn.set_author(
                name="Practice Your Russian & English", icon_url=interaction.guild.icon.url)
        embedRundownRu = discord.Embed(
            type="rich", description=rundownRu, color=0xffa400)
        embedRundownRu.set_author(
                name="Practice Your Russian & English", icon_url=interaction.guild.icon.url)
        await interaction.channel.send(embed=embedRundownEn)
        await interaction.channel.send(embed=embedRundownRu)
        await interaction.response.send_message('Please stand by', ephemeral=True, delete_after=10)
        fileEn = discord.File('en_circle_icon.png', filename="en_circle_icon.png")
        fileRu = discord.File('ru_circle_icon.png', filename="ru_circle_icon.png")
        embedEn = discord.Embed(
            type="rich", title='**Please choose the English language proficiency role that best fits your current ability level\n\nВыберите роль, соответствующую Вашему уровню владения английским языком**', color=0xffa400)
        embedEn.set_author(name='English proficiency', icon_url=interaction.guild.icon.url)
        embedEn.set_author(name='English proficiency', icon_url='attachment://en_circle_icon.png')
        await interaction.channel.send(file=fileEn, embed=embedEn, view=EnglishMenu())
        embedRu = discord.Embed(
            type="rich", title='**Please choose the Russian language proficiency role that best fits your current ability level\n\nВыберите роль, соответствующую Вашему уровню владения русским языком**', color=0xffa400)
        embedRu.set_author(name='Russian proficiency', icon_url='attachment://ru_circle_icon.png')
        await interaction.channel.send(file=fileRu, embed=embedRu, view=RussianMenu())
        embedHe = discord.Embed(
            type="rich", description=rolesHe, color=0xffa400)
        await interaction.channel.send(embed=embedHe, view=HeritageMenu())

        top = ''
        async for message in interaction.channel.history(limit=1, oldest_first=True):
            top = str(message.jump_url)
        
        embedBacktoTop = discord.Embed(color=0x2c2d31, type='rich', description=f'[^ Back to Top]({top})')
        await interaction.channel.send(embed=embedBacktoTop)