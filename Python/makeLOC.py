import maya.cmds as cmds

def create(option):
    #Creates a locator at center of selection or pivot based on input.
    sels = cmds.ls(sl=True)

    # create locator at center of selections
    if option is 1:
        duple = cmds.duplicate(sels, rr=True)
        duple = cmds.polyUnite(duple, ch=True, mergeUVSets=True, centerPivot=True)[0]
        bbox = cmds.xform(duple, boundingBox=True, q=True)
        pivot = [(bbox[0] + bbox[3]) / 2, (bbox[1] + bbox[4]) / 2, (bbox[2] + bbox[5]) / 2]

        cmds.delete(duple, ch=True)
        cmds.delete(duple)

        locator = cmds.spaceLocator()[0]
        cmds.xform(locator, translation=pivot, worldSpace=True)

    # create locator at pivot point of each selection
    elif option is 2:
        for sel in sels:
            pivot = cmds.xform(sel, q=True, rp=True, ws=True)
            locator = cmds.spaceLocator()[0]
            cmds.xform(locator, translation=pivot, worldSpace=True)


if cmds.window('Locator Creator', exists=True):
    cmds.deleteUI('Locator Creator')

win = cmds.window(title = 'Locator Creator', wh = (300, 50))
mCol = cmds.columnLayout(adjustableColumn=True)
drop = cmds.optionMenu(label='Type')
cmds.menuItem(parent=drop, label='Bounding Box')
cmds.menuItem(parent=drop, label='Pivot Point')
cmds.button(label='Create Locator', c=lambda x: create(cmds.optionMenu(drop, q=True, select=True)))

cmds.showWindow(win)