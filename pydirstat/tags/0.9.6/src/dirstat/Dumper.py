#!/usr/bin/env python

from FileInfo import FileTree
from TreemapView import TreemapView
import os
from SimuQT import Size

class FileDumper( object ) :
    EXT=".dump"
    NEEDHANDLE=True
    def __init__(self, rootpath=None, outputfile=None, size=None, tree=None) :
        # Gruik Gruik : C:" -> C:\ Thanks Windows !
        if rootpath and (len(rootpath)==3) and (rootpath[2]) == '"' :
            rootpath = rootpath[0:2] + '\\'
        if (rootpath == None) and (tree==None) :
            rootpath = u'.'
        if rootpath != None :
            tree = FileTree(unicode(rootpath))
            tree.scan()

        self._tree=tree
        filename = outputfile
        if filename == None :
            if os.path.isdir(rootpath) :
                filename = os.path.join(rootpath,'dirstat'+self.EXT)
            else :
                name = os.path.split(rootpath)[1]
                filename = name + '.dirstat' + self.EXT
        self._filename = filename
        self._size = size
    def dump(self,gsize=None) :
        if gsize != None :
            self._size = gsize
        if self._size == None :
            self._size = Size(810,540)
        self._tmv = TreemapView( self._tree, None, self._size )
        size = self._tmv.visibleSize()

        if self.NEEDHANDLE :
            self._file = file(self._filename,'wt')

        self._start_dump()
        self._tmv.draw(self)
        self._end_dump()

        if self.NEEDHANDLE :
            self._file.close()

    def _start_dump(self) :
        '''You should override this method. Called once before starting dump.'''
        pass

    def _end_dump(self) :
        '''You should override this method. Called once after dumping all rectangle.'''
        pass

    def addrect(self,**kwargs) :
        '''You should override this method. It will be called on each rectangle. kwargs contains x,y,width,height,filename,filesize,color...'''
        pass

