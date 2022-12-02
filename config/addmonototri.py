with open('output/monophones0', 'r') as reader:
    monophones = reader.readlines()
    
with open('output/triphones1', 'r') as reader:
    triphones = reader.readlines()

for monophone in monophones:
    if monophone not in triphones:
        triphones.append(monophone)

with open('output/triphones1', 'w') as writer:
    for triphone in triphones:
        writer.write(triphone)