#!/usr/bin/env python3

import unicodedata as ud
import sys

'''
outputs from beginning to end of unicode range in tsv format
argv:
    0: beginning of unicode range (e.g. 0x2600)
    1: ending of unicode range (e.g. 0x2700)
'''

#print('\t'.join(['code', 'name', 'category', 'symbol', 'keybinding',]))
start = int(sys.argv[1], 16)
end = int(sys.argv[2], 16)
for i in range(start, end + 1):
    print('\t'.join([
                'U+%X' % i,
                ud.name(chr(i)),
                ud.category(chr(i)),
                chr(i),
                ''
          ]))

