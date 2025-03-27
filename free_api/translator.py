from translate import Translator

def translate_to_hindi(text):
    translator = Translator(to_lang="hi")  # Hindi language code is 'hi'
    translation = translator.translate(text)
    return translation

text = " rupa"
hindi_text = translate_to_hindi(text)
print(f"English: {text}")
print(f"Hindi: {hindi_text}")
