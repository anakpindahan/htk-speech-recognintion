with open('data/wordlist/wordlist.txt', 'r') as reader:
    words = reader.readlines()

with open('grammar.bnf', 'w') as writer:
    for word in words:
        writer.write(word[:-1] + " | ")