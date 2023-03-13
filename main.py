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
from datetime import datetime
import wiktionary
import help

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
    await client.tree.sync()
    await client.tree.sync(guild=discord.Object(id=1079023618450792498))
    print('Bot online!')


@client.event
async def on_voice_state_update(member, before, after):
    if after.channel != None:
        if after.channel.id == 1081588020995698708:  # id канала который нужно мониторить
            botCommands = client.get_channel(1081588020995698708)
            botInfo = client.get_channel(1081670787699855412)
            await botCommands.send(f'{member.mention} type in "/voice_create [user limit] [channel name]" to create a temporary channel\n\nFor a more comprehensive list of available commands, please refer to {botInfo.mention}')


@client.event
async def on_member_join(member):
    with io.open('roles.json', encoding='utf-8') as file:
        jsonRoles = json.load(file)
        unverifiedID = jsonRoles['unverified']
    unverified = client.get_guild(1079023618450792498).get_role(unverifiedID)
    channel = client.get_channel(1079080374992392292)
    rules = client.get_channel(1079080406328021124)
    roles = client.get_channel(1079081151706173654)
    introductions = client.get_channel(1079080326132936815)
    await member.add_roles(unverified)
    await channel.send(f"Hello {member.mention} and welcome to PYRE!\nPlease take a moment to read our {rules.mention} and choose your {roles.mention} to get verified and gain full access to the server. If you have any questions, feel free to contact our moderator team. ")


@client.tree.command(name='translate', description='Translate a piece of text', guild=discord.Object(id=1079023618450792498))
async def self(interaction: discord.Interaction, target_lang: str, phrase: str):
    await translate.translate(interaction, target_lang, phrase)


@client.tree.command(name='rules', description='Display server rules. Moderator only.', guild=discord.Object(id=1079023618450792498))
async def self(interaction: discord.Interaction):
    await rules.rules(interaction)


@client.tree.command(name='rule', description='Display a specific rule. Please specify rule number and language (ru/en). Moderator only.', guild=discord.Object(id=1079023618450792498))
async def self(interaction: discord.Interaction, rule_number: str, lang: str):
    await rules.rule(interaction, rule_number=rule_number, lang=lang)


@client.tree.command(name='help_translate', description='Display the full list of languages you can use via the "/translate" command', guild=discord.Object(id=1079023618450792498))
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
async def self(interaction: discord.Interaction, word: str, part_of_speech: str = 'all'):
    await wiktionary.wiktionary(interaction, word, part_of_speech)


@client.tree.command(name='urban', description='Look up a word on Urban Dictionary')
async def self(interaction: discord.Interaction, word: str):
    await dictionaries.urban(interaction, word)


@client.tree.command(name='roles', description='Display role selecting menus. Moderator only.', guild=discord.Object(id=1079023618450792498))
async def self(interaction: discord.Interaction):
    await roles.menuLangs(interaction)


@client.tree.command(name='mute', description='Mute a member. Moderator only.', guild=discord.Object(id=1079023618450792498))
async def self(interaction: discord.Interaction, member: discord.Member, duration: int, time_unit: str = 's', reason: str = 'blank'):
    await admin.mute(interaction, member, duration, time_unit, reason)


@client.tree.command(name='unmute', description='Unmute a member. Moderator only.', guild=discord.Object(id=1079023618450792498))
async def self(interaction: discord.Interaction, member: discord.Member):
    await admin.unmute(interaction, member)


@client.tree.command(name='mute_check', description='Moderator only', guild=discord.Object(id=1079023618450792498))
async def self(interaction: discord.Interaction):
    await admin.mute_check(interaction)


@client.tree.command(name='ban', description='Ban a member. Moderator only.', guild=discord.Object(id=1079023618450792498))
async def self(interaction: discord.Interaction, member: discord.Member, reason: str = 'blank'):
    await admin.ban(interaction, member, reason)


@client.tree.command(name='unban', description='Unban a member. Moderator only.', guild=discord.Object(id=1079023618450792498))
async def self(interaction: discord.Interaction, member: discord.User):
    await admin.unban(interaction, member)


@client.tree.command(name='kick', description='Kick a member. Moderator only.', guild=discord.Object(id=1079023618450792498))
async def self(interaction: discord.Interaction, user: discord.User, reason: str = 'blank'):
    await admin.kick(interaction, user, reason)


@client.tree.command(name='can_do', description='Moderator only')
async def self(interaction: discord.Interaction):
    await help.can_do(interaction)


client.run(
    'MTA4MTI4NTc3NzU2MjAxMzgxNw.GqCV_E.V4cvIG-YxYlk4XZTf8IbUfAOjUvbT_qAbrxo2M')
