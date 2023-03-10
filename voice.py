import discord


async def create(interaction: discord.Interaction, client: discord.Client, user_limit: int = 0, channel_name: str = 'default'):
    if interaction.user.voice is None:
        await interaction.response.send_message('You have to be in a voice channel to use this command!', ephemeral=True)
    else:
        guild = interaction.guild
        category = discord.utils.get(
            guild.categories, name='Temporary Channels')
        if category is None:
            category = await guild.create_category('Temporary Channels')
        if channel_name == 'default':
            channel_name = f"{interaction.user.display_name}\'s Channel"
        overwrites = {
            guild.default_role: discord.PermissionOverwrite(connect=True),
            interaction.user: discord.PermissionOverwrite(connect=True)
        }
        channel = await category.create_voice_channel(name=channel_name, overwrites=overwrites)
        await channel.edit(user_limit=user_limit)
        await interaction.user.move_to(channel)
        await channel.set_permissions(interaction.user, manage_channels=True)
        await interaction.response.send_message('Your temporary channel has been created!', ephemeral=True)

        def check(x, y, z):
            return len(channel.members) == 0
        await client.wait_for('voice_state_update', check=check)
        await channel.delete()


async def ban(interaction: discord.Interaction, member: discord.Member):
    guild = interaction.guild
    role = discord.utils.find(lambda r: r.name == 'Moderator', guild.roles)
    if interaction.user.voice is None:
        await interaction.response.send_message('You have to be in your custom channel to use this command!', ephemeral=True)
    elif interaction.user.voice.channel.permissions_for(interaction.user).manage_channels == False:
        await interaction.response.send_message('You do not have permission to ban people from this voice channel!', ephemeral=True)
    elif role in member.roles:
        await interaction.response.send_message('You cannot ban a moderator!', ephemeral=True)
    else:
        channel = interaction.user.voice.channel
        if member.voice is None or member.voice.channel != channel:
            await channel.set_permissions(member, connect=False)
            await interaction.response.send_message(f"{member.display_name} has been banned from {channel.name}!", ephemeral=True)
        elif member.voice.channel == channel:
            await member.move_to(None)
            await channel.set_permissions(member, connect=False)
            await interaction.response.send_message(f"{member.display_name} has been banned from {channel.name}!", ephemeral=True)
            await member.send(f"You have been banned from {interaction.user.display_name}'s channel!")


async def unban(interaction: discord.Interaction, member: discord.Member):
    if interaction.user.voice is None:
        await interaction.response.send_message('You have to be in your custom channel to use this command!', ephemeral=True)
    elif interaction.user.voice.channel.permissions_for(interaction.user).manage_channels == False:
        await interaction.response.send_message('You do not have permission to unban people from this voice channel!', ephemeral=True)
    else:
        channel = interaction.user.voice.channel
        if member.voice is None or member.voice.channel != channel:
            await channel.set_permissions(member, connect=True)
            await interaction.response.send_message(f"{member.display_name} has been unbanned from {channel.name}!", ephemeral=True)
        elif member.voice.channel == channel:
            await channel.set_permissions(member, connect=True)
            await interaction.response.send_message(f"{member.display_name} has been unbanned from {channel.name}!", ephemeral=True)
            await member.send(f"You have been unbanned from {interaction.user.display_name}'s channel!")


async def rename(interaction: discord.Interaction, new_name: str):
    if interaction.user.voice is None:
        await interaction.response.send_message('You have to be in your custom channel to use this command!', ephemeral=True)
    elif interaction.user.voice.channel.permissions_for(interaction.user).manage_channels == False:
        await interaction.response.send_message('You do not have permission to rename this channel!', ephemeral=True)
    else:
        channel = interaction.user.voice.channel
        await channel.edit(name=f'{new_name}')
        await interaction.response.send_message('Your channel has been renamed!', ephemeral=True)


async def lock(interaction: discord.Interaction):
    if interaction.user.voice is None:
        await interaction.response.send_message('You have to be in your custom channel to use this command!', ephemeral=True)
    elif interaction.user.voice.channel.permissions_for(interaction.user).manage_channels == False:
        await interaction.response.send_message('You do not have permission to lock this channel!', ephemeral=True)
    else:
        guild = interaction.guild
        channel = interaction.user.voice.channel
        overwrites = {
            guild.default_role: discord.PermissionOverwrite(connect=False),
            interaction.user: discord.PermissionOverwrite(connect=True)
        }
        await channel.edit(overwrites=overwrites)
        await interaction.response.send_message('Your channel has been locked!', ephemeral=True)


async def unlock(interaction: discord.Interaction):
    if interaction.user.voice is None:
        await interaction.response.send_message('You have to be in your custom channel to use this command!', ephemeral=True)
    elif interaction.user.voice.channel.permissions_for(interaction.user).manage_channels == False:
        await interaction.response.send_message('You do not have permission to unlock this channel!', ephemeral=True)
    else:
        guild = interaction.guild
        channel = interaction.user.voice.channel
        overwrites = {
            guild.default_role: discord.PermissionOverwrite(connect=True),
            interaction.user: discord.PermissionOverwrite(connect=True)
        }
        await channel.edit(overwrites=overwrites)
        await interaction.response.send_message('Your channel has been unlocked!', ephemeral=True)


async def limit(interaction: discord.Interaction, new_limit: int):
    if interaction.user.voice is None:
        await interaction.response.send_message('You have to be in your custom channel to use this command!', ephemeral=True)
    elif interaction.user.voice.channel.permissions_for(interaction.user).manage_channels == False:
        await interaction.response.send_message('You do not have permission to unlock this channel!', ephemeral=True)
    elif new_limit < 1 or new_limit > 99:
        await interaction.response.send_message('Please give a number between 1 and 99', ephemeral=True)
    else:
        channel = interaction.user.voice.channel
        await channel.edit(user_limit=new_limit)
        await interaction.response.send_message('User limit has been changed!', ephemeral=True)
