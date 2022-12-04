def add_sp(x):
    return x[:-1] + ' sp' + x[-1]

with open('data/lexicon/dictwithoutsp', 'r') as reader:
    lexicons = reader.readlines()

new_lexicons = [add_sp(x) for x in lexicons]

with open('output/dict', 'w') as writer:
    for lexicon in new_lexicons:
        writer.write(lexicon)
    writer.write('SENT-START [] sil\nSENT-END [] sil\n')
    
with open('output/monophones1', 'r') as reader:
    monophones = reader.readlines()

with open('output/fulllist0', 'r') as reader:
    fulllists = reader.readlines()

with open('output/fulllist0', 'w') as writer:
    for fulllist in fulllists:
        writer.write(fulllist)
    for monophone in monophones:
        if monophone not in fulllists:
            writer.write(monophone)

with open('output/dict-tri', 'r') as reader:
    entries = reader.readlines()

with open('output/dict-tri', 'w') as writer:
    for entry in entries:
        writer.write(entry)
    writer.write('SENT-START sil\nSENT-END sil\n') 