from lxml import html
import requests
import string
import discord


def addPronunciation(tag: str, pronunciations: list, dialects: list):
    tempPronunciations = tag.xpath(f'./following-sibling::ul[1]')[0].text_content().split('\n')
    tempPronunciations = [pronunciation for pronunciation in tempPronunciations if 'IPA(key):' in pronunciation]
    for pronunciation in tempPronunciations:
        dialectStart = pronunciation.find("(") + 1
        dialectEnd = pronunciation.find(")")
        dialect = set(pronunciation[dialectStart:dialectEnd].split(','))

        if 'key' in dialect:
            pronunciations.append(pronunciation[pronunciation.find('IPA(key):') + 10:])

        elif len(dialect.intersection(dialects)) > 0:

            # end of pronunciation
            if pronunciation.rfind('/') > pronunciation.rfind(']'):
                pronunciationStart = pronunciation.find('/')
                pronunciationEnd = pronunciation.rfind('/')
            else:
                pronunciationStart = pronunciation.find('[')
                pronunciationEnd = pronunciation.rfind(']')

            pronunciations.append(pronunciation[dialectStart - 1 : dialectEnd + 1] + ' ' + pronunciation[pronunciationStart : pronunciationEnd + 1])
    
    etymStr = '**Pronunciation**\n\n'
    for pronunciation in pronunciations:
        etymStr += f'{pronunciation}\n\n'

    return etymStr


def addSpeechParts(tag):
    speechPart = tag.xpath(f'./span[@class="mw-headline"]')[0].text
    speechPartStr = f'**{speechPart}**\n\n'

    if tag.xpath('following-sibling::*[1]')[0].tag == 'p':  # class="Latn headword", lang="en"
        underSpeechPart = tag.xpath('following-sibling::*[1]')[0].text_content()
        speechPartStr += f'{underSpeechPart}\n'

    lis = tag.xpath('./following-sibling::ol[1]/li')

    # extract the text from the tag and all its children
    for j, li in enumerate(lis):
        lis[j] = li.text_content().split('\n')[0].strip()

        # usage example if exists
        if len(li.xpath('./dl/dd')) > 0:
            for usageRaw in li.xpath('./dl/dd'):  # alternative: li.xpath('.//div[@class="h-usage-example"]')
                if usageRaw.text_content().split()[0] not in ['Synonym:', 'Synonyms:', 'Antonym:', 'Antonyms:']:
                    usage = usageRaw.text_content()
                    lis[j] += f'\n• *{usage}*'

        elif len(li.xpath('./ol/li/dl/dd')) > 0:
            if li.xpath('./ol/li/dl/dd')[0].text_content().split()[0] not in ['Synonym:', 'Synonyms:', 'Antonym:', 'Antonyms:']:
                usage = li.xpath('./ol/li/dl/dd')[0].text_content()
                lis[j] += f'\n*{usage}*'

    # remove empty entries
    lis = list(filter(None, lis))

    for j, li in enumerate(lis):
        if j < 5:
            speechPartStr += f'{j + 1}) {li}\n\n'

    return speechPartStr


def generateOutput(inputWord: str, speechPart: str):

    output = {}
    speechPart = speechPart.capitalize()
    pronunciations = []
    isPronunBeforeEtym = False
    isPronunFound = False
    isEtymFound = False

    if speechPart == 'All':
        speechParts = [
            'Article', 'Determiner', 'Numeral', 'Noun', 'Pronoun', 'Verb', 'Adjective',
            'Adverb', 'Preposition', 'Postposition', 'Circumposition', 'Ambiposition',
            'Conjunction', 'Interjection', 'Exclamation', 'Particle', 'Clause', 'Proper noun',
            'Participle', 'Phrase'
            ]
    else:
        speechParts = [speechPart]  # break after speechPart is found increases performance

    # IPA(key), (UK), (Received Pronunciation), (Received Pronunciation, General American), (General American), (General American, Canada), (General American, Ireland), (US)
    allDialects = {'UK', 'Received Pronunciation', 'US', 'General American', 'weak vowel merger'}

    if inputWord[0] in string.ascii_letters:
        language = 'English'
    else:
        language = 'Russian'

    url = requests.get(f'https://en.wiktionary.org/wiki/{inputWord}')
    tree = html.fromstring(url.content)

    for i in range(1, len(tree.xpath(f'//h2[span[@id="{language}"]]/following-sibling::*'))):
        currentTag = tree.xpath(f'//h2[span[@id="{language}"]]/following-sibling::*[{i}]')[0]  # why list
        currentTagName = currentTag.tag

        # check what comes first etymology or pronuciation:
        if len(currentTag.xpath(f'./span[@class="mw-headline"]')) > 0 and currentTag.xpath(f'./span[@class="mw-headline"]')[0].text.split()[0] == 'Etymology':
            isEtymFound = True
            if isPronunFound:
                isPronunBeforeEtym = True
                break
        elif len(currentTag.xpath(f'./span[@class="mw-headline"]')) > 0 and currentTag.xpath(f'./span[@class="mw-headline"]')[0].text == 'Pronunciation':
            isPronunFound = True
            if isEtymFound:
                break

    for i in range(1, len(tree.xpath(f'//h2[span[@id="{language}"]]/following-sibling::*'))):
        currentTag = tree.xpath(f'//h2[span[@id="{language}"]]/following-sibling::*[{i}]')[0]  # why list
        currentTagName = currentTag.tag

        # terminate if another language has been reached
        if currentTagName == 'h2':
            break
        
        # if etymology comes before pronoun
        if not isPronunBeforeEtym:
            # Etymology
            if len(currentTag.xpath(f'./span[@class="mw-headline"]')) > 0 and currentTag.xpath(f'./span[@class="mw-headline"]')[0].text.split()[0] == 'Etymology':
                currentEtymology = currentTag.xpath(f'./span[@class="mw-headline"]')[0].text
                output[currentEtymology] = ''

            # Pronunciation
            elif len(currentTag.xpath(f'./span[@class="mw-headline"]')) > 0 and currentTag.xpath(f'./span[@class="mw-headline"]')[0].text == 'Pronunciation':
                output[currentEtymology] += addPronunciation(currentTag, pronunciations, allDialects)

            # Speech parts
            elif len(currentTag.xpath(f'./span[@class="mw-headline"]')) > 0 and currentTag.xpath(f'./span[@class="mw-headline"]')[0].text in speechParts:
                output[currentEtymology] += addSpeechParts(currentTag)

        # if pronoun comes before etymology
        else:
            # Pronunciation
            if len(currentTag.xpath(f'./span[@class="mw-headline"]')) > 0 and currentTag.xpath(f'./span[@class="mw-headline"]')[0].text == 'Pronunciation':
                pronuncations = addPronunciation(currentTag, pronunciations, allDialects)
            
            # Etymology
            elif len(currentTag.xpath(f'./span[@class="mw-headline"]')) > 0 and currentTag.xpath(f'./span[@class="mw-headline"]')[0].text.split()[0] == 'Etymology':
                currentEtymology = currentTag.xpath(f'./span[@class="mw-headline"]')[0].text
                output[currentEtymology] = pronuncations
            
            # Speech parts
            elif len(currentTag.xpath(f'./span[@class="mw-headline"]')) > 0 and currentTag.xpath(f'./span[@class="mw-headline"]')[0].text in speechParts:
                output[currentEtymology] += addSpeechParts(currentTag)

    if len(output) == 0:
        if speechPart == 'All':
            output = 'Word or phrase not found'
        else:
            output = 'The word does not fit into the specified part of speech'

    else:
        for key, value in list(output.items()):
            if not value or value[-3] in ['/', ']']:  # TODO: value[-3] is unreliable, better make a list
                del output[key]
        if len(output) == 0:  # TODO: redo this part
            if speechPart == 'All':
                output = 'Word or phrase not found'  # TODO: remove the dynamic typization
            else:
                output = 'The word does not fit into the specified part of speech'

    return output

class WiktionaryMenu(discord.ui.View):
    def __init__(self, embeds, index):
        super().__init__(timeout=None)
        self.embeds = embeds
        self.index = index
    @discord.ui.button(emoji='<:left:1085573430281252976>', style=discord.ButtonStyle.red, custom_id='left_button')
    async def left(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer()
        if self.index > 0:
            self.index -= 1
            await interaction.message.edit(embed=self.embeds[self.index])
        # left button 
    @discord.ui.button(emoji='<:right:1085573441375178824>', style=discord.ButtonStyle.red, custom_id='right_button')
    async def right(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer()
        if self.index < (len(self.embeds) - 1):
            self.index += 1
            await interaction.message.edit(embed=self.embeds[self.index])
        # right button

async def wiktionary(interaction: discord.Interaction, inpWord: str, speech_part: str = 'all'):
    output = generateOutput(inpWord, speech_part)
    finalString = ''
    for i in output:
        if i != inpWord:
            finalString += f'{i}\n'
    urlStr = inpWord.replace(' ', '_')
    if output != 'Word or phrase not found' and output != 'The word does not fit into the specified part of speech':
        if len(output) == 1:
            file = discord.File('wiktionary_icon.png',filename="wiktionary_icon.png")
            embed = discord.Embed(type='rich', title=inpWord, url=f'https://en.wiktionary.org/wiki/{urlStr}', description=output['Etymology'], color=0xeed6ae)
            embed.set_author(name='Wiktionary', icon_url='attachment://wiktionary_icon.png')
            await interaction.response.send_message(file=file, embed=embed)
        else:
            file = discord.File('wiktionary_icon.png', filename="wiktionary_icon.png")
            embeds = []
            for key, value in output.items():
                embed = discord.Embed(type='rich', title=inpWord, url=f'https://en.wiktionary.org/wiki/{urlStr}', description=f'{key}\n\n{value}', color=0xeed6ae)
                embed.set_author(name='Wiktionary', icon_url='attachment://wiktionary_icon.png')
                embeds.append(embed)
            await interaction.response.send_message(file=file, embed=embeds[0], view=WiktionaryMenu(embeds, 0))
    else:
        file = discord.File('wiktionary_icon.png', filename="wiktionary_icon.png")
        embed = discord.Embed(type='rich', title='Error', description=output, color=0xeed6ae)
        embed.set_author(name='Wiktionary', icon_url='attachment://wiktionary_icon.png')
        await interaction.response.send_message(file=file, embed=embed)