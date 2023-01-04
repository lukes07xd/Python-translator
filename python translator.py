from googletrans import Translator

def translate_text(text, target_language):
  translator = Translator()
  translation = translator.translate(text, dest=target_language)
  return translation.text

text = input("Enter the text to be translated: ")

print("Afrikaans: af\nAlbanian: sq\nAmharic: am\nArabic: ar\nArmenian: hy\nAzerbaijani: az\nBasque: eu\nBelarusian: be\nBengali: bn\nBosnian: bs\nBulgarian: bg\nCatalan: ca\nCebuano: ceb\nChichewa: ny\nChinese (Simplified): zh-CN\nChinese (Traditional): zh-TW\nCorsican: co\nCroatian: hr\nCzech: cs\nDanish: da\nDutch: nl\nEnglish: en\nEsperanto: eo\nEstonian: et\nFilipino: fil\nFinnish: fi\nFrench: fr\nFrisian: fy\nGalician: gl\nGeorgian: ka\nGerma: de\nGreek: el\nGujarati: gu\nHaitian Creole: ht\nHausa: ha\nHawaiian: haw\nHebrew: he\nHindi: hi\nHmong: hmn\nHungarian: hu\nIcelandic: is\nIgbo: ig\nIndonesian: id\nIrish: ga\nItalian: it\nJapanese: ja\nJavanese: jv\nKannada: kn\nKazakh: kk\nKhmer: km\nKorean: ko\nKurdish: ku\nKyrgyz: ky\nLao: lo\nLatin: la\nLatvian: lv\nLithuanian: lt\nLuxembourgish: lb\nMacedonian: mk\nMalagasy: mg\nMalay: ms\nMalayalam: ml\nMaltese: mt\nMaori: mi\nMarathi: mr\nMongolian: mn\nMyanmar (Burmese): my\nNepali: ne\nNorwegian: no\nPashto: ps\nPersian: fa\nPolish: pl\nPortuguese: pt\nPunjabi: pa\nRomanian: ro\nRussian: ru\nSamoan: sm\nScots Gaelic: gd\nSerbian	sr")

target_language = input("Enter the target language code: ")

translated_text = translate_text(text, target_language)
print(translated_text)