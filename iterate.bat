HCompV -C config\extractmfcc.conf -f 0.01 -m -S config\train.scp -M hmms\hmm.0 hmms\proto
py hmms\script.py
HERest -C config\extractmfcc.conf -I output\phones0.mlf -t 250.0 150.0 1000.0 -S config\train.scp -H hmms\hmm.0\macros -H hmms\hmm.0\hmmdefs -M hmms\hmm.1 output\monophones0
HERest -C config\extractmfcc.conf -I output\phones0.mlf -t 250.0 150.0 1000.0 -S config\train.scp -H hmms\hmm.1\macros -H hmms\hmm.1\hmmdefs -M hmms\hmm.2 output\monophones0
HERest -C config\extractmfcc.conf -I output\phones0.mlf -t 250.0 150.0 1000.0 -S config\train.scp -H hmms\hmm.2\macros -H hmms\hmm.2\hmmdefs -M hmms\hmm.3 output\monophones0
py hmms\script2.py
HHEd -H hmms\hmm.4\macros -H hmms\hmm.4\hmmdefs -M hmms\hmm.5 config\sil.hed output\monophones1
HERest -C config\extractmfcc.conf -I output\phones1.mlf -t 250.0 150.0 1000.0 -S config\train.scp -H hmms\hmm.5\macros -H hmms\hmm.5\hmmdefs -M hmms\hmm.6 output\monophones1
HERest -C config\extractmfcc.conf -I output\phones1.mlf -t 250.0 150.0 1000.0 -S config\train.scp -H hmms\hmm.6\macros -H hmms\hmm.6\hmmdefs -M hmms\hmm.7 output\monophones1
HVite -l * -o SWT -b SENT-END -C config\extractmfcc.conf -a -H hmms\hmm.7\macros -H hmms\hmm.7\hmmdefs -i output\aligned.mlf -m -t 250.0 -y lab -I output\words.mlf -S config\train.scp output\dict output\monophones1
HERest -C config\extractmfcc.conf -I output\aligned.mlf -t 250.0 150.0 1000.0 -S config\train.scp -H hmms\hmm.7\macros -H hmms\hmm.7\hmmdefs -M hmms\hmm.8 output\monophones1
HERest -C config\extractmfcc.conf -I output\aligned.mlf -t 250.0 150.0 1000.0 -S config\train.scp -H hmms\hmm.8\macros -H hmms\hmm.8\hmmdefs -M hmms\hmm.9 output\monophones1