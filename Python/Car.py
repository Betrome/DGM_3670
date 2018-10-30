import maya.cmds as cmds

cmds.polyCube (w=4.153696, h=1, d=2.414538, sx=1, sy=1, sz=1, ax=(0, 1, 0), cuv=4, ch=1, name="body")
cmds.select ("body.f[1]", r=True)
cmds.hilite ("body.f[1]")
cmds.selectMode (component=True)
cmds.select ("body.f[1]", r=True)
cmds.polyExtrudeFacet ("body.f[1]", constructionHistory=1, keepFacesTogether=1, pvx=0, pvy=0.5, pvz=0, divisions=1, twist=0, taper=1, off=0, thickness=0, smoothingAngle=30,)
# Result: polyExtrudeFace1 
cmds.setAttr ("polyExtrudeFace1.localTranslate", 0.593195, 0, 0.513042, type="double3")
cmds.setAttr ("polyExtrudeFace1.localScale", 0.49906, 0.657291, 1, type="double3")

cmds.polyTorus (sr=0.5, tw=0, sx=20, sy=20, ax=(0, 1, 0), cuv=1, ch=1, name="tire")
# Result: tire
cmds.rotate ("90deg", 0, 0, "tire")
cmds.move (1.243357, 0.054872, 1.398502)
cmds.scale (0.5, 0.5, 0.5)

cmds.duplicate ("tire")
# Result: tire1 
cmds.select ("tire1")
cmds.move (1.243357, 0.054872, -1.398502)
cmds.duplicate ("tire", "tire1")

# Result: tire2 & 3
cmds.select("tire2")
cmds.move (-1.144, 0, 1.398502)
cmds.select("tire3")
cmds.move (-1.144, 0, -1.398502)

cmds.group ("tire", "tire1", "tire2", "tire3", n="group1")
cmds.select ("group1")
cmds.select ("body", add=True)
cmds.parent ("group1", "body")
