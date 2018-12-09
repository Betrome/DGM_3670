import maya.cmds as cmds
import math
import sys

#Creates the three-point lighting system.
def threePoints():
	sels = cmds.ls(sl=True)

	if len(sels) == 0:
		sys.exit('Please select an object first')

	bBox = cmds.exactWorldBoundingBox(sels)

	key = cmds.shadingNode('areaLight', asLight=True)
	fill = cmds.shadingNode('areaLight', asLight=True)
	rim = cmds.shadingNode('areaLight', asLight=True)

	lights = [key, fill, rim]
	cmds.select(key)
	cmds.select(fill, add = True)
	cmds.select(rim, add = True)

	contain = cmds.group()

	v1 = [bBox[0], bBox[1], bBox[2]]
	v2 = [bBox[3], bBox[4], bBox[5]]
	v3 = [v2[0]- v1[0], v2[1]-v1[1], v2[2]-v1[2]]
	vLength = math.sqrt(v3[0]**2 + v3[1]**2 + v3[2]**2)
	rounded = math.ceil(vLength)
	factor = rounded/7.0
	

	cmds.xform(key, absolute = True, translation = [bBox[4] * 2.29 / factor, bBox[4] / factor * 0.75, -bBox[4] *1.71 / factor], rotation = [-24, 130, 0])
	cmds.xform(fill, absolute = True, translation = [bBox[4] * 1.71 / factor, bBox[4] / factor * 1.6, bBox[4] * 2.86 / factor], rotation = [-18, 35, 0])
	cmds.xform(rim, absolute = True, translation = [-bBox[4] *3.43 / factor, bBox[4] / factor * 0.5, bBox[4] * 0.57 / factor], rotation = [0, -77, 0], scale = [2, 2, 2])



	for light in lights:
		shape = cmds.listRelatives(light, shapes = True)
		cmds.setAttr(shape[0] + ".intensity", 20 * factor * factor/2)
		cmds.setAttr(shape[0] + ".decayRate", 2)

	key = cmds.rename(key, 'keyLight')
	fill = cmds.rename(fill, 'fillLight')
	rim = cmds.rename(rim, 'rimLight')
	contain = cmds.rename(contain, 'threePt_light_GRP')

threePoints()