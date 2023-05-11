import discord
import asyncio
import io
import datetime
import json


async def mute(interaction: discord.Interaction, member: discord.Member, duration: int, time_unit: str = 'm', reason: str = 'blank'):
    role = discord.utils.find(lambda r: r.name == 'Moderator', interaction.guild.roles)
    if role not in interaction.user.roles:
        await interaction.response.send_message('You do not have permission to use this command!', ephemeral=True, delete_after=20)
    else:
        try:
            mutedRole = interaction.guild.get_role(1081677484002648104)
            units = {"s": "seconds", "m": "minutes", "h": "hours", "d": "days"}
            durationDisplayed = duration
            if time_unit == 'm' or time_unit == 'minutes' or time_unit == 'minute':
                duration *= 60
                time_unit = 'm'
            elif time_unit == 'h' or time_unit == 'hours' or time_unit == 'hour':
                duration *= 60*60
                time_unit = 'h'
            elif time_unit == 'd' or time_unit == 'days' or time_unit == 'day':
                duration *= 60*60*24
                time_unit = 'd'
            if mutedRole not in member.roles:
                with io.open('channel_ids.json', encoding='utf-8') as file:
                    channels = json.load(file)
                    muteLog = interaction.guild.get_channel(channels['mute-log'])
                    now = datetime.datetime.utcnow()
                    unmuteTime = datetime.timedelta(seconds=duration) + now
                    log = str(member.id) + '[]' + str(unmuteTime.strftime('%y-%m-%d %H:%M:%S') + '')
                    await muteLog.send(content=log, delete_after=duration)

                await member.add_roles(mutedRole)
                await interaction.response.send_message('The member has been muted')
                await member.send(f'You have been muted\nDuration: **{durationDisplayed} {units[time_unit]}**\nReason: **{reason}**')

                await member.add_roles(mutedRole)
                await interaction.response.send_message('The member has been muted')
                await member.send(f'You have been muted\nDuration: **{durationDisplayed} {units[time_unit]}**\nReason: **{reason}**')

                await asyncio.sleep(duration)
                await member.remove_roles(mutedRole)
                await member.send('You have been unmuted')
            else:
                await interaction.response.send_message('This member is already muted!', ephemeral=True, delete_after=20)
        except:
            await interaction.response.send_message('Something went wrong. Please make sure you have provided the correct user ID.', ephemeral=True, delete_after=10)


async def unmute(interaction: discord.Interaction, member: discord.Member):
    role = discord.utils.find(
        lambda r: r.name == 'Moderator', interaction.guild.roles)
    if role not in interaction.user.roles:
        await interaction.response.send_message('You do not have permission to use this command!', ephemeral=True, delete_after=20)
    else:
        try:
            mutedRole = interaction.guild.get_role(1081677484002648104)
            if mutedRole in member.roles:
                await member.remove_roles(mutedRole)
                await member.send('You have been unmuted')
                await interaction.response.send_message('The member has been unmuted')
            else:
                await interaction.response.send_message('Something went wrong. Please make sure you have provided the correct user ID.', ephemeral=True, delete_after=10)
        except:
            await interaction.response.send_message('Something went wrong. Please make sure you have provided the correct user ID.', ephemeral=True, delete_after=10)


async def mute_check(interaction: discord.Interaction):
    role = discord.utils.find(lambda r: r.name == 'Moderator', interaction.guild.roles)
    if role not in interaction.user.roles:
        await interaction.response.send_message('You do not have permission to use this command!', ephemeral=True, delete_after=20)
    else:
        await interaction.response.send_message('Please stand by', ephemeral=True, delete_after=20)
        with io.open('mutes.txt', 'r+', encoding='utf-8') as file:
            inputData = file.readlines()
            for item in inputData:
                id = int(item.split('[]')[0])
                time = datetime.datetime.strptime(item.split(
                    '[]')[1].replace('\n', ''), '%y-%m-%d %H:%M:%S')
                now = datetime.datetime.utcnow()
                passed = now > time
                member = await interaction.guild.fetch_member(id)
                mutedRole = interaction.guild.get_role(1081677484002648104)
                if passed:
                    if mutedRole in member.roles:
                        await member.remove_roles(mutedRole)
                        await member.send('You have been unmuted')
                    with open("mutes.txt", "r+") as f:
                        new_f = f.readlines()
                        f.seek(0)
                        for line in new_f:
                            if item not in line:
                                f.write(line)
                        f.truncate()
                else:
                    difference = time - now
                    wait = int(difference.total_seconds())
                    await asyncio.sleep(wait)
                    if mutedRole in member.roles:
                        await member.remove_roles(mutedRole)
                        await member.send('You have been unmuted')
                    with open("mutes.txt", "r+") as f:
                        new_f = f.readlines()
                        f.seek(0)
                        for line in new_f:
                            if item not in line:
                                f.write(line)
                        f.truncate()


async def ban(interaction: discord.Interaction, member: discord.Member, reason: str = 'blank'):
    role = discord.utils.find(lambda r: r.name == 'Moderator', interaction.guild.roles)
    if role not in interaction.user.roles:
        await interaction.response.send_message('You do not have permission to use this command!', ephemeral=True, delete_after=20)
    else:
        try:
            await member.send(f'You have been banned\nReason: **{reason}**')
            await member.ban()
            await interaction.response.send_message('The user has been banned', ephemeral=True, delete_after=20)
        except:
            await interaction.response.send_message('Something went wrong. Please make sure you have provided the correct user ID.', ephemeral=True, delete_after=20)
        
        
async def unban(interaction: discord.Interaction, user: discord.User):
    role = discord.utils.find(
        lambda r: r.name == 'Moderator', interaction.guild.roles)
    if role not in interaction.user.roles:
        await interaction.response.send_message('You do not have permission to use this command!', ephemeral=True, delete_after=20)
    else:
        try:
            await interaction.guild.unban(user)
            await interaction.response.send_message('The user has been unbanned', ephemeral=True, delete_after=20)
        except:
            await interaction.response.send_message('Something went wrong. Please make sure you have provided the correct user ID.', ephemeral=True, delete_after=20)


async def kick(interaction: discord.Interaction, member: discord.Member, reason: str = 'blank'):
    role = discord.utils.find(
        lambda r: r.name == 'Moderator', interaction.guild.roles)
    if role not in interaction.user.roles:
        await interaction.response.send_message('You do not have permission to use this command!', ephemeral=True, delete_after=20)
    else:    
        try:
            await member.send(f'You have been kicked\nReason: **{reason}**')
            await member.kick()
            await interaction.response.send_message('The user has been kicked', ephemeral=True, delete_after=20) 
        except:
            await interaction.response.send_message('Something went wrong. Please make sure you have provided the correct user ID.', ephemeral=True, delete_after=20)


async def clear(interaction: discord.Interaction, amount: int):
    role = discord.utils.find(
        lambda r: r.name == 'Moderator', interaction.guild.roles)
    if role not in interaction.user.roles:
        await interaction.response.send_message('You do not have permission to use this command!', ephemeral=True, delete_after=20)
    else:
        if amount <= 100:
            channel = interaction.channel
            await interaction.response.send_message('Please stand by', ephemeral=True)
            count = 0
            async for _ in channel.history(limit=amount):
                count += 1
            await channel.purge(limit=amount)
            await channel.send(f'{count} messages deleted', delete_after=20) 
        else:
            await interaction.response.send_message('You cannot delete more than 100 messages', ephemeral=True, delete_after=20)

async def resolve(interaction: discord.Interaction):
    if interaction.channel.permissions_for(interaction.user).manage_channels == True or interaction.user == interaction.channel.owner:
        with io.open('channel_ids.json', encoding='utf-8') as file:
            channels = json.load(file)
            languageQuestions = interaction.guild.get_channel(channels['language-questions'])
        if interaction.channel in languageQuestions.threads:
            interaction.channel.locked = True
            await interaction.channel.edit(locked=True)
            for tag in languageQuestions.available_tags:
                if 'Resolved' in tag.name:
                    resolvedTag = tag
            await interaction.channel.add_tags(resolvedTag)
            print(f'{interaction.channel.locked} {interaction.channel.id}')
            await interaction.response.send_message('This post has been locked')
        else:
            await interaction.response.send_message(f'You can only use this command in a {languageQuestions.mention} post')
    else:
        await interaction.response.send_message('You do not have permission to use this command in this channel', ephemeral=True, delete_after=20)