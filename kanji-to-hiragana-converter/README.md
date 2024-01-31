# Kanji and Katakana to Hiragana Converter

## Description
The "Kanji and Katakana to Hiragana Converter" is a tool developed to assist students of the Japanese language in reading and understanding Japanese text. It automatically converts Kanji and Katakana to Hiragana, making the text easier to read while allowing learners to practice Hiragana.

## Motivation
As a Japanese language learner, the challenge of reading Japanese text in Hiragana was the main inspiration for this project. The objective was to create a tool that simplifies the reading process, allowing learners to focus on comprehension and fluency. Additionally, this project was an opportunity to delve into the technical aspects of bash scripts, file permissions, and the intricacies of Natural Language Processing (NLP).

## Features
- Convert Japanese text (including Kanji and Katakana) to Hiragana.
- Use MeCab, a robust morphological analyzer, to tokenize Japanese text.
- Simple command-line interface for easy use.

## Technologies Used
- **Language**: Python
- **NLP Tool**: MeCab
- **Others**: Bash for scripting

## File Structure
- `kanji_to_hiragana.py`: The main Python script for conversion.
- `kanji_to_hiragana.sh`: Bash script to run the Python script and handle input/output.
- `README.md`: Documentation and guide.
- `requirements.txt`: List the Python dependencies for the project.
- `hiragana_text.txt`: Output file where the converted text is saved.

## Set Up and Requirements
- Python 3.x
- MeCab
Ensure you have the above requirements installed. For MeCab installation, follow the [official documentation](https://pypi.org/project/mecab-python3/).
Also, make sure to give execution permissions to `kanji_to_hiragana.sh`:

```bash
chmod +x kanji_to_hiragana.sh
```

## How to Use
1. Clone the repository.
2. Navigate to the project directory.
3. Make sure you have MeCab installed on your system.
4. Run the script using the following command:
   ```bash
   ./kanji_to_hiragana.sh "Your Japanese text here"
   ```
