#!/usr/bin/python3

import sys

from src import save, restore

if __name__ == '__main__':
    if sys.argv.__len__() == 1:
        print('./run.py export - stores all data')
        print('./run.py import - restores all data')
    elif 'export' in sys.argv:
        ex = save.Export()
        ex.start()
    elif 'import' in sys.argv:
        im = restore.Import()
        im.start()
    else:
        sys.exit('unknown arg')
