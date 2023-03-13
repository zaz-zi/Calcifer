from lxml import html
import requests
import string
import discord

def generateOutput(inputWord: str, speechPart: str):

    output = ''
    speechPart = speechPart.capitalize()

    if speechPart == 'All':
        speechParts = [
            'Article', 'Determiner', 'Numeral', 'Noun', 'Pronoun', 'Verb', 'Adjective',
            'Adverb', 'Preposition', 'Postposition', 'Circumposition', 'Ambiposition',
            'Conjunction', 'Interjection', 'Exclamation', 'Particle', 'Clause', 'Proper noun',
            'Participle', 'Phrase'
            ]
    else:
        speechParts = [speechPart]  # break after speechPart is found increases performance

    if inputWord[0] in string.ascii_letters:
        language = 'English'
    else:
        language = 'Russian'

    url = requests.get(f'https://en.wiktionary.org/wiki/{inputWord}')
    tree = html.fromstring(url.content)

    for i in range(1, len(tree.xpath(f'//h2[span[@id="{language}"]]/following-sibling::*'))):
        currentTag = tree.xpath(f'//h2[span[@id="{language}"]]/following-sibling::*[{i}]')[0]  # why list
        currentTagName = currentTag.tag

        if currentTagName == 'h2':
            break

        # elif currentTagName in ['h3', 'h4']:
        elif len(currentTag.xpath(f'./span[@class="mw-headline"]')) > 0 and currentTag.xpath(f'./span[@class="mw-headline"]')[0].text in speechParts:

            speechPart = currentTag.xpath(f'./span[@class="mw-headline"]')[0].text
            output = f'{output}**{speechPart}**\n\n'

            if currentTag.xpath('following-sibling::*[1]')[0].tag == 'p':  # class="Latn headword", lang="en"
                underSpeechPart = currentTag.xpath('following-sibling::*[1]')[0].text_content()
                output = f'{output}{underSpeechPart}\n'

            lis = currentTag.xpath('./following-sibling::ol[1]/li')

            # extract the text from the tag and all its children
            for j, li in enumerate(lis):
                lis[j] = li.text_content().split('\n')[0].strip()

                # usage example if exists
                if len(li.xpath('./dl/dd')) > 0:
                    for usageRaw in li.xpath('./dl/dd'):  # alternative: li.xpath('.//div[@class="h-usage-example"]')
                        if usageRaw.text_content().split()[0] not in ['Synonym:', 'Synonyms:', 'Antonym:', 'Antonyms:']:
                            usage = usageRaw.text_content()
                            lis[j] = lis[j] + '\n' + f'*{usage}*'

                elif len(li.xpath('./ol/li/dl/dd')) > 0:
                    if li.xpath('./ol/li/dl/dd')[0].text_content().split()[0] not in ['Synonym:', 'Synonyms:', 'Antonym:', 'Antonyms:']:
                        usage = li.xpath('./ol/li/dl/dd')[0].text_content()
                        lis[j] = lis[j] + '\n' + f'*{usage}*'

            # remove empty entries
            lis = list(filter(None, lis))

            for j, li in enumerate(lis):
                if j < 5:
                    output = f'{output}{j + 1}) {li}\n\n'

    if output == '':
        if speechPart == 'All':
            output = 'Word or phrase not found'
        else:
            output = 'The word does not fit into the specified part of speech'

    return output



async def wiktionary(interaction: discord.Interaction, inpWord: str, speech_part: str = 'all'):
    output = generateOutput(inpWord, speech_part)
    finalString = ''
    for i in output:
        if i != inpWord:
            finalString += f'{i}\n'
    urlStr = inpWord.replace(' ', '_')
    file = discord.File('wiktionary_icon.png', filename="wiktionary_icon.png")
    embed = discord.Embed(type='rich', title=f'{inpWord}', url=f'https://en.wiktionary.org/wiki/{urlStr}', description=output, color=0xffa400)
    embed.set_author(name='test', icon_url='attachment://wiktionary_icon.png')
    await interaction.response.send_message(file=file, embed=embed)