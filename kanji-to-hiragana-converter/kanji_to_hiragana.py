import MeCab
import sys

def convert_katakana_to_hiragana(word_katakana: str) -> str:
    """Converts Katakana characters in a string to Hiragana.

    Args:
        word_katakana: A string containing Katakana characters.

    Returns:
        A string where Katakana characters have been converted to Hiragana.
    """
    hiragana = ""
    for character in word_katakana:
        # Convert Katakana characters to Hiragana if in the Katakana Unicode block.
        if 'ァ' <= character <= 'ヶ':
            unicode_hiragana = ord(character) - 96  # Convert to Hiragana Unicode.
            character_hiragana = chr(unicode_hiragana)
        else:
            character_hiragana = character  # Keep non-Katakana characters as they are.
        hiragana += character_hiragana
    return hiragana

def main():
    tagger = MeCab.Tagger()

    if len(sys.argv) > 1:
        text_input = sys.argv[1]
    else:
        text_input = input('Text with Kanji or Katakana:\n')

    parsed_text = tagger.parse(text_input)
    node = tagger.parseToNode(text_input)
    katakana_words = []  # List to store words converted from Katakana.

    while node:
        features = node.feature.split(',')
        # Use surface form if Katakana form is not available.
        katakana_form = features[6] if len(features) > 7 else node.surface
        katakana_words.append(katakana_form)
        node = node.next

    words_in_hiragana = []
    for word in katakana_words:
        word_hiragana = convert_katakana_to_hiragana(word)
        words_in_hiragana.append(word_hiragana)

    words_in_hiragana.pop()
    words_in_hiragana.remove('*')
    hiragana_text_output = ''.join(words_in_hiragana)

    print(f'Text with Hiragana:\n{hiragana_text_output}')

if __name__ == "__main__":
    main()
