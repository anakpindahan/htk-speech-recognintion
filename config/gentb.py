with open('output/monophones0', 'r') as reader:
    monophones = reader.readlines()

with open('output/tb.txt', 'w') as writer:
    for i in range(5):
        for monophone in monophones:
            writer.write('TB 350 "ST_' + monophone[:-1] + '_2_" {("' + monophone[:-1] + '","*-' + monophone[:-1] + '+*","' + monophone[:-1] + '+*","*-' + monophone[:-1] + '").state[2]}\n')
        for monophone in monophones:
            writer.write('TB 350 "ST_' + monophone[:-1] + '_3_" {("' + monophone[:-1] + '","*-' + monophone[:-1] + '+*","' + monophone[:-1] + '+*","*-' + monophone[:-1] + '").state[3]}\n')
        for monophone in monophones:
            writer.write('TB 350 "ST_' + monophone[:-1] + '_4_" {("' + monophone[:-1] + '","*-' + monophone[:-1] + '+*","' + monophone[:-1] + '+*","*-' + monophone[:-1] + '").state[4]}\n')
        writer.write('\nTR 1\n\nAU "output/triphones1"\nCO "output/tiedlist"\n\nST "output/trees"\n\n')
         