

import sys
import os


x = len(sys.argv)

if x > 1:
    if sys.argv[1] == 'taras':
        print("HElp Requestrd")
        print("usage of this projgram is python")
    print("Arguments entered :" + str(sys.argv[1:]))
else:
    print("Arguments enter")

os.system("dir")     # where we are
                     #  os.mkdir ("myddir")  create dir
sys.exit(2)          # os.system("dir > test.txt ) created text file
