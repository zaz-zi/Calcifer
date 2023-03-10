import discord
import asyncio
import io
import datetime


async def mute(interaction: discord.Interaction, member: discord.Member, duration: int, time_unit: str = 'm', reason: str = 'blank'):
    role = discord.utils.find(lambda r: r.name == 'Moderator', interaction.guild.roles)
    if role not in interaction.user.roles:
        await interaction.response.send_message('You do not have permission to use this command!', ephemeral=True)
    else:
        mutedRole = interaction.guild.get_role(1081677484002648104)
        units = {"s": "seconds", "m": "minutes", "h": "hours", "d": "days"}
        durationDisplayed = duration
        if time_unit == 'm':
            duration *= 60
        elif time_unit == 'h':
            duration *= 60*60
        elif time_unit == 'd':
            duration *= 60*60*24
        if mutedRole not in member.roles:
            await member.add_roles(mutedRole)
            await interaction.response.send_message('The member has been muted', ephemeral=True)
            await member.send(f'You have been muted\nDuration: **{durationDisplayed} {units[time_unit]}**\nReason: **{reason}**')
            with io.open('mutes.txt', 'r+', encoding='utf-8') as file:
                now = datetime.datetime.utcnow()
                unmuteTime = datetime.timedelta(seconds=duration) + now
                file.write(str(member.id) + '[]' +
                        str(unmuteTime.strftime('%y-%m-%d %H:%M:%S') + ''))
            await asyncio.sleep(duration)
            await member.remove_roles(mutedRole)
            await member.send('You have been unmuted')
        else:
            await interaction.response.send_message('This member is already muted!', ephemeral=True)


async def unmute(interaction: discord.Interaction, member: discord.Member):
    role = discord.utils.find(
        lambda r: r.name == 'Moderator', interaction.guild.roles)
    if role not in interaction.user.roles:
        await interaction.response.send_message('You do not have permission to use this command!', ephemeral=True)
    else:
        mutedRole = interaction.guild.get_role(1081677484002648104)
        if mutedRole in member.roles:
            member.remove_roles(mutedRole)
            member.send('You have been unmuted')
            interaction.response.send_message('The member has been unmuted', ephemeral=True)
        else:
            interaction.response.send_message('The member is not muted!')


async def mute_check(interaction: discord.Interaction):
    role = discord.utils.find(lambda r: r.name == 'Moderator', interaction.guild.roles)
    if role not in interaction.user.roles:
        await interaction.response.send_message('You do not have permission to use this command!', ephemeral=True)
    else:
        await interaction.response.send_message('.', ephemeral=True)
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
        await interaction.response.send_message('You do not have permission to use this command!', ephemeral=True)
    else:
        await member.send(f'You have been banned\nReason: **{reason}**')
        await member.ban()
        await interaction.response.send_message('The user has been banned', ephemeral=True)
        
        
async def unban(interaction: discord.Interaction, user: discord.User):
    role = discord.utils.find(
        lambda r: r.name == 'Moderator', interaction.guild.roles)
    if role not in interaction.user.roles:
        await interaction.response.send_message('You do not have permission to use this command!', ephemeral=True)
    else:
        # banned = interaction.guild.bans()
        # if user in banned:
        await interaction.guild.unban(user)
        await interaction.response.send_message('The user has been unbanned', ephemeral=True)


async def kick(interaction: discord.Interaction, member: discord.Member, reason: str = 'blank'):
    role = discord.utils.find(
        lambda r: r.name == 'Moderator', interaction.guild.roles)
    if role not in interaction.user.roles:
        await interaction.response.send_message('You do not have permission to use this command!', ephemeral=True)
    else:
        await member.send(f'You have been kicked\nReason: **{reason}**')
        await member.kick()
        await interaction.response.send_message('The user has been kicked', ephemeral=True)
