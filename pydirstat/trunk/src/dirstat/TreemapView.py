#!/usr/bin/env python

DefaultMinTileSize          = 3
UpdateMinSize               = 2

from SimuQT import Point, Rect, Color, Canvas
import os
from TreemapTile import TreemapTile

class TreemapView( object ):
    """This class is the main class of pydirstat that make the drawing. It is directly inspired from KTreemapView (from KDirStat).
       This class build the tree of files and work with the dumper/drawer to draw the tree."""
    def __init__( self, tree, initialSize, configuration ):
        """Constructor"""
        self._tree = tree
        self._rootTile = None
        self._selectedTile = None
        self._selectionRect = None
        self._tilestodraw = []
        # Not in KDirStat
        self._initialSize = initialSize
        self._configuration = configuration

        self.readConfig()

        # self.resize( initialSize )

        if tree and tree.root() :
            if not self._rootTile :
                self.rebuildTreemap( tree.root() )

    def selectedTile(self)  : return self._selectedTile
    def rootTile(self)      : return self._rootTile
    def tree(self)          : return self._tree
    def minTileSize(self)   : return self._minTileSize

    def readConfig( self ) :

        self._minTileSize   = DefaultMinTileSize

    def canvas( self ) :
        """Return a new simulated Qt Canvas."""
        return Canvas()

    def tileAt( self, pos ) :
        """Find the tile at a certain position. Anyway, need to implement Canvas.collisions first. Not used. DO NOT USE."""
        tile = None

        for canvasitem in self.canvas().collisions( pos ) :
            if canvasitem :
                return canvasitem

        return None

    def rebuildTreemap( self, newRoot, newSize=None ):
        """Build/Rebuild the tree."""
        if not newSize :
            newSize = self.visibleSize()

        self._selectedTile  = None;
        self._selectionRect = None;
        self._rootTile      = None;

        self.canvas().resize( newSize.width(), newSize.height() )

        if newSize.width() >= UpdateMinSize and newSize.height() >= UpdateMinSize  :
            if newRoot :
                self._rootTile = TreemapTile(
                    self,       # parentView
                    None,       # parentTile
                    newRoot,    # fileinfo
                    Rect( point=Point(0, 0), size=newSize ),
                    'Auto' )

    def visibleSize( self ) :
        """Access to the size of the tree"""
        return self._initialSize

    def tileColor( self, file ) :
        """Find the Color of a file."""
        # [PyInfo] : file is a FileInfo

        tabext = self._configuration.get_section('type:extension')
        tablowerext = self._configuration.get_section('type:extensionlower')
        contain = self._configuration.get_section('type:contain')
        exactmatch = self._configuration.get_section('type:exactmatch')

        colormatch = {}
        colorconfig = self._configuration.get_section('color')
        for key in colorconfig :
            colormatch[key] = Color(colorconfig[key])

        defaultColor = colormatch.get('_',Color('purple'))

        if file :
            if file.isFile() :
                filename = file.name()
                idx = -1
                idx=filename.find(".",idx+1)
                while idx != -1 :
                    ext = filename[idx+1:]

                    if tabext.has_key(ext) : return colormatch.get(tabext[ext],defaultColor)
                    if tablowerext.has_key(ext.lower()) : return colormatch.get(tablowerext[ext.lower()],defaultColor)
                    idx=filename.find(".",idx+1)

                for key in contain.keys() :
                    if filename.find(key) != -1 : return colormatch.get(contain[key],defaultColor)

                for key in exactmatch.keys() :
                    if filename == key : return colormatch.get(exactmatch[key],defaultColor)

                # if ( ( file->mode() & S_IXUSR  ) == S_IXUSR )   return Qt::magenta;
                # if ??*isexec*?? : return colormatch.get('exec',defaultColor)

            else :
                return colormatch.get('dir',defaultColor)

        return colormatch.get('file',defaultColor)

    def draw(self,painter):
        """Draw the tree in a painter/dumper."""
        for tile in self._tilestodraw :
            tile.drawShape(painter)

    def addTileToDraw(self,tile) :
        """Add a new TreemapTile to the View"""
        self._tilestodraw.append(tile)

if __name__ == '__main__' :
    pass
