import MeCab
import sys

def katakana_to_hiragana(word_katakana: str) -> str:
    """Converts a string of Katakana characters to Hiragana."""
    hiragana = ""
    for character in word_katakana:
        if 'ァ' <= character <= 'ヶ':
            # Conversion to Hiragana by adjusting the Unicode value
            character_unicode_hiragana = ord(character) - 96
            character_hiragana = chr(character_unicode_hiragana)
        else:
            character_hiragana = character
        hiragana += character_hiragana
    return hiragana

def main():
    """Main function to read text, tokenize, convert to Hiragana, and print."""
    tagger = MeCab.Tagger()
    if len(sys.argv) > 1:
        text = sys.argv[1]
    else:
        text = input('Text with Kanji or Katakana:\n')

    parsed_text = tagger.parse(text)
    node = tagger.parseToNode(text)
    katakana_words = []

    while node:
        features = node.feature.split(',')
        katakana_pre = (features[6] if len(features) > 7 
                        else node.surface)
        katakana_words.append(katakana_pre)
        node = node.next

    hiragana_words = []
    for word in katakana_words:
        word_hiragana = katakana_to_hiragana(word)
        hiragana_words.append(word_hiragana)

    # Remove the last two elements which are not actual words
    hiragana_words = hiragana_words[:-2]
    
    hiragana_text = ''.join(hiragana_words)
    print(f'Text with Hiragana:\n{hiragana_text}')

if __name__ == "__main__":
    main()
