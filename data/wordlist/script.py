def get_first_word(x):
    return x.split()[0]

with open('new_lexicon.txt', 'r') as reader:
    lexicons = reader.readlines()

words = [get_first_word(lexicon) for lexicon in lexicons]

with open('wordlist.txt', 'w') as writer:
    for word in words:
        writer.write(word + "\n")