with open('output\monophones0', 'r') as reader:
    monophones = reader.readlines()

with open('config\mktri.hed', 'w') as writer:
    writer.write('CL output/triphones1\n')
    for monophone in monophones[:-1]:
        writer.write('TI T_' + monophone[:-1] + ' {(*-' + monophone[:-1] + '+*,' + monophone[:-1] + '+*,*-' + monophone[:-1] + ').transP}\n')