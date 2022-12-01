# import re

with open('output\phones0.mlf', 'r') as reader:
    transcripts = reader.readlines()

# reg0 = re.compile('[^a-zA-Z -]')
# reg1 = re.compile('[-]')
# for idx, transcript in enumerate(transcripts):
#     transcripts[idx] = reg0.sub('', transcript[17:-1])
#     transcripts[idx] = reg1.sub(' ', transcripts[idx])
#     transcripts[idx] = transcripts[idx].lower()

transcripts = transcripts[1:]

for idx, _ in enumerate(transcripts):
    if transcripts[idx][0] == '"':
        name_file = transcripts[idx][5:-2]
        if int(transcripts[idx][-9:-6]) in [7,9,14,17,25,33,34,35,39,57,58,61,62,63,65,73,79,80,94,103,107,123,129,136,143,150,151,157,159,165,169,177,180,183,217,230,235,241,250,253,259,265,267,285,290]:
            base_root = 'mfcc_test/'
        else:
            base_root = 'mfcc/'
        idx += 1
        with open(base_root + name_file, 'w') as writer:
            while(transcripts[idx] != '.\n'):
                writer.write(transcripts[idx])
                idx += 1

# for last_nim in ['093', '170', '178', '198', '211']:
#     for i in range(1, 300):
#         if i in [7,9,14,17,25,33,34,35,39,57,58,61,62,63,65,73,79,80,94,103,107,123,129,136,143,150,151,157,159,165,169,177,180,183,217,230,235,241,250,253,259,265,267,285,290]:
#             with open('mfcc_test/13519' + last_nim + '_' + str(i).zfill(3) + '.lab' , 'w') as writer:
#                 writer.write(transcripts[i - 1] + '\n')
#         else:
#             with open('mfcc/13519' + last_nim + '_' + str(i).zfill(3) + '.lab', 'w') as writer:
#                 writer.write(transcripts[i - 1] + '\n')