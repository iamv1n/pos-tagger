# POS Tagger
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

## Description
POS Tagger is a Python-based tool that utilizes the Natural Language Toolkit (NLTK) library to perform Part-of-Speech (POS) tagging on sentences. POS tagging is an important step in natural language processing, as it assigns grammatical labels to words, enabling deeper linguistic analysis and understanding. The project leverages a decision tree classifier trained on a tagged corpus to accurately predict the POS tags for words in a given sentence. With its high accuracy, the POS Tagger can be used for various applications, including text analysis and information retrieval.

## Features

- Assigns POS tags to words in a sentence
- Accurate tagging using machine learning models

## Installation

1. Clone the repository:
```bash
git clone https://github.com/iamv1n/pos-tagger.git
```

2. Navigate to the project directory:
```bash
cd pos-tagger
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

4. To use the pos_tagger module globally Install the module
```bash
pip install -e pos_tagger
```
`This will install the package in editable mode (-e flag), allowing you to make changes to the package without reinstalling it.`

## Usage
Import the pos_tagger module and use the tag_sentence function to tag a sentence:
```python
from postagger import tag_sentence

sentence = "This is a sample sentence."
tags = tag_sentence(sentence)
print(tags)

```
The output will be a list of (word, tag) tuples representing the POS tags for each word in the sentence.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
