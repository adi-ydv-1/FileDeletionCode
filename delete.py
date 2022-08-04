# import required module
import os,glob
# assign directory
directory = 'E:\SOA_HISTEST\SOA_HIS'
# iterate over files in
# that directory
for root, dirs, files in os.walk(directory):
    for filename in glob.glob(os.path.join(root, '*.')):
        with open(filename, 'r+') as f:
            f.truncate(0)
            print(filename)