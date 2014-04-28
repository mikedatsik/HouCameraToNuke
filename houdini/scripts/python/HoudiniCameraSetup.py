## Add expression for import camera animation to *.exr

import hou
def CameraToExr():
  sel = hou.selectedNodes()
  if (len(sel) == 0):
      if hou.ui.displayMessage("Select Rop Node and retry!", buttons=("OK",)) == 0:
	  print "Eror"
  else: 
      for i in range(0,len(sel)):
		expstr = '`pythonexprs("hou.node(hou.parm('+"'camera').eval()).worldTransform().asTuple()"+'")``pythonexprs("hou.parm(hou.parm('+"'camera').eval()+'/focal').eval()"+'")``")"``pythonexprs("hou.parm(hou.parm('+"'camera').eval()+'/aperture').eval()"+'")`'
		sel[i].parm('vm_image_comment').set(expstr)
