
wip = "wip"
examples = []
for example_word in lex:
    if validate(wip, example_word):
        examples.append(example_word)

print(examples)