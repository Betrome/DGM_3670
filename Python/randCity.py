import maya.cmds as cmds
from random import uniform as rand


result = cmds.ls (sl=True)

num = 20

for i in range (num):
    cmds.instance(result)
    cmds.scale(rand(5,-5), rand(5,-5), rand(5,-5), result)
    cmds.move(rand(10,-10), rand(10,-10), rand(10,-10), result)
    cmds.rotate(rand(0,360), rand(0,360), rand(0,360), result)    