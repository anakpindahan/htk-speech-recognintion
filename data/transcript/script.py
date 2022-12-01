import re

with open('data/transcript/13519093_Transcript.txt', 'r') as reader:
    transcripts = reader.readlines()

reg0 = re.compile('[^a-zA-Z -]')
reg1 = re.compile('[-]')
for idx, transcript in enumerate(transcripts):
    transcripts[idx] = reg0.sub('', transcript[17:-1])
    transcripts[idx] = reg1.sub(' ', transcripts[idx])
    transcripts[idx] = transcripts[idx].lower()

with open('output/words.mlf', 'w') as writer:
    writer.write('#!MLF!#\n')
    for nim in ['093', '170', '178', '198', '211']:
        for idx, transcript in enumerate(transcripts):
            writer.write('"*/13519' + nim + "_" + str((idx + 1)).zfill(3) + '.lab"\n')
            for word in transcript.split():
                writer.write(word + '\n')
            writer.write('.' + '\n')
            
        