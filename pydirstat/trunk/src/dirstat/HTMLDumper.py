#!/usr/bin/env python

from Dumper import FileDumper

class HTMLDumper( FileDumper ) :
    EXT='.html'

    def _start_dump(self) :
        header='''<html>
<head>
<title>Repertoire </title>
<script language='javascript'>
<!--
function fileinfo(elm,filename,filesize) {
 document.getElementById("filename").innerHTML=filename;
 document.getElementById("filesize").innerHTML=filesize;
 elm._oldcolor=elm.style.backgroundColor;
 elm.style.backgroundColor="#ff0000";
}
function fileout(elm) {
 document.getElementById("filename").innerHTML="";
 document.getElementById("filesize").innerHTML="";
 elm.style.backgroundColor=elm._oldcolor;
}
-->
</script>
<style type='text/css'>
<!--
.info {
  position:absolute;
  left:5;
  top:5;
  width:%(sizex)s;
  height:30;
  font-family:Verdana,Arial,Lucida,Sans-Serif;
  font-size:11px;
  font-weight:bold;
  background-color:#efe;
  border: solid 1px #8c8;
  padding : 2px;
  margin: 2px;
  white-space: nowrap;
  overflow: visible;
}
.rect {
  position:absolute;
  border-style:solid;
  border-width:1px;
  margin : solid 0 #fff;
}
.panel {
  position:absolute;
  left:5;
  top:40;
  width:%(sizex)s;
  height:%(sizey)s;
  background-color:none;
  border-color:#000;
  border-style:solid;
  border-width:1px;
  margin : solid 0 #fff;
}
#filename {
  padding-left: 10px;
  padding-right: 10px;
  padding-top: 2px;
  padding-bottom: 1px;
}
#filesize {
  padding-left: 10px;
  padding-right: 10px;
  padding-top: 1px;
  padding-bottom: 2px;
}
-->
</style>
</head>
<body>
<span class='info'>
<span id='filename'></span><br />
<span id='filesize'></span>
</span>
<span class='panel'>
'''
        size = self._tmv.visibleSize()
        self._file.write(header % {'sizex':size.x(),'sizey':size.y()})

    def _end_dump(self) :
        footer='''
</span>
</body>
</html>
'''
        size = self._tmv.visibleSize()
        self._file.write(footer % {'sizex':size.x(),'sizey':size.y()})

    def addrect(self,**kwargs) :
        kwargs['filename'] = kwargs['filename'].replace('\\','\\\\').replace('\'','&apos;').replace('\"','&quot;').replace('&','&amp;').encode('iso-8859-1','replace');
        kwargs['colorx'] = kwargs['color'].get_htmlcolor_extended(lambda x:int(x*0.6))
        self._file.write('''<span class='rect' onMouseOver='fileinfo(this,"%(filename)s","%(filesize)s")' onMouseOut='fileout(this)' style='left:%(x)dpx;top:%(y)dpx;width:%(width)dpx;height:%(height)dpx;background-color:%(color)s;border-color:%(colorx)s' /></span>\n''' % kwargs)

def test():
    HTMLDumper().dump()

if __name__ == '__main__' :
    test()
