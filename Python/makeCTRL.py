import pymel.core as cmds

def makeCTRL():
    
    selection[] = cmds.ls (selection = true)
    
    size = 0
    for i in selections:
        size = i
    
    if (size == 0):
        cmds.error ("Please select one or more objects.")
        
    controlSize = cmds.floatSliderGrp (label = "controlSize", q = 1, v = 0.0)
    
	clr = cmds.colorIndexSliderGrp (label = "controlColor", q = 1, v = 0)
	clr -= 1
	
    controlSuff = cmds.textFieldGrp (label = "controlName", q = 1, v = 0)
    
    ctrlShape = cmds.intSliderGrp (lable = "ctrlShape", q = 1, v = 0)
    
    for i in size:
	    if (cmds.objExists (selection[0] + controlSuff) == 1)
	        error "Please enter a different suffix."
	    
	
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
		
		
		
		#creates Square controls
		elif (ctrlShape == 1):		    
		    object1 = cmds.nurbsSquare (c = (0, 0, 0), nr = (0, 1, 0), sl1 = 2, sl2 = 2, sps =  1, d = 3, ch = 1)
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
		    
		 #To Here   		    		 
		
		#creates Sphere controls
		else if ($ctrlShape == 2)
		{		    
		    $object1 =`circle -nr 1 0 0 -ch 0`;
		    $objectShape1 = `pickWalk -d down`;
		    $object2 =`circle -nr 0 1 0 -ch 0`;
		    $objectShape2 = `pickWalk -d down`;
		    $object3 =`circle -nr 0 0 1 -ch 0`;
		    $objectShape3 = `pickWalk -d down`;
		
		    setAttr ($objectShape1[0] + ".overrideEnabled") 1;
		    setAttr ($objectShape2[0] + ".overrideEnabled") 1;
		    setAttr ($objectShape3[0] + ".overrideEnabled") 1;
		
		    setAttr ($objectShape1[0] + ".overrideColor") $color ;
		    setAttr ($objectShape2[0] + ".overrideColor") $color ;
		    setAttr ($objectShape3[0] + ".overrideColor") $color ;
		
		    parent -shape -r $objectShape3 $objectShape2 $object1[0];
		    delete $object2[0];
		    delete $object3[0];		 		    
		}

		


		rename $object1[0] ($selection[$i]+ $controlSuff);
		select ($selection[$i]+ $controlSuff);
		scale -r ($controlSize *.25) ($controlSize *.25) ($controlSize *.25);
		makeIdentity -apply true -t 1 -r 1 -s 1 -n 0;
		
		//creates an offset node
		group -em -n ($selection[$i]+"_offset");
		$tempConstraint = `orientConstraint $selection[$i] ($selection[$i]+"_offset")`;
		delete $tempConstraint;
		$tempConstraint = `pointConstraint $selection[$i] ($selection[$i]+"_offset")`;
		delete $tempConstraint;

		parent ($selection[$i]+ $controlSuff) ($selection[$i]+"_offset");
		
		//parents all controls to the appropriate parent control
		if ($i>=1)
			parent ($selection[$i]+"_offset")  ($selection[$i-1]+$controlSuff);
		
		//sets their attributes to zero
		setAttr ($selection[$i]+ $controlSuff+".tx") 0;
		setAttr ($selection[$i]+ $controlSuff+".ty") 0;
		setAttr ($selection[$i]+ $controlSuff+".tz") 0;
		
		setAttr ($selection[$i]+ $controlSuff+".rx") 0;
		setAttr ($selection[$i]+ $controlSuff+".ry") 0;
		setAttr ($selection[$i]+ $controlSuff+".rz") 0;
		
		//connects FK controls directly to joint rotations
		parentConstraint -mo ($selection[$i]+ $controlSuff) ($selection[$i])  ;

	        
	        
	        