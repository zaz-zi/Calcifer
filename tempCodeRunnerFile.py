import re
phrase = 'Привет!, сегодня такой 2346 замечательны      й день...;'
phraseLettersOnly = re.sub("[^a-zA-Z]+", "", phrase)
print(phraseLettersOnly)