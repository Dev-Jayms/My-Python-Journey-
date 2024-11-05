"""Building a Translator App"""

# This code let you import the translate module.
from translate import Translator

"""# This code let you read from a user input.
text = input("Enter text: ")
lang = input("Which language would you like to translate to: ")
# This line of code let youtranslate from ENGLISH to any language.
translator = Translator(from_lang="english", to_lang=lang)
# translator = Translator(to_lang="ja")# This code set the default  from_lang to AUTODETECT.
# translator = Translator(from_lang="english", to_lang="ja") #This code let u translate from ENGLISH to JAPANESE
print(translator.translate(text))

"""

translator = Translator(to_lang="ja")
try:
    with open("translator.txt", mode="r", encoding="UTF-8") as file:
        lang = file.read()
        translation = translator.translate(lang)
        with open("japaneseTranslation.txt", mode="w", encoding="UTF-8") as file2:
            file2.write(translation)
except FileNotFoundError:
    print("This file doesn'africa exist.")
