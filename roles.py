import discord
import io
import json


class EnglishMenu(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label='Beginner', style=discord.ButtonStyle.red, custom_id='en1')
    async def selfEnBeginner(self, interaction: discord.Interaction, Button: discord.ui.Button):
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
                if interaction.user.guild.get_role(item) in interaction.user.roles:
                    alreadyHas = True
            if alreadyHas == True:
                await interaction.response.send_message('You already have an English role!', ephemeral=True, delete_after=20)
            else:
                verified = False
                for item in ruRoles:
                    if interaction.user.guild.get_role(item) in interaction.user.roles:
                        if unverified in interaction.user.roles:
                            await interaction.user.remove_roles(unverified)
                            introductions = interaction.guild.get_channel(1079080326132936815)
                            general = interaction.guild.get_channel(1079023618983464986)
                            languageQuestions = interaction.guild.get_channel(1079073206570328115)
                            verified = True
                await interaction.user.add_roles(role)
                if verified == False:
                    await interaction.response.send_message('Role granted', ephemeral=True, delete_after=20)
                else:
                    await interaction.response.send_message(f"Congrats on getting verified {interaction.user.mention}!\nDon't forget to {introductions.mention}, and check out {general.mention} to say hi to the others! If you have any questions related to Russian or English, you can refer to {languageQuestions.mention}.\n Enjoy your stay!", ephemeral=True, delete_after=60*60*2)

    @discord.ui.button(label='Intermediate', style=discord.ButtonStyle.red, custom_id='en2')
    async def selfEnIntermediate(self, interaction: discord.Interaction, Button: discord.ui.Button):
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
                if interaction.user.guild.get_role(item) in interaction.user.roles:
                    alreadyHas = True
            if alreadyHas == True:
                await interaction.response.send_message('You already have an English role!', ephemeral=True, delete_after=20)
            else:
                verified = False
                for item in ruRoles:
                    if interaction.user.guild.get_role(item) in interaction.user.roles:
                        if unverified in interaction.user.roles:
                            await interaction.user.remove_roles(unverified)
                            introductions = interaction.guild.get_channel(
                                1079080326132936815)
                            general = interaction.guild.get_channel(
                                1079023618983464986)
                            languageQuestions = interaction.guild.get_channel(
                                1079073206570328115)
                            verified = True
                await interaction.user.add_roles(role)
                if verified == False:
                    await interaction.response.send_message('Role granted', ephemeral=True, delete_after=20)
                else:
                    await interaction.response.send_message(f"Congrats on getting verified {interaction.user.mention}!\nDon't forget to {introductions.mention}, and check out {general.mention} to say hi to the others! If you have any questions related to Russian or English, you can refer to {languageQuestions.mention}.\n Enjoy your stay!", ephemeral=True, delete_after=60*60*2)

    @discord.ui.button(label='Advanced', style=discord.ButtonStyle.red, custom_id='en3')
    async def selfEnAdvanced(self, interaction: discord.Interaction, Button: discord.ui.Button):
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
                if interaction.user.guild.get_role(item) in interaction.user.roles:
                    alreadyHas = True
            if alreadyHas == True:
                await interaction.response.send_message('You already have an English role!', ephemeral=True, delete_after=20)
            else:
                verified = False
                for item in ruRoles:
                    if interaction.user.guild.get_role(item) in interaction.user.roles:
                        if unverified in interaction.user.roles:
                            await interaction.user.remove_roles(unverified)
                            introductions = interaction.guild.get_channel(
                                1079080326132936815)
                            general = interaction.guild.get_channel(
                                1079023618983464986)
                            languageQuestions = interaction.guild.get_channel(
                                1079073206570328115)
                            verified = True
                await interaction.user.add_roles(role)
                if verified == False:
                    await interaction.response.send_message('Role granted', ephemeral=True, delete_after=20)
                else:
                    await interaction.response.send_message(f"Congrats on getting verified {interaction.user.mention}!\nDon't forget to {introductions.mention}, and check out {general.mention} to say hi to the others! If you have any questions related to Russian or English, you can refer to {languageQuestions.mention}.\n Enjoy your stay!", ephemeral=True, delete_after=60*60*2)

    @discord.ui.button(label='Native Speaker', style=discord.ButtonStyle.red, custom_id='en4')
    async def selfEnNative(self, interaction: discord.Interaction, Button: discord.ui.Button):
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
                if interaction.user.guild.get_role(item) in interaction.user.roles:
                    alreadyHas = True
            if alreadyHas == True:
                await interaction.response.send_message('You already have an English role!', ephemeral=True, delete_after=20)
            else:
                verified = False
                for item in ruRoles:
                    if interaction.user.guild.get_role(item) in interaction.user.roles:
                        if unverified in interaction.user.roles:
                            await interaction.user.remove_roles(unverified)
                            introductions = interaction.guild.get_channel(
                                1079080326132936815)
                            general = interaction.guild.get_channel(
                                1079023618983464986)
                            languageQuestions = interaction.guild.get_channel(
                                1079073206570328115)
                            verified = True
                await interaction.user.add_roles(role)
                if verified == False:
                    await interaction.response.send_message('Role granted', ephemeral=True, delete_after=20)
                else:
                    await interaction.response.send_message(f"Congrats on getting verified {interaction.user.mention}!\nDon't forget to {introductions.mention}, and check out {general.mention} to say hi to the others! If you have any questions related to Russian or English, you can refer to {languageQuestions.mention}.\n Enjoy your stay!", ephemeral=True, delete_after=60*60*2)


class RussianMenu(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label='Beginner', style=discord.ButtonStyle.red, custom_id='ru1')
    async def selfRuBeginner(self, interaction: discord.Interaction, Button: discord.ui.Button):
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
                if interaction.user.guild.get_role(item) in interaction.user.roles:
                    alreadyHas = True
            if alreadyHas == True:
                await interaction.response.send_message('You already have a Russian role!', ephemeral=True, delete_after=20)
            else:
                verified = False
                for item in enRoles:
                    if interaction.user.guild.get_role(item) in interaction.user.roles:
                        if unverified in interaction.user.roles:
                            await interaction.user.remove_roles(unverified)
                            introductions = interaction.guild.get_channel(1079080326132936815)
                            general = interaction.guild.get_channel(1079023618983464986)
                            languageQuestions = interaction.guild.get_channel(1079073206570328115)
                            verified = True
                await interaction.user.add_roles(role)
                if verified == False:
                    await interaction.response.send_message('Role granted', ephemeral=True, delete_after=20)
                else:
                    await interaction.response.send_message(f"Congrats on getting verified {interaction.user.mention}!\nDon't forget to {introductions.mention}, and check out {general.mention} to say hi to the others! If you have any questions related to Russian or English, you can refer to {languageQuestions.mention}.\n Enjoy your stay!", ephemeral=True, delete_after=60*60*2)

    @discord.ui.button(label='Intermediate', style=discord.ButtonStyle.red, custom_id='ru2')
    async def selfRuIntermediate(self, interaction: discord.Interaction, Button: discord.ui.Button):
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
                if interaction.user.guild.get_role(item) in interaction.user.roles:
                    alreadyHas = True
            if alreadyHas == True:
                await interaction.response.send_message('You already have a Russian role!', ephemeral=True, delete_after=20)
            else:
                verified = False
                for item in enRoles:
                    if interaction.user.guild.get_role(item) in interaction.user.roles:
                        if unverified in interaction.user.roles:
                            await interaction.user.remove_roles(unverified)
                            introductions = interaction.guild.get_channel(1079080326132936815)
                            general = interaction.guild.get_channel(1079023618983464986)
                            languageQuestions = interaction.guild.get_channel(1079073206570328115)
                            verified = True
                await interaction.user.add_roles(role)
                if verified == False:
                    await interaction.response.send_message('Role granted', ephemeral=True, delete_after=20)
                else:
                    await interaction.response.send_message(f"Congrats on getting verified {interaction.user.mention}!\nDon't forget to {introductions.mention}, and check out {general.mention} to say hi to the others! If you have any questions related to Russian or English, you can refer to {languageQuestions.mention}.\n Enjoy your stay!", ephemeral=True, delete_after=60*60*2)

    @discord.ui.button(label='Advanced', style=discord.ButtonStyle.red, custom_id='ru3')
    async def selfRuAdvanced(self, interaction: discord.Interaction, Button: discord.ui.Button):
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
                if interaction.user.guild.get_role(item) in interaction.user.roles:
                    alreadyHas = True
            if alreadyHas == True:
                await interaction.response.send_message('You already have a Russian role!', ephemeral=True, delete_after=20)
            else:
                verified = False
                for item in enRoles:
                    if interaction.user.guild.get_role(item) in interaction.user.roles:
                        if unverified in interaction.user.roles:
                            await interaction.user.remove_roles(unverified)
                            introductions = interaction.guild.get_channel(1079080326132936815)
                            general = interaction.guild.get_channel(1079023618983464986)
                            languageQuestions = interaction.guild.get_channel(1079073206570328115)
                            verified = True
                await interaction.user.add_roles(role)
                if verified == False:
                    await interaction.response.send_message('Role granted', ephemeral=True, delete_after=20)
                else:
                    await interaction.response.send_message(f"Congrats on getting verified {interaction.user.mention}!\nDon't forget to {introductions.mention}, and check out {general.mention} to say hi to the others! If you have any questions related to Russian or English, you can refer to {languageQuestions.mention}.\n Enjoy your stay!", ephemeral=True, delete_after=60*60*2)

    @discord.ui.button(label='Native Speaker', style=discord.ButtonStyle.red, custom_id='ru4')
    async def selfRuNative(self, interaction: discord.Interaction, Button: discord.ui.Button):
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
                if interaction.user.guild.get_role(item) in interaction.user.roles:
                    alreadyHas = True
            if alreadyHas == True:
                await interaction.response.send_message('You already have a Russian role!', ephemeral=True, delete_after=20)
            else:
                verified = False
                for item in enRoles:
                    if interaction.user.guild.get_role(item) in interaction.user.roles:
                        if unverified in interaction.user.roles:
                            await interaction.user.remove_roles(unverified)
                            introductions = interaction.guild.get_channel(1079080326132936815)
                            general = interaction.guild.get_channel(1079023618983464986)
                            languageQuestions = interaction.guild.get_channel(1079073206570328115)
                            verified = True
                await interaction.user.add_roles(role)
                if verified == False:
                    await interaction.response.send_message('Role granted', ephemeral=True, delete_after=20)
                else:
                    await interaction.response.send_message(f"Congrats on getting verified {interaction.user.mention}!\nDon't forget to {introductions.mention}, and check out {general.mention} to say hi to the others! If you have any questions related to Russian or English, you can refer to {languageQuestions.mention}.\n Enjoy your stay!", ephemeral=True, delete_after=60*60*2)


class HeritageMenu(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label='Heritage Speaker', style=discord.ButtonStyle.red, custom_id='he1')
    async def selfHeritage(self, interaction: discord.Interaction, Button: discord.ui.Button):
        role = interaction.user.guild.get_role(1079413567209611304)
        if role in interaction.user.roles:
            await interaction.user.remove_roles(role)
            await interaction.response.send_message('Role revoked', ephemeral=True, delete_after=20)
        else:
            await interaction.user.add_roles(role)
            await interaction.response.send_message('Role granted', ephemeral=True, delete_after=20)


async def menuLangs(interaction: discord.Interaction):
    with io.open('roles.json', encoding='utf-8') as file:
        jsonRoles = json.load(file)
        rolesHe = jsonRoles['he']
        rundown = jsonRoles['description']
    embedRundown = discord.Embed(
        type="rich", description=rundown, color=0xffa400)
    await interaction.channel.send(embed=embedRundown)
    await interaction.response.send_message('.', ephemeral=True)
    embedEn = discord.Embed(
        type="rich", title='**Please choose the English language proficiency role that best fits your current ability level\n\nВыберите роль, соответствующую Вашему уровню владения английским языком**', color=0xffa400)
    await interaction.channel.send(embed=embedEn, view=EnglishMenu())

    embedRu = discord.Embed(
        type="rich", title='**Please choose the Russian language proficiency role that best fits your current ability level\n\nВыберите роль, соответствующую Вашему уровню владения русским языком**', color=0xffa400)
    await interaction.channel.send(embed=embedRu, view=RussianMenu())
    embedHe = discord.Embed(
        type="rich", description=rolesHe, color=0xffa400)
    await interaction.channel.send(embed=embedHe, view=HeritageMenu())
