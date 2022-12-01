def add_sp(x):
    return x[:-1] + ' sp' + x[-1]

with open('Lexicon.txt', 'r') as reader:
    lexicons = reader.readlines()

new_lexicons = [add_sp(x) for x in lexicons]

with open('new_lexicon.txt', 'w') as writer:
    for lexicon in new_lexicons:
        writer.write(lexicon)