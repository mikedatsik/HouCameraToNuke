HouCameraToNuke
===============

Expor camera from Houdini to EXR files and read them in Nuke


How to install:


HOUDINI:

####################################################################################################

1. Copy content from houdini folder to your $HOME/houdiniX.Y/  directory, or anywhere within $HOUDINI_SCRIPT_PATH

2. Add "Other" shelf in Houdini interface


NUKE:

####################################################################################################

1. Copy the nuke/ExportAnimationFromEXR folder (the whole folder, not just the files inside) to your .nuke/  directory, or anywhere within NUKE_PATH

2. Add the following line to your own menu.py

import ExportAnimationFromEXR
