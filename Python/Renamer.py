import maya.cmds as cmds
# import maya.mel as mel

def Rename_Main(*args):
    
    selected_objects = cmds.ls(selection=True)
    
    # specify new name here
    newname = cmds.textFieldGrp('name', q=1, text=1)
    
    for number, object in enumerate(selected_objects):
        cmds.rename(object, ('%s%02d' % (newname, number)))
    
    
def RenamerUI():
    if cmds.window ('Rename_toolWindow', ex=True): 
         cmds.deleteUI ('Rename_toolWindow')
    
    window = cmds.window( title="Rename_toolWindow", iconName='Renamer', widthHeight=(400, 55) )
    cmds.columnLayout( adjustableColumn=True )
    cmds.textFieldGrp('name', label='Rename:', text='Name')
    cmds.button( label='Execute', command=Rename_Main )
    cmds.setParent( '..' )
    cmds.showWindow( window )
    
RenamerUI()