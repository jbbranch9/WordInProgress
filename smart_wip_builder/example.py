from validate import validate_example_word as validate
from lexicon import lexicon as lex

def find_example_words(wip):
    examples = []
    for example_word in lex:
        if validate(wip, example_word):
            examples.append(example_word)

    return examples


