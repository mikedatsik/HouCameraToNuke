## Create camera and animation form *.exr files
 
import math, nuke

## Get Camera Transformation Matrix from EXR

def getMetadataMatrix(meta_list):
    m = nuke.math.Matrix4()
    preMatrix = meta_list[1:-1].replace(")", ", ").split(",")
    try: 
        for i in range(0,16):
          m[i] = float(preMatrix[i])
    except:
          m.makeIdentity()
    return m

## Get Camera FocalLength from EXR

def getMetadataFocal(meta_list):
     preMatrix = meta_list[1:-1].replace(")", ", ").split(",")
     try: 
          m = float(preMatrix[16])
     except:
          m = 50
     return m
     
## Get Camera Aperture from EXR

def getMetadataAperture(meta_list):
     preMatrix = meta_list[1:-1].replace(")", ", ").split(",")
     try: 
          app = float(preMatrix[17])
     except:
          app = 41.4214
     return app

## Create Scene asset with camera and animation

def CamExp(): 
    selectedNodes = nuke.selectedNodes()
        # either nothing or too much is selected
    if (len(selectedNodes) != 1):
        nuke.message("Select Read node!")
        return "Fail"
    
    nodeType = selectedNodes[0].Class()
    
    if (nodeType != "Read"):
        nuke.message("Select Read node!")
        return "Fail"
    
    n=nuke.toNode(nuke.selectedNode().name())

    b1 = nuke.nodes.Camera()
    scan = nuke.nodes.ScanlineRender()
    scene = nuke.nodes.Scene()
    sph = nuke.nodes.Sphere()

    scan.connectInput(0,b1)
    scan.connectInput(1,scene)
    scene.connectInput(0, b1)
    scene.connectInput(1, sph)

    scanreadX = n.xpos()
    scanreadY = n.ypos()

    scan['xpos'].setValue(scanreadX+200)
    scan['ypos'].setValue(scanreadY)    
    
    #Get ScanlineRender position
    posX = scan.xpos()
    posY = scan.ypos()

    #position scene
    scene['xpos'].setValue(posX)
    scene['ypos'].setValue(posY-100)

    #position camera
    b1['xpos'].setValue(posX-100)
    b1['ypos'].setValue(posY-100)
    
    #position sphere
    sph['xpos'].setValue(posX)
    sph['ypos'].setValue(posY-200)


    k1 = b1['matrix']
    b1['useMatrix'].setValue(1)
    c1 = b1['focal']
    app1 = b1['haperture']
    k1.setAnimated()
    c1.setAnimated()
    app1.setAnimated()
    
    fistFF=nuke.Node.firstFrame(nuke.selectedNode())
    lastFF=nuke.Node.lastFrame(nuke.selectedNode())
    
    for i in range(fistFF, lastFF+1):

        camFocal = getMetadataFocal(n.metadata('exr/comment',i))
        c1.setValue(camFocal, time = i)
        
        camAperture = getMetadataAperture(n.metadata('exr/comment',i))
        app1.setValue(camAperture, time = i)
    
        camMatrix = getMetadataMatrix(n.metadata('exr/comment',i))
    
        transposedMatrix = nuke.math.Matrix4(camMatrix)
        transposedMatrix.transpose()
        resMatrix = transposedMatrix 
        
        k1.setValue(resMatrix[0], 0, time = i)
        k1.setValue(resMatrix[1], 1, time = i)
        k1.setValue(resMatrix[2], 2, time = i)
        k1.setValue(resMatrix[3], 3, time = i)
        k1.setValue(resMatrix[4], 4, time = i)
        k1.setValue(resMatrix[5], 5, time = i)
        k1.setValue(resMatrix[6], 6, time = i)
        k1.setValue(resMatrix[7], 7, time = i)
        k1.setValue(resMatrix[8], 8, time = i)
        k1.setValue(resMatrix[9], 9, time = i)
        k1.setValue(resMatrix[10], 10, time = i)
        k1.setValue(resMatrix[11], 11, time = i)
        k1.setValue(resMatrix[12], 12, time = i)
        k1.setValue(resMatrix[13], 13, time = i)
        k1.setValue(resMatrix[14], 14, time = i)
        k1.setValue(resMatrix[15], 15, time = i)
