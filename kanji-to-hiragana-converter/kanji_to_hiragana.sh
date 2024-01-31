# Check if an argument was provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 'Text with Kanji or Katakana'"
    exit 1
fi

# Run the Python script with the provided argument and redirect output to file
python kanji_to_hiragana.py "$1" >> hiragana_text.txt

# Inform the user and display the content
echo "The text in hiragana has been written in hiragana_text.txt"
cat hiragana_text.txt
