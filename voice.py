import discord


async def create(interaction: discord.Interaction, client: discord.Client, user_limit: int = 0, channel_name: str = 'default'):
    if interaction.user.voice is None:
        await interaction.response.send_message('You have to be in a voice channel to use this command', ephemeral=True, delete_after=20)
    elif len(channel_name) >= len('moderator-onlyssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss') or len(channel_name) < 1:
        await interaction.response.send_message('Invalid channel name length', ephemeral=True, delete_after=20)
    else:
        if user_limit >= 0 and user_limit <= 99:
            guild = interaction.guild
            category = discord.utils.get(
                guild.categories, name='Temporary Voice Channels')
            if category is None:
                category = await guild.create_category('Temporary Voice Channels')
            if channel_name == 'default':
                channel_name = f"{interaction.user.display_name}\'s Channel"
            overwrites = {
                guild.default_role: discord.PermissionOverwrite(connect=True),
                interaction.user: discord.PermissionOverwrite(connect=True, manage_channels=True)
            }
            channel = await category.create_voice_channel(name=channel_name, overwrites=overwrites)
            await channel.edit(user_limit=user_limit)
            await interaction.user.move_to(channel)
            await channel.set_permissions(interaction.user, manage_channels=True)
            await interaction.response.send_message('Your temporary channel has been created', ephemeral=True, delete_after=20)

            def check(x, y, z):
                return len(channel.members) == 0
            await client.wait_for('voice_state_update', check=check)
            await channel.delete()
        else:
            await interaction.response.send_message('You have entered an invalid user limit. Please enter a value between 1 and 99.', ephemeral=True)


async def ban(interaction: discord.Interaction, member: discord.Member):
    guild = interaction.guild
    role = discord.utils.find(lambda r: r.name == 'Moderator', guild.roles)
    if interaction.user.voice is None:
        await interaction.response.send_message('You have to be in your custom channel to use this command', ephemeral=True, delete_after=20)
    elif interaction.user.voice.channel.permissions_for(interaction.user).manage_channels == False:
        await interaction.response.send_message('You do not have permission to ban people from this voice channel', ephemeral=True, delete_after=20)
    elif role in member.roles:
        await interaction.response.send_message('You cannot ban a moderator', ephemeral=True, delete_after=20)
    else:
        channel = interaction.user.voice.channel
        if member.voice is None or member.voice.channel != channel:
            await channel.set_permissions(member, connect=False)
            await interaction.response.send_message(f"{member.display_name} has been banned from this channel", ephemeral=True, delete_after=20)
        elif member.voice.channel == channel:
            await member.move_to(None)
            await channel.set_permissions(member, connect=False)
            await interaction.response.send_message(f"{member.display_name} has been banned from this channel", ephemeral=True, delete_after=20)
            await member.send(f"You have been banned from {interaction.user.display_name}'s channel")


async def unban(interaction: discord.Interaction, member: discord.Member):
    if interaction.user.voice is None:
        await interaction.response.send_message('You have to be in your custom channel to use this command', ephemeral=True, delete_after=20)
    elif interaction.user.voice.channel.permissions_for(interaction.user).manage_channels == False:
        await interaction.response.send_message('You do not have permission to unban people from this voice channel', ephemeral=True, delete_after=20)
    elif interaction.user.voice.channel.permissions_for(member).connect == True:
        await interaction.response.send_message('This user is not banned from this channel', ephemeral=True, delete_after=20)
    else:
        channel = interaction.user.voice.channel
        if member.voice is None or member.voice.channel != channel:
            await channel.set_permissions(member, connect=True)
            await interaction.response.send_message(f"{member.display_name} has been unbanned from this channel", ephemeral=True, delete_after=20)
        elif member.voice.channel == channel:
            await channel.set_permissions(member, connect=True)
            await interaction.response.send_message(f"{member.display_name} has been unbanned from this channel", ephemeral=True, delete_after=20)
            await member.send(f"You have been unbanned from {interaction.user.display_name}'s channel")


async def rename(interaction: discord.Interaction, new_name: str):
    if interaction.user.voice is None:
        await interaction.response.send_message('You have to be in your custom channel to use this command', ephemeral=True, delete_after=20)
    elif interaction.user.voice.channel.permissions_for(interaction.user).manage_channels == False:
        await interaction.response.send_message('You do not have permission to rename this channel', ephemeral=True, delete_after=20)
    elif len(new_name) >= len('moderator-onlyssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss') or len(new_name) < 1:
        await interaction.response.send_message('Invalid channel name length', ephemeral=True, delete_after=20)
    else:
        channel = interaction.user.voice.channel
        await channel.edit(name=f'{new_name}')
        await interaction.response.send_message('Your channel has been renamed', ephemeral=True, delete_after=20)


async def lock(interaction: discord.Interaction):
    if interaction.user.voice is None:
        await interaction.response.send_message('You have to be in your custom channel to use this command', ephemeral=True, delete_after=20)
    elif interaction.user.voice.channel.permissions_for(interaction.user).manage_channels == False:
        await interaction.response.send_message('You do not have permission to lock this channel', ephemeral=True, delete_after=20)
    else:
        guild = interaction.guild
        role = discord.utils.find(lambda r: r.name == 'Moderator', guild.roles)
        channel = interaction.user.voice.channel
        overwrites = {
            guild.default_role: discord.PermissionOverwrite(connect=False),
            interaction.user: discord.PermissionOverwrite(connect=True, manage_channels=True),
            role: discord.PermissionOverwrite(connect=True, manage_channels=True)
        }
        await channel.edit(overwrites=overwrites)
        await interaction.response.send_message('Your channel has been locked', ephemeral=True, delete_after=20)


async def unlock(interaction: discord.Interaction):
    if interaction.user.voice is None:
        await interaction.response.send_message('You have to be in your custom channel to use this command', ephemeral=True, delete_after=20)
    elif interaction.user.voice.channel.permissions_for(interaction.user).manage_channels == False:
        await interaction.response.send_message('You do not have permission to unlock this channel', ephemeral=True, delete_after=20)
    elif interaction.user.voice.channel.permissions_for(interaction.guild.default_role).connect == True:
        await interaction.response.send_message('This channel is not locked', ephemeral=True, delete_after=20)
    else:
        guild = interaction.guild
        channel = interaction.user.voice.channel
        overwrites = {
            guild.default_role: discord.PermissionOverwrite(connect=True),
            interaction.user: discord.PermissionOverwrite(connect=True, manage_channels=True)
        }
        await channel.edit(overwrites=overwrites)
        await interaction.response.send_message('Your channel has been unlocked', ephemeral=True, delete_after=20)
        

async def limit(interaction: discord.Interaction, new_limit: int):
    if interaction.user.voice is None:
        await interaction.response.send_message('You have to be in your custom channel to use this command', ephemeral=True, delete_after=20)
    elif interaction.user.voice.channel.permissions_for(interaction.user).manage_channels == False:
        await interaction.response.send_message('You do not have permission to unlock this channel', ephemeral=True, delete_after=20)
    elif new_limit < 1 or new_limit > 99:
        await interaction.response.send_message('You have entered an invalid user limit. Please enter a value between 1 and 99.', ephemeral=True, delete_after=20)
    else:
        channel = interaction.user.voice.channel
        await channel.edit(user_limit=new_limit)
        await interaction.response.send_message('User limit has been changed!', ephemeral=True, delete_after=20)
