source_root = 'data/rekaman/'
target_root_1 = 'mfcc/'
target_root_2 = 'mfcc_test/'

nama = {'akeyla':'13519178', 
        'alfan': '13519211', 
        'marcel':'13519198', 
        'rajuh': '13519170', 
        'wisnu':'13519093'}

with open('config/targetList.txt', 'w') as writer:
    for key, value in nama.items():
        for i in range(1,300):
            if i in [7,9,14,17,25,33,34,35,39,57,58,61,62,63,65,73,79,80,94,103,107,123,129,136,143,150,151,157,159,165,169,177,180,183,217,230,235,241,250,253,259,265,267,285,290]:
                if (key == 'alfan' or key == 'marcel'):
                    writer.write(source_root + key + '/' + value + '-' + str(i).zfill(3) + '.wav' + ' ' + target_root_2 + value + '_' + str(i).zfill(3) + '.mfcc\n')    
                else:
                    writer.write(source_root + key + '/' + value + '_' + str(i).zfill(3) + '.wav' + ' ' + target_root_2 + value + '_' + str(i).zfill(3) + '.mfcc\n')
            else:
                if (key == 'alfan' or key == 'marcel'):
                    writer.write(source_root + key + '/' + value + '-' + str(i).zfill(3) + '.wav' + ' ' + target_root_1 + value + '_' + str(i).zfill(3) + '.mfcc\n')    
                else:
                    writer.write(source_root + key + '/' + value + '_' + str(i).zfill(3) + '.wav' + ' ' + target_root_1 + value + '_' + str(i).zfill(3) + '.mfcc\n')