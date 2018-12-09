import pymel.core as cmds


def makeCTRL(*args):
    
    selection = cmds.ls (selection = True)
    
    size = len(selection)
    
    if (size == 0):
        cmds.error ("Please select one or more objects.")
        
    ctrlSize = cmds.floatSliderGrp ('controlSize', q = 1, value = 1.0)
    
    clr = cmds.colorIndexSliderGrp ('controlColor', q = 1, value = 1)
    clr -= 1
	
    controlSuff = cmds.textFieldGrp ('controlName', q = 1, text = 1)
    
    shape = cmds.intSliderGrp ('ctrlShape', q = 1, value = 1)


    if controlSuff == "":
        cmds.error ("Please enter a suffix.")
	    
    i = 0
    while i < size:
        object1 = []
        objectShape1 = []	  

		#creates Circle controls
        if shape == 0:
		    object1 = cmds.circle (nr = (1,0,0), ch = False)
		    objectShape1 = cmds.pickWalk (direction = 'down')
		    
		    cmds.setAttr (objectShape1[0] + ".overrideEnabled", 1)
		    
		    cmds.setAttr (objectShape1[0] + ".overrideColor", clr)		    
		
		#Creates Square controls  
        elif shape == 1:
            object1 = cmds.nurbsSquare (c = (0, 0, 0), nr = (0, 1, 0), sl1 = 2, sl2 = 2, sps = 1, d = 3, ch = True)
            objectShape1 = cmds.pickWalk (d = 'down')
            objectShape2 = cmds.pickWalk (d = 'right')
            objectShape3 = cmds.pickWalk (d = 'right')
            objectShape4 = cmds.pickWalk (d = 'right')
		    
            cmds.setAttr (objectShape1[0] + ".overrideEnabled", 1)
            cmds.setAttr (objectShape2[0] + ".overrideEnabled", 1)
            cmds.setAttr (objectShape3[0] + ".overrideEnabled", 1)
            cmds.setAttr (objectShape4[0] + ".overrideEnabled", 1)
            cmds.setAttr (objectShape1[0] + ".overrideColor", clr)
            cmds.setAttr (objectShape2[0] + ".overrideColor", clr)
            cmds.setAttr (objectShape3[0] + ".overrideColor", clr)
            cmds.setAttr (objectShape4[0] + ".overrideColor", clr)
		       		    		 
		
		#creates Sphere controls
        elif shape == 2:
		    
            object1 = cmds.circle (nr = (1, 0, 0), ch = 0)
            objectShape1 = cmds.pickWalk (d = 'down')
            object2 = cmds.circle (nr = (0, 1, 0), ch = 0)
            objectShape2 = cmds.pickWalk (d = 'down')
            object3 = cmds.circle (nr = (0, 0, 1), ch = 0)
            objectShape3 = cmds.pickWalk (d = 'down')
            
            cmds.setAttr (objectShape1[0] + ".overrideEnabled", 1)
            cmds.setAttr (objectShape2[0] + ".overrideEnabled", 1)
            cmds.setAttr (objectShape3[0] + ".overrideEnabled", 1)
            
            cmds.setAttr (objectShape1[0] + ".overrideColor", clr)
            cmds.setAttr (objectShape2[0] + ".overrideColor", clr)
            cmds.setAttr (objectShape3[0] + ".overrideColor", clr)
            
            cmds.parent (objectShape3, objectShape2, object1[0], shape = True, r = True)
            cmds.delete (object2[0])
            cmds.delete (object3[0])    
        
        cmds.rename (object1[0], (selection[i] + controlSuff))
        cmds.select (selection[i] + controlSuff)
        cmds.scale ((ctrlSize *.25), (ctrlSize *.25), (ctrlSize *.25), r = True)
        cmds.makeIdentity (apply = True, t = True, r = True, s = True, n = 0)
        
        #creates an offset node
        cmds.group (em = True, n = (selection[i]+"_offset"))    
        tempConstraint = cmds.orientConstraint (selection[i], (selection[i]+"_offset"))
        cmds.delete (tempConstraint)
        tempConstraint = cmds.pointConstraint (selection[i], (selection[i]+"_offset"))
        cmds.delete (tempConstraint)
        
        cmds.parent ((selection[i] + controlSuff), (selection[i] + "_offset"))
        
        #parents all controls to the appropriate parent control
        if i >= 1:
            cmds.parent ((selection[i]+"_offset"),  (selection[i-1] + controlSuff))
            
        #sets their attributes to zero
        cmds.setAttr ((selection[i]+ controlSuff+".tx"), 0)
        cmds.setAttr ((selection[i]+ controlSuff+".ty"), 0)
        cmds.setAttr ((selection[i]+ controlSuff+".tz"), 0)
        
        cmds.setAttr ((selection[i]+ controlSuff+".rx"), 0)
        cmds.setAttr ((selection[i]+ controlSuff+".ry"), 0)
        cmds.setAttr ((selection[i]+ controlSuff+".rz"), 0)
        
        #connects FK controls directly to joint rotations
        cmds.parentConstraint ((selection[i]+ controlSuff), selection[i], mo = True)
        i += 1


def createFKControls():
    if cmds.window ('Create_FK_Controllers', ex = True):
        cmds.deleteUI ('Create_FK_Controllers')
    
    text = ""
    sel = cmds.ls (sl = True)
    
    size = 0
    for x in sel:
        size = x
        
    if size >= 1:
        text = sel[0]
        
    window = cmds.window (title = "Create_FK_Controllers", iconName = "Ctrl maker", wh = (310, 110))
    
    cmds.columnLayout (adj = True)
    
    cmds.floatSliderGrp ('controlSize', label = "Control Size", field = True, cw3 = (80, 40, 150), minValue = 0.01, maxValue = 50.0, fieldMinValue = 0.1, fieldMaxValue = 50, value = 2)
    
    cmds.colorIndexSliderGrp ('controlColor',label = "Control Color", cw3 = (80, 40, 150), min = 0, max = 31, value = 5)
    
    cmds.intSliderGrp ('ctrlShape', label = "Control Shape", field = True, cw3 = (80, 40, 80), minValue = 0, maxValue = 2, fieldMinValue = 0, fieldMaxValue = 2, value = 0)
    
    cmds.textFieldGrp ('controlName', label = "Control Suffix", text = "_CTRL", cw2 = (80, 200))
    
    cz = cmds.floatSliderGrp ('controlSize', q = 1, value = 1.0)
    
    createFKButton = cmds.button (label = "EXECUTE", command = makeCTRL)
    
    originalSelection = cmds.ls (sl = True)
    
    cmds.select (originalSelection, r = True)
    
    cmds.showWindow (window)
    
    controlName = cmds.textFieldGrp (text = "_CTRL", editable = True)
    
    
createFKControls()