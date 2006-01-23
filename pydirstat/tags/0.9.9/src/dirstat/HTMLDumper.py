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
 // document.getElementById("tooltip").innerHTML = "<b>Nom du fichier : </b>"+filename+"<br /><b>Taille du fichier : </b>"+filesize;
 // show();
 elm._oldcolor=elm.style.backgroundColor;
 elm.style.backgroundColor="#ff0000";
}
function fileout(elm) {
 document.getElementById("filename").innerHTML="";
 document.getElementById("filesize").innerHTML="";
 // document.getElementById("tooltip").innerHTML = "";
 // hide();
 elm.style.backgroundColor=elm._oldcolor;
}
tooltipOn = false;
function show(){
  if (true){
    document.getElementById("tooltip").xwidth = document.getElementById("tooltip").offsetWidth;
    document.getElementById("tooltip").xheight = document.getElementById("tooltip").offsetHeight;
    mainwidth = 0
    mainheight = 0
    if( typeof( window.innerWidth ) == 'number' ) {
      mainwidth = window.innerWidth;
      mainheight = window.innerHeight;
    } else if( document.documentElement && ( document.documentElement.clientWidth || document.documentElement.clientHeight ) ) {
      mainwidth = document.documentElement.clientWidth;
      mainheight = document.documentElement.clientHeight;
    } else if( document.body && ( document.body.clientWidth || document.body.clientHeight ) ) {
      mainwidth = document.body.clientWidth;
      mainheight = document.body.clientHeight;
    }
    document.getElementById("tooltip").mainwidth = mainwidth
    document.getElementById("tooltip").mainheight = mainheight
    // document.getElementById("tooltip").innerHTML = "";
    tooltipOn = true;
  }
}
function hide(){
  tooltipOn = false
}
function getPosition(p){
  x = (navigator.appName.substring(0,3) == "Net") ? p.pageX : event.x+document.body.scrollLeft;
  y = (navigator.appName.substring(0,3) == "Net") ? p.pageY : event.y+document.body.scrollTop;
  if(tooltipOn){
    xleft = x-120;
    xtop = y+25;
    xwidth = document.getElementById("tooltip").xwidth;
    xheight = document.getElementById("tooltip").xheight;

    mainwidth = document.getElementById("tooltip").mainwidth
    mainheight = document.getElementById("tooltip").mainheight

    if (xleft+xwidth>mainwidth) { xleft = mainwidth-xwidth; }
    if (xleft<0) { xleft = 0; }
    if (xtop+xheight>mainheight) { xtop = mainheight-xheight; }
    if (xtop<0) { xtop = 0; }

    document.getElementById("tooltip").style.top = xtop;
    document.getElementById("tooltip").style.left = xleft;
    document.getElementById("tooltip").style.visibility = "visible";
  }
  else{
    document.getElementById("tooltip").style.visibility = "hidden";
    document.getElementById("tooltip").style.top = 0;
    document.getElementById("tooltip").style.left = 0;
  }
}
// document.onmousemove = getPosition;
document.write('<div id="tooltip" class="tooltip"></div>');
-->
</script>
<style type='text/css'>
<!--
.tooltip {
  z-index:800;
  position:absolute;
  font-family:Verdana,Arial,Lucida,Sans-Serif;
  font-size:11px;
  border: solid 1px #808080;
  background-color:#E4E0D8;
  visibility:hidden;
  padding:1;
}
.info {
  position:absolute;
  left:5;
  top:5;
  width:810;
  height:30;
  font-family:Verdana,Arial,Lucida,Sans-Serif;
  font-size:11px;
  font-weight:bold;
  border: solid 1px #808080;
  background-color:#E4E0D8;
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
