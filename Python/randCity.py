import maya.cmds as cmds
from random import uniform as rand

def building(*args):

    result = cmds.ls (sl=True)
    
    min = cmds.intSliderGrp ('numMin', q = 1, value = 1)
    max = cmds.intSliderGrp ('numMax', q = 1, value = 1)
    
    sXmin = cmds.floatSliderGrp ('scalexMin', q = 1, value = 1.0)
    sXmax = cmds.floatSliderGrp ('scalexMax', q = 1, value = 1.0)
    
    sYmin = cmds.floatSliderGrp ('scaleyMin', q = 1, value = 1.0)
    sYmax = cmds.floatSliderGrp ('scaleyMax', q = 1, value = 1.0)
    
    sZmin = cmds.floatSliderGrp ('scalezMin', q = 1, value = 1.0)
    sZmax = cmds.floatSliderGrp ('scalezMax', q = 1, value = 1.0)
    
    mXmin = cmds.floatSliderGrp ('movexMin', q = 1, value = 1.0)
    mXmax = cmds.floatSliderGrp ('movexMax', q = 1, value = 1.0)
    
    mYmin = cmds.floatSliderGrp ('moveyMin', q = 1, value = 1.0)
    mYmax = cmds.floatSliderGrp ('moveyMax', q = 1, value = 1.0)
    
    mZmin = cmds.floatSliderGrp ('movezMin', q = 1, value = 1.0)
    mZmax = cmds.floatSliderGrp ('movezMax', q = 1, value = 1.0)
    
    rXmin = cmds.floatSliderGrp ('rotatexMin', q = 1, value = 1.0)
    rXmax = cmds.floatSliderGrp ('rotatexMax', q = 1, value = 1.0)
    
    rYmin = cmds.floatSliderGrp ('rotateyMin', q = 1, value = 1.0)
    rYmax = cmds.floatSliderGrp ('rotateyMax', q = 1, value = 1.0)
    
    rZmin = cmds.floatSliderGrp ('rotatezMin', q = 1, value = 1.0)
    rZmax = cmds.floatSliderGrp ('rotatezMax', q = 1, value = 1.0)
        
    num = int(rand(min, max))
    
    for i in range (num):
        cmds.instance(result)
        cmds.scale(rand(sXmin, sXmax), rand(sYmin, sYmax), rand(sZmin, sZmax), result)
        cmds.move(rand(mXmin, mXmax), rand(mYmin, mYmax), rand(mZmin, mZmax), result)
        cmds.rotate(rand(rXmin, rXmax), rand(rYmin, rYmax), rand(rZmin, rZmax), result)    
        

def randWindow():        
    if cmds.window ('Randomizer', ex = True):
        cmds.deleteUI ('Randomizer')
        
    window = cmds.window (title = "Randomizer", iconName = "Randomize", wh = (310, 480))
    
    cmds.columnLayout (adj = True)
    
    cmds.intSliderGrp ('numMin', label = "Number Min", field = True, cw3 = (80, 40, 80), minValue = 0, maxValue = 50, fieldMinValue = 0, fieldMaxValue = 50, value = 1)
    cmds.intSliderGrp ('numMax', label = "Number Max", field = True, cw3 = (80, 40, 80), minValue = 0, maxValue = 50, fieldMinValue = 0, fieldMaxValue = 50, value = 5)
    
    cmds.floatSliderGrp ('scalexMin', label = "Scale x Min", field = True, cw3 = (80, 40, 150), minValue = 0.01, maxValue = 50.0, fieldMinValue = 0.1, fieldMaxValue = 50, value = 0.5)
    cmds.floatSliderGrp ('scalexMax', label = "Scale x Max", field = True, cw3 = (80, 40, 150), minValue = 0.01, maxValue = 50.0, fieldMinValue = 0.1, fieldMaxValue = 50, value = 2)
    
    cmds.floatSliderGrp ('scaleyMin', label = "Scale y Min", field = True, cw3 = (80, 40, 150), minValue = 0.01, maxValue = 50.0, fieldMinValue = 0.1, fieldMaxValue = 50, value = 0.5)
    cmds.floatSliderGrp ('scaleyMax', label = "Scale y Max", field = True, cw3 = (80, 40, 150), minValue = 0.01, maxValue = 50.0, fieldMinValue = 0.1, fieldMaxValue = 50, value = 2)
    
    cmds.floatSliderGrp ('scalezMin', label = "Scale z Min", field = True, cw3 = (80, 40, 150), minValue = 0.01, maxValue = 50.0, fieldMinValue = 0.1, fieldMaxValue = 50, value = 0.5)
    cmds.floatSliderGrp ('scalezMax', label = "Scale z Max", field = True, cw3 = (80, 40, 150), minValue = 0.01, maxValue = 50.0, fieldMinValue = 0.1, fieldMaxValue = 50, value = 2)
    
    cmds.floatSliderGrp ('movexMin', label = "Move x Min", field = True, cw3 = (80, 40, 150), minValue = -50.0, maxValue = 0.0, fieldMinValue = -50, fieldMaxValue = 0, value = -10)
    cmds.floatSliderGrp ('movexMax', label = "Move x Max", field = True, cw3 = (80, 40, 150), minValue = 0.00, maxValue = 50.0, fieldMinValue = 0, fieldMaxValue = 50, value = 10)
    
    cmds.floatSliderGrp ('moveyMin', label = "Move y Min", field = True, cw3 = (80, 40, 150), minValue = -50.0, maxValue = 0.0, fieldMinValue = -50, fieldMaxValue = 0, value = -10)
    cmds.floatSliderGrp ('moveyMax', label = "Move y Max", field = True, cw3 = (80, 40, 150), minValue = 0.00, maxValue = 50.0, fieldMinValue = 0, fieldMaxValue = 50, value = 10)
    
    cmds.floatSliderGrp ('movezMin', label = "Move z Min", field = True, cw3 = (80, 40, 150), minValue = -50.0, maxValue = 0.0, fieldMinValue = -50, fieldMaxValue = 0, value = -10)
    cmds.floatSliderGrp ('movezMax', label = "Move z Max", field = True, cw3 = (80, 40, 150), minValue = 0.00, maxValue = 50.0, fieldMinValue = 0, fieldMaxValue = 50, value = 10)
    
    cmds.floatSliderGrp ('rotatexMin', label = "Rotate x Min", field = True, cw3 = (80, 40, 150), minValue = -360.0, maxValue = 0.0, fieldMinValue = -360, fieldMaxValue = 0, value = -90)
    cmds.floatSliderGrp ('rotatexMax', label = "Rotate x Max", field = True, cw3 = (80, 40, 150), minValue = 0.00, maxValue = 360.0, fieldMinValue = 0, fieldMaxValue = 360, value = 90)
    
    cmds.floatSliderGrp ('rotateyMin', label = "Rotate y Min", field = True, cw3 = (80, 40, 150), minValue = -360.0, maxValue = 0.0, fieldMinValue = -360, fieldMaxValue = 0, value = -90)
    cmds.floatSliderGrp ('rotateyMax', label = "Rotate y Max", field = True, cw3 = (80, 40, 150), minValue = 0.00, maxValue = 360.0, fieldMinValue = 0, fieldMaxValue = 360, value = 90)
    
    cmds.floatSliderGrp ('rotatezMin', label = "Rotate z Min", field = True, cw3 = (80, 40, 150), minValue = -360.0, maxValue = 0.0, fieldMinValue = -360, fieldMaxValue = 0, value = -90)
    cmds.floatSliderGrp ('rotatezMax', label = "Rotate z Max", field = True, cw3 = (80, 40, 150), minValue = 0.00, maxValue = 360.0, fieldMinValue = 0, fieldMaxValue = 360, value = 90)
    
    randButton = cmds.button (label = "RANDOMIZE", command = building)
    
    originalSelection = cmds.ls (sl = True)
    
    cmds.select (originalSelection, r = True)
    
    cmds.showWindow (window)
    
randWindow()