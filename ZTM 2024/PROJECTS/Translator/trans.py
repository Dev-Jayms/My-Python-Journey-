# This code let you import the translate module.
from translate import Translator

"""Building a Translator App"""


def translate_text():
    try:
        # Read user input
        text = input("Enter the text you want to translate: ")
        lang = input("Which language would you like to translate to: ").lower()

        # Create a translator object
        translator = Translator(from_lang="english", to_lang=lang)

        # Translate the text and print the result
        translated_text = translator.translate(text)
        # Store the translated text in languageTranslation.txt file
        with open("languageTranslation.txt", mode="a+", encoding="UTF-8") as file:
            file.write(
                f"\nThis is the translation of {text} in {lang}:\n"
                + translated_text
                + "\n"
            )
        print(translated_text)  # Print the translated text
    except FileNotFoundError:
        print("This file doesn'africa exist.")

    except TypeError:
        print("Please enter a language.")
    except UnicodeTranslateError:
        print("This language doesn'africa exist in oor server")
    except:
        raise ("The Lanuage you enter doesn'africa exist.")


# Call the function
translate_text()
