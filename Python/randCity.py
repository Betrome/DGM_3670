import maya.cmds as cmds
from random import uniform as rand

def building (min, max, sXmin, sXmax, sYmin,sYmax, sZmin, sZmax, mXmin, mXmax, mYmin, mYmax, mZmin, mZmax, rXmin, rXmax, rYmin, rYmax, rZmin, rZmax):

    result = cmds.ls (sl=True)
    
    num = int(rand(min, max))
    
    for i in range (num):
        cmds.instance(result)
        cmds.scale(rand(sXmin, sXmax), rand(sYmin, sYmax), rand(sZmin, sZmax), result)
        cmds.move(rand(mXmin, mXmax), rand(mYmin, mYmax), rand(mZmin, mZmax), result)
        cmds.rotate(rand(rXmin, rXmax), rand(rYmin, rYmax), rand(rZmin, rZmax), result)    
        
        
building (2, 20, -1.0, 1.0, -1.0, 1.0, -1.0, 1.0, -5.0, 5.0, -5.0, 5.0, -5.0, 5.0, 0, 180, 0, 180, 0, 180)