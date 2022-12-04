HHEd -A -D -T 1 -H hmms\hmm.12\macros -H hmms\hmm.12\hmmdefs -M hmms\hmm.13 config\tree.hed output\triphones1
HERest -A -C config\extractmfcc.conf -I output\wintri.mlf  -t 250.0 150.0 3000.0 -S config\train.scp -H hmms\hmm.13\macros -H hmms\hmm.13\hmmdefs -M hmms\hmm.14 output\tiedlist0
HERest -A -C config\extractmfcc.conf -I output\wintri.mlf  -t 250.0 150.0 3000.0 -S config\train.scp -H hmms\hmm.14\macros -H hmms\hmm.14\hmmdefs -M hmms\hmm.15 output\tiedlist0
HVite -C config\extractmfcc.conf -H hmms\hmm.15\macros -H hmms\hmm.15\hmmdefs -S config\test.scp -l * -i output\recout.mlf -w data\grammar\grammar.slf -p 0.0 -s 5.0 output\dict-tri output\tiedlist0
HResults -I output\testword.mlf output\tiedlist0 output\recout.mlf