#!/usr/bin/env python

from FileInfo import FileTree
from Configuration import Configuration
from TreemapView import TreemapView
import os
from SimuQT import Size

class FileDumper( object ) :
    EXT=".dump"
    NEEDHANDLE=True
    def __init__(self, rootpath=None, outputfile=None, size=None, tree=None, configuration=None) :
        self._configuration = configuration
        if self._configuration == None :
            self._configuration = Configuration()

        if rootpath == None and self._configuration.get_value('path') != '' :
            rootpath = self._configuration.get_value('path')

        # Gruik Gruik : C:" -> C:\ Thanks Windows !
        if rootpath and (len(rootpath)==3) and (rootpath[2]) == '"' :
            rootpath = rootpath[0:2] + '\\'
        if (rootpath == None) and (tree==None) :
            rootpath = '.'
        if rootpath != None :
            if os.path.supports_unicode_filenames :
                rootpath = unicode(rootpath)
            else :
                rootpath = str(rootpath)
            tree = FileTree(rootpath)
            tree.scan()

        self._tree = tree
        filename = outputfile
        if filename == None :
            filename = self._configuration.get_value('outputfile')
        if filename == '' :
            if os.path.isdir(rootpath) :
                filename = os.path.join(rootpath,self._configuration.get_value('basename')+self.EXT)
            else :
                name = os.path.split(rootpath)[1]
                filename = name + '.' + self._configuration.get_value('basename') + self.EXT
        self._filename = filename
        self._size = size

    def dump(self,gsize=None) :
        if gsize != None :
            self._size = gsize
        if self._size == None :
            self._size = Size(self._configuration.get_value('width'),self._configuration.get_value('height'))
        self._tmv = TreemapView( self._tree, self._size, self._configuration )
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

