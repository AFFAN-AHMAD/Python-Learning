def girrageLanguageTranslator(phrase):
    translatedPhrase = ""
    SmallVowels = ['a', 'e', 'i', 'o', 'u']
    largeVowels = ['A', 'E', 'I', 'O', 'U']
    # phrase = phrase.replace()
    for letters in phrase:
        if letters in SmallVowels:
            translatedPhrase += 'g'
        elif letters in largeVowels:
            translatedPhrase += 'G'
        else:
            translatedPhrase += letters
    return translatedPhrase
print(girrageLanguageTranslator('A book in the garden found in a wet state')
)