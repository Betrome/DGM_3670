import maya.cmds as cmds
import sys
print sys.path
sys.path.append(r'C:\Users\spira\Documents\DGM_3670\Python')

def Toolbox():
    
    if cmds.window ('Toolbox', ex = True):
        cmds.deleteUI ('Toolbox')
        
    win = cmds.window (title = "Toolbox", iconName = "Toolbox", wh = (310, 130))
    
    cmds.columnLayout (adj = True)
    
    ctrlButton = cmds.button (label = "CTRL Maker", command = lambda x: ctrl())
    renameButton = cmds. button (label = "Renamer", command = lambda x: renamer())
    locButton = cmds.button (label = "Locator Creator", command = lambda x: loc())
    lightButton = cmds.button (label = "Light Setter", command = lambda x: light())
    randButton = cmds.button (label = "Randomizer", command = lambda x: random())
    
    cmds.showWindow (win)
    
def ctrl():
    import makeCTRL 
    makeCTRL.createFKControls()
    
def renamer():
    import Renamer
    Renamer.RenamerUI()
    
def loc():
    import makeLOC
    makeLOC.locWindow()
    
def light():
    import threePoint
    threePoint.threePoints()
    
def random():
    import randCity
    randCity.randWindow()
    
    
Toolbox()