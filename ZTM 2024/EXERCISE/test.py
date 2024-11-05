# from python_translator import Translator
#
# translator = Translator()
# result = translator.translate("My name is James", "french", "english")
#
# print(result)
from googletrans import Translator

# translator = Translator(
#     service_urls=[
#         "translate.google.com",
#         "translate.google.co.kr",
#     ]
# )
#
#
# translator = Translator()
# lang1 = translator.translate("안녕하세요.")
# # <Translated src=ko dest=en text=Good evening. pronunciation=Good evening.>
# lang2 = translator.translate("안녕하세요.", dest="ja")
# # <Translated src=ko dest=ja text=こんにちは。 pronunciation=Kon'nichiwa.>
# lang3 = translator.translate("veritas lux mea", src="la")
# # <Translated src=la dest=en text=The truth is my light pronunciation=The truth is my light>
# print(lang2)

#
# translator = Translator()
# print(translator.detect("이 문장은 한글로 쓰여졌습니다."))
