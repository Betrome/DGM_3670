import pymel.core as cmds

def makeCTRL():
    
    selection = cmds.ls (selection = True)
    
    size = 0
    for i in selection:
        size = i
    
    if (size == 0):
        cmds.error ("Please select one or more objects.")
        
    controlSize = cmds.floatSliderGrp (q = 1, v = controlSize)
    
    clr = cmds.colorIndexSliderGrp (q = 1, v = controlColor)
    clr -= 1
	
    controlSuff = cmds.textFieldGrp (q = 1, v = controlName)
    
    ctrlShape = cmds.intSliderGrp (q = 1, v = ctrlShape)
    
    for i in size:
        if (cmds.objExists (selection[0] + controlSuff) == 1):
            cmds.error ("Please enter a different suffix.")

    if (controlSuff == ""):
        cmds.error ("Please enter a suffix.")
	    
    for i in size:
        object1 = []
        objectShape1 = []	  

		#creates Circle controls
        if (ctrlShape == 0):
		    object1 = cmds.circle (nr = (1,0,0), ch = False)
		    objectShape1 = cmds.pickWalk (direction = 'down')
		    
		    cmds.setAttr (objectShape1[0] + ".overrideEnabled", 1)
		    
		    cmds.setAttr (objectShape1[0] + ".overrideColor", clr)		    
		
		#Creates Square controls  
        elif (ctrlShape == 1):
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
        elif (ctrlShape == 2):
		    
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


        cmds.rename (object1[0], (selection[i]+ controlSuff))
        cmds.select (selection[i] + controlSuff)
        cmds.scale ((controlSize *.25), (controlSize *.25), (controlSize *.25), r = True)
        cmds.makeIdentity (apply = True, t = True, r = True, s = True, n = 0)
        
        #creates an offset node
        cmds.group (em = True, n = (selection[i]+"_offset"))    
        tempConstraint = cmds.orientConstraint (selection[i], (selection[i]+"_offset"))
        cmds.delete (tempConstraint)
        tempConstraint = cmds.pointConstraint (selection[i], (selection[i]+"_offset"))
        cmds.delete (tempConstraint)
        
        cmds.parent ((selection[i] + controlSuff), (selection[i] + "_offset"))
        
        #parents all controls to the appropriate parent control
        if (i >= 1):
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
        
        
        
global def createFKControls():
    #Start Here
    if (cmds.window (Title = "makeFKWindow", exists = True))
	cmds.deleteUI makeFKWindow;

	string $text;

	$sel = `ls -sl`;	
    	if (`size ($sel)` >= 1)
    	
    	$text = $sel[0];
    
    	window -title "Create FK Controllers" makeFKWindow;
    	columnLayout -adj true makeFKColumn ;
    
    
    
    	floatSliderGrp 
    	-label "Control Size" 
    	-field true
    	-cw 1  80
    	-cw 2  40
    	-cw 3 150
       -minValue .01 
    	-maxValue 50.0
       -fieldMinValue .1 
    	-fieldMaxValue 50
       -value 2
    	controlSize;
    	
    	colorIndexSliderGrp 
    	-cw 1  80
    	-cw 2  40
    	-label "Control Color" 
    	-min 0 
    	-max 31 
    	-value 5
    	controlColor;
    	
    	intSliderGrp
    	-label "Control Shape" 
    	-field true    	
    	-cw 1 80
    	-cw 2 40
    	-cw 3 80
    	-minValue 0
    	-maxValue 2
       -fieldMinValue 0 
    	-fieldMaxValue 2
       -value 0
       ctrlShape;   	
    
        textFieldGrp
    	-cw 1  80
    	-cw 2 200
       -label "Control Suffix"
       -text  ("_CTRL")
    	controlName;

    	button
    	-label "EXECUTE"
    	-command "makeCTRL"
    	createFKButton;
    	
    	$originalSelection = `ls -sl`;
    
        
        select -r $originalSelection;
    
        
    	showWindow makeFKWindow;
    	window -edit -wh 310 110 makeFKWindow;
    	
    	if (`size($sel)` >= 1)
        textFieldGrp -e -text "_CTRL" -editable true controlName;
	
}

createFKControls

