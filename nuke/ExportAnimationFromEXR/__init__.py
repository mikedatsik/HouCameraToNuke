from ExportAnimationFromEXR import *
import nuke
try:
	toolbar = nuke.toolbar("Nodes")
	m = toolbar.addMenu("System")
	m.addCommand("Create Camera form EXR", "ExportAnimationFromEXR.CamExp()", "h")
except:
    pass