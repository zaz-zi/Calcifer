import discord
from discord.ext import commands
import roles
import rules
import translate
import voice
import dictionaries
import json
import io
import admin
import datetime
import wiktionary
import help
import asyncio
import clubs
from resources import resources
from proofreading import proofreading
from _calcinfo import bot_token, pyre_guild_id

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
client = commands.Bot(intents=intents, command_prefix=commands.when_mentioned_or('c_'))


class PersistentViewBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.all()
        super().__init__(command_prefix=commands.when_mentioned_or('c_'), intents=intents)

    async def setup_hook(self) -> None:
        self.add_view(roles.EnglishMenu())
        self.add_view(roles.RussianMenu())
        self.add_view(roles.HeritageMenu())


client = PersistentViewBot()


@client.event
async def on_ready():
    guild = client.get_guild(pyre_guild_id)
    await client.tree.sync()
    await client.tree.sync(guild=guild)
    await client.get_channel(1079113375918850059).send('Let\'s get a fire going!')
    
    with io.open('channel_ids.json', encoding='utf-8') as file:
        channels = json.load(file)
        muteLog = guild.get_channel(channels['mute-log'])
        async for message in muteLog.history():
            try:
                id = int(message.content.split('[]')[0])
                time = datetime.datetime.strptime(message.content.split(
                    '[]')[1].replace('\n', ''), '%y-%m-%d %H:%M:%S')
                now = datetime.datetime.utcnow()
                passed = now > time
                member = await guild.fetch_member(id)
                mutedRole = guild.get_role(1081677484002648104)
                if passed:
                    if mutedRole in member.roles:
                        await member.remove_roles(mutedRole)
                        await member.send('You have been unmuted')
                    await message.delete()
                else:
                    difference = time - now
                    wait = int(difference.total_seconds())
                    await asyncio.sleep(wait)
                    if mutedRole in member.roles:
                        await member.remove_roles(mutedRole)
                        await member.send('You have been unmuted')
                    await message.delete()
            except:
                await message.delete()


@client.event
async def on_resumed():
    guild = client.get_guild(pyre_guild_id)
    with io.open('channel_ids.json', encoding='utf-8') as file:
        channels = json.load(file)
        muteLog = guild.get_channel(channels['mute-log'])
        async for message in muteLog.history():
            try:
                id = int(message.content.split('[]')[0])
                time = datetime.datetime.strptime(message.content.split('[]')[1].replace('\n', ''), '%y-%m-%d %H:%M:%S')
                now = datetime.datetime.utcnow()
                passed = now > time
                member = await guild.fetch_member(id)
                mutedRole = guild.get_role(1081677484002648104)
                if passed:
                    if mutedRole in member.roles:
                        await member.remove_roles(mutedRole)
                        await member.send('You have been unmuted')
                    await message.delete()
                else:
                    difference = time - now
                    wait = int(difference.total_seconds())
                    await asyncio.sleep(wait)
                    if mutedRole in member.roles:
                        await member.remove_roles(mutedRole)
                        await member.send('You have been unmuted')
                    await message.delete()
            except:
                await message.delete()
    

@client.event
async def on_voice_state_update(member, before, after):
    if after.channel != None:
        if after.channel.id == 1081588020995698708:
            with io.open('channel_ids.json', encoding='utf-8') as file:
                channels = json.load(file)
                botInfo = client.get_channel(channels['bot-info'])
            await after.channel.send(f'{member.mention} type in */voice_create [user limit] [channel name]* to create a temporary channel\n\nFor a more comprehensive list of available commands, please refer to {botInfo.mention}')


@client.event
async def on_member_join(member):
    with io.open('roles.json', encoding='utf-8') as file:
        jsonRoles = json.load(file)
        unverifiedID = jsonRoles['unverified']
    unverified = client.get_guild(1079023618450792498).get_role(unverifiedID)
    with io.open('channel_ids.json', encoding='utf-8') as file:
        channels = json.load(file)
        channel = client.get_channel(channels['welcome'])
        rules = client.get_channel(channels['rules'])
        roles = client.get_channel(channels['roles'])
    await member.add_roles(unverified)
    await channel.send(f"Hello {member.mention} and welcome to PYRE!\nPlease take a moment to read our {rules.mention} and choose your {roles.mention} to get verified and gain full access to the server. If you have any questions, feel free to contact our moderator team. ")


@client.event
async def on_message(message):
    await client.process_commands(message)
    with io.open('channel_ids.json', encoding='utf-8') as file:
        channels = json.load(file)
        proofreading = client.get_channel(channels['proofreading'])
        proofreading_id = str(channels['proofreading'])
    with io.open('proofreading_banned_links.json', encoding='utf-8') as file:
        links = json.load(file)    
    # webhook info
    with io.open('webhook_url.json', encoding='utf-8') as file:
        webhook_info = json.load(file)
        webhook_id = webhook_info['id']
        webhook_token = webhook_info['token']
    if message.channel == proofreading:
        if message.author.id not in {1081285777562013817, webhook_id}:
            text = message.content
            linkFilter = False
            for link in links:
                if link in text:
                    linkFilter = True
            if text != "" and linkFilter == False:
                if len(text) <= 2000:
                    newMessage = await proofreading.send(f'Submission by {message.author.mention}')
                    thread = await newMessage.create_thread(name=f"Submission by @{message.author.name}")
                    await thread.send(text)
                    await message.delete()
                    # look through the last 10 messages for the old pin sent by {webhook_id}
                    async for oldPin in message.channel.history(limit=10):
                        if oldPin.author.id==webhook_id:
                            await oldPin.delete()
                            break
                    newPin_webhook = discord.Webhook.from_url(f'https://discord.com/api/webhooks/{webhook_id}/{webhook_token}', client=client)
                    pins = await proofreading.pins()
                    top = pins[0]
                    # top = ''
                    # async for item in message.channel.history(oldest_first=True, limit=1):
                    #     top = str(message.jump_url)
                    await newPin_webhook.send(content=f'Before posting, please check [our quick guide](https://discord.com/channels/{message.guild.id}/{proofreading_id}/{top.id}) on proper channel usage and text submission instructions.')
                    # await newPin_webhook.send(content=f'Before posting, please check [our quick guide]({top}) on proper channel usage and text submission instructions.')
                else:
                    await proofreading.send(f'{message.author.mention} your message exceeds the 2,000 characters limit. Please refer to the pinned message of this channel for our quick guide on how to properly submit longer texts using Google Docs.', delete_after=20)
                    await message.delete()
            else:
                await proofreading.send(f'{message.author.mention} you cannot post any content other than text (such as pictures, GIFs, or files) in this channel.', delete_after=20)
                await message.delete()


@client.event
async def on_message_delete(message):
    if message.guild.id == pyre_guild_id:
        with io.open('channel_ids.json', encoding='utf-8') as file:
            channels = json.load(file)
            modLog = client.get_channel(channels['mod-log'])
        role = discord.utils.find(
            lambda r: r.name == 'Moderator', client.get_guild(1079023618450792498).roles)
        botRole = discord.utils.find(
            lambda r: r.name == 'Bots', client.get_guild(1079023618450792498).roles)
        if message.author.id != 1081285777562013817:
            if (role not in message.author.roles) and (botRole not in message.author.roles):
                async for entry in message.guild.audit_logs(limit=1, action=discord.AuditLogAction.message_delete):
                    if entry.target == message.author:
                        deleter = entry.user
                        date = f'<t:{str(int(message.created_at.timestamp()))}:d><t:{str(int(message.created_at.timestamp()))}:t>'
                        await modLog.send(f'**{deleter.name}** deleted a message by **{message.author.name}** in {message.channel.mention}:\n({date}) {message.content}')
                    else:
                        date = f'<t:{str(int(message.created_at.timestamp()))}:d><t:{str(int(message.created_at.timestamp()))}:t>'
                        await modLog.send(f'Deleted message by **{message.author.name}** in {message.channel.mention}:\n({date}) **{message.content}**')
                

@client.hybrid_command(name='members', description='Display the current amount of server members. Moderator only.')
async def members(ctx):
    role = discord.utils.find(
        lambda r: r.name == 'Moderator', ctx.guild.roles)
    if role not in ctx.author.roles:
        await ctx.send('You do not have permission to use this command!', ephemeral=True)
    else:
        total = ctx.guild.member_count
        members = len([m for m in ctx.guild.members if not m.bot])
        bots = total - members
        await ctx.send(f'ms: **{members}**\nbots: **{bots}**\ntotal: **{total}**')


@client.tree.command(name='translate', description='Translate a piece of text', guild=discord.Object(id=pyre_guild_id))
async def self(interaction: discord.Interaction, target_lang: str, input: str, source_lang: str = 'auto'):
    await translate.translate(interaction, target_lang, input, source_lang)


@client.tree.command(name='rules', description='Post the server rules. Moderator only.', guild=discord.Object(id=pyre_guild_id))
async def self(interaction: discord.Interaction):
    await rules.rules(interaction)


@client.tree.command(name='rule', description='Post a specific rule. Please specify the rule number and language (ru/en). Moderator only.', guild=discord.Object(id=pyre_guild_id))
async def self(interaction: discord.Interaction, rule_number: str, lang: str):
    await rules.rule(interaction, rule_number=rule_number, lang=lang)


@client.tree.command(name='translate_help', description='Display the full list of languages you can use via the "/translate" command', guild=discord.Object(id=pyre_guild_id))
async def self(interaction: discord.Interaction):
    await translate.help_translate(interaction)


@client.tree.command(name='voice_create', description='Create your own voice channel')
async def self(interaction: discord.Interaction, user_limit: int = 0, channel_name: str = 'default'):
    await voice.create(interaction, client, user_limit, channel_name)


@client.tree.command(name='voice_ban', description='Ban a member from your custom voice channel')
async def self(interaction: discord.Interaction, member: discord.Member):
    await voice.ban(interaction, member)


@client.tree.command(name='voice_unban', description='Unban a member from your custom voice channel')
async def self(interaction: discord.Interaction, member: discord.Member):
    await voice.unban(interaction, member)


@client.tree.command(name='voice_rename', description='Rename your custom voice channel')
async def self(interaction: discord.Interaction, new_name: str):
    await voice.rename(interaction, new_name)


@client.tree.command(name='voice_lock', description='Prevent server members from joining your custom voice channel')
async def self(interaction: discord.Interaction):
    await voice.lock(interaction)


@client.tree.command(name='voice_unlock', description='Allow server members to join your custom voice channel')
async def self(interaction: discord.Interaction):
    await voice.unlock(interaction)


@client.tree.command(name='voice_limit', description='Change the user limit of your custom voice channel')
async def self(interaction: discord.Interaction, new_limit: int):
    await voice.limit(interaction, new_limit)


@client.tree.command(name='define', description='Define a word or phrase')
async def self(interaction: discord.Interaction, input: str, part_of_speech: str = 'all'):
    await wiktionary.wiktionary(interaction, input, part_of_speech)


@client.tree.command(name='urban', description='Look up a word on Urban Dictionary')
async def self(interaction: discord.Interaction, input: str):
    await dictionaries.urban(interaction, input)


@client.tree.command(name='roles', description='Post role selecting menus. Moderator only.', guild=discord.Object(id=pyre_guild_id))
async def self(interaction: discord.Interaction):
    await roles.menuLangs(interaction)


@client.tree.command(name='events', description='Post the Russian Events menu. Moderator only.', guild=discord.Object(id=pyre_guild_id))
async def self(interaction: discord.Interaction):
    await clubs.readingMenu(interaction)


@client.tree.command(name='mute', description='Mute a member. Moderator only.', guild=discord.Object(id=pyre_guild_id))
async def self(interaction: discord.Interaction, member: discord.Member, duration: int, time_unit: str = 'm', reason: str = 'blank'):
    await admin.mute(interaction, member, duration, time_unit, reason)


@client.tree.command(name='unmute', description='Unmute a member. Moderator only.', guild=discord.Object(id=pyre_guild_id))
async def self(interaction: discord.Interaction, member: discord.Member):
    await admin.unmute(interaction, member)


@client.tree.command(name='mute_check', description='Refresh Calcifer\'s mute memory. Moderator only.', guild=discord.Object(id=pyre_guild_id))
async def self(interaction: discord.Interaction):
    await admin.mute_check(interaction)


@client.tree.command(name='ban', description='Ban a member. Moderator only.', guild=discord.Object(id=pyre_guild_id))
async def self(interaction: discord.Interaction, member: discord.Member, reason: str = 'blank'):
    await admin.ban(interaction, member, reason)


@client.tree.command(name='unban', description='Unban a member. Moderator only.')
async def self(interaction: discord.Interaction, member: discord.User):
    await admin.unban(interaction, member)


@client.tree.command(name='kick', description='Kick a member. Moderator only.')
async def self(interaction: discord.Interaction, user: discord.User, reason: str = 'blank'):
    await admin.kick(interaction, user, reason)


@client.tree.command(name='can_do', description='Post the full list of Calcifer\'s available commands. Moderator only.', guild=discord.Object(id=pyre_guild_id))
async def self(interaction: discord.Interaction):
    await help.can_do(interaction)


@client.tree.command(name='help', description='Get info on Calcifer\'s available commands', guild=discord.Object(id=pyre_guild_id))
async def self(interaction: discord.Interaction):
    await help.help(interaction)


@client.tree.command(name='remove', description='Remove up to 100 recent messages. Moderator only.', guild=discord.Object(id=pyre_guild_id))
async def self(interaction: discord.Interaction, amount: int):
    await admin.clear(interaction, amount)


@client.tree.command(name='ru_resources', description='Post Russian learning resources. Moderator only.', guild=discord.Object(id=pyre_guild_id))
async def self(interaction: discord.Interaction):
    await resources.resources(interaction)


@client.tree.command(name='resolved', description='Lock and tag the current post as resolved', guild=discord.Object(id=pyre_guild_id))
async def self(interaction: discord.Interaction):
    await admin.resolve(interaction)


@client.tree.command(name='proofreading', description='Post guidelines for the proofreading channel. Moderator only.', guild=discord.Object(id=pyre_guild_id))
async def self(interaction: discord.Interaction):
    await proofreading.proofreading(interaction)


@client.tree.command(name='language_questions', description='Generate a post with channel guidelines. Moderator only.', guild=discord.Object(id=pyre_guild_id))
async def self(interaction: discord.Interaction):
    await help.nigger(interaction)


@client.tree.command(name='create_post', description='Generate a post in the media channel. Moderator only.', guild=discord.Object(id=pyre_guild_id))
async def self(interaction: discord.Interaction, name: str, description: str):
    await help.createPost(interaction, name, description)


@client.tree.command(name='create_post_set', description='Generate the default set of posts in the media channel. Moderator only.', guild=discord.Object(id=pyre_guild_id))
async def self(interaction: discord.Interaction):
    await help.defaultPost(interaction)

client.run(bot_token) 
