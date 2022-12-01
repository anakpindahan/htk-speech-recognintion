with open('hmms/hmm.0/proto', 'r') as reader:
    rows = reader.readlines()

with open('output/monophones1', 'r') as reader:
    monophones = reader.readlines()

with open('hmms/hmm.0/hmmdefs', 'w') as writer:
    for monophone in monophones:
        writer.write('~h "' + monophone[:-1] + '"\n')        
        for row in rows[4:]:
            writer.write(row)