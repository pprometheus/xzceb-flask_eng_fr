'''Translator Module'''
from deep_translator import MyMemoryTranslator
def english_to_french(_english_text):
    '''Translates from English to French'''
    frenchtext = MyMemoryTranslator (source="en",target="fr").translate('Good Morning')
    print(frenchtext)
    return frenchtext
def french_to_english(_fr_text):
    '''Translates from French to English'''
    englishtext=MyMemoryTranslator(source="fr",target='en').translate('Bonjour')
    print(englishtext)
    return englishtext
