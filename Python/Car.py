import maya.cmds as cmds

cmds.polyCube (w=4.153696, h=1, d=2.414538, sx=1, sy=1, sz=1, ax=(0, 1, 0), cuv=4, ch=1, name="cube")
cmds.select ("cube.f[1]", r=True)
cmds.hilite ("cube.f[1]")
cmds.selectMode (component)
cmds.select ("cube.f[1]", r=True)
--> cmds.polyExtrudeFacet ("cube.f[1]", constructionHistory=1, keepFacesTogether=1, pvx=0, pvy=0.5, pvz=0, divisions=1, twist=0, taper=1, off=0, thickness=0, smoothingAngle=30,)
# Result: polyExtrudeFace1 
cmds.setAttr ("polyExtrudeFace1.localTranslate", type=double3, 0.593195, 0, 0.513042)
cmds.setAttr ("polyExtrudeFace1.localScale", type=double3, 0.49906, 0.657291, 1)
select -r pCube1.f[3] ;
move -r 0 0.389744 0 ;
polyTorus -r 1 -sr 0.5 -tw 0 -sx 20 -sy 20 -ax 0 1 0 -cuv 1 -ch 1;
// Result: pTorus1 polyTorus1 // 
rotate -r -os -fo 90 0 0 ;
move -r -1.243357 0.054872 1.398502 ;
scale -r 0.386195 0.386195 0.386195 ;
select -r pTorus1 ;
duplicate -rr;
// Result: pTorus2 //
move -r 2.292955 0 0 ;
select -r pTorus2 pTorus1 ;
duplicate -rr;
// Result: pTorus3 pTorus4 //
move -r 0 0 -2.796359 ;
select -r pCube1 ;
select -r pCube1 ;
rename "pCube1" "Base";
// Result: Base // 
select -r pTorus1 ;
rename "pTorus1" "Wheel_RR";
// Result: Wheel_RR // 
select -r pTorus2 ;
rename "pTorus2" "Wheel_RF";
// Result: Wheel_RF // 
select -r pTorus3 ;
rename "pTorus3" "Wheel_LF";
// Result: Wheel_LF // 
select -r pTorus4 ;
rename "pTorus4" "Wheel_LR";
// Result: Wheel_LR // 
select -r Wheel_LR ;
select -r Wheel_LR Wheel_LF Wheel_RF Wheel_RR ;
doGroup 0 1 1;
select -r group1 ;
select -add Base ;
parent;
// Result: group1 // 