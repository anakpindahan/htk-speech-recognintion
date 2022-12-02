HLEd -n output\triphones1 -l * -i output\wintri.mlf config\mktri.led output\aligned.mlf
py config\maketrihed.py
HHEd -B -H hmms\hmm.9\macros -H hmms\hmm.9\hmmdefs -M hmms\hmm.10 config\mktri.hed output\monophones1
HERest -B -C config\wav_to_mfcc.conf -I output\wintri.mlf -t 250.0 150.0 1000.0 -s log\stats -S config\train.scp -H hmms\hmm.10\macros -H hmms\hmm.10\hmmdefs -M hmms\hmm.11 output\triphones1