#!/usr/bin/env python

from dirstat.MingDumper import MingDumper as Dumper
from dirstat.SimuQT import Size
import sys
import encodings

def main(path=None,gsize=None,outputfile=None) :
    if len(sys.argv)>=2 :
        path = sys.argv[1]
    if len(sys.argv)>=4 :
        gsize = Size(int(sys.argv[2]),int(sys.argv[3]))
    if len(sys.argv)>=5 :
        outputfile = sys.argv[4]

    Dumper(path,outputfile).dump(gsize)

if __name__ == '__main__' :
    main(u'.')

