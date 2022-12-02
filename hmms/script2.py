with open('hmms\hmm.3\macros', 'r') as reader:
    rows = reader.readlines() 

with open('hmms\hmm.4\macros', 'w') as writer:
    for row in rows:
        writer.write(row)
        
with open('hmms\hmm.3\hmmdefs', 'r') as reader:
    rows = reader.readlines()

with open('hmms\hmm.4\hmmdefs', 'w') as writer:
    for row in rows:
        writer.write(row)
    writer.write('~h "sp"\n')
    writer.write('<BEGINHMM>\n')
    writer.write('<NUMSTATES> 3\n')
    writer.write('<STATE> 2\n')
    for row in rows[-18:-14]:
        writer.write(row)
    writer.write('<TRANSP> 3\n')
    writer.write(' 0.0 1.0 0.0\n')
    writer.write(' 0.0 0.9 0.1\n')
    writer.write(' 0.0 0.0 0.0\n')
    writer.write('<ENDHMM>\n')    