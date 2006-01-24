#!/usr/bin/env python

from dirstat.Configuration import Configuration
import sys

def main() :
    configuration = Configuration()
    for key in configuration :
        if configuration.need_configure(key) :
            doc = configuration.get_doc(key)
            strvalue = configuration.get_strvalue(key)
            print "%s ?[%s]" % (doc,strvalue)
            line = sys.stdin.readline().replace('\r','').replace('\n','')
            if line != '' :
                configuration.set_strvalue(key,line)
    configuration.save()

if __name__ == '__main__' :
    main()

