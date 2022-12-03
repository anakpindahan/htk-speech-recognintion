import re

with open('data/transcript/13519093_Transcript.txt', 'r') as reader:
    transcripts = reader.readlines()

reg0 = re.compile('[^a-zA-Z -]')
reg1 = re.compile('[-]')
for idx, transcript in enumerate(transcripts):
    transcripts[idx] = reg0.sub('', transcript[17:-1])
    transcripts[idx] = reg1.sub(' ', transcripts[idx])
    transcripts[idx] = transcripts[idx].lower()

with open('output/testword.mlf', 'w') as writer:
    writer.write('#!MLF!#\n')
    for nim in ['093', '170', '178', '198', '211']:
        for idx, transcript in enumerate(transcripts):
            if (idx + 1) in [7,9,14,17,25,33,34,35,39,57,58,61,62,63,65,73,79,80,94,103,107,123,129,136,143,150,151,157,159,165,169,177,180,183,217,230,235,241,250,253,259,265,267,285,290]:
                writer.write('"*/13519' + nim + "_" + str((idx + 1)).zfill(3) + '.lab"\n')
                for word in transcript.split():
                    writer.write(word + '\n')
                writer.write('.' + '\n')
            