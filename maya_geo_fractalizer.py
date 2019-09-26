import maya.cmds as cmds

def copy2face(object, depth, max_depth, scale_factor):
    if depth < max_depth:
        
        cmds.select(object)
        
        face_centroids = []
        num_faces = cmds.polyEvaluate(f=True)
        
        for f in range(num_faces):
            face = cmds.select(object + '.f[%i]' % f)
            vertices = cmds.ls(cmds.polyListComponentConversion(toVertex=True), flatten=True)
        
            coords_sms = [0, 0, 0]
            for v in vertices:
                cmds.select(v)
                pos = cmds.pointPosition()
            
                for i in range(len(coords_sms)):
                    coords_sms[i] += pos[i]
        
            face_center = [c/len(vertices) for c in coords_sms]          
            
            new_obj=cmds.instance(object)
            cmds.select(new_obj)
            cmds.move(face_center[0],face_center[1],face_center[2])
            cmds.scale(scale_factor,scale_factor,scale_factor,r=True)

            copy2face(new_obj[0], depth+1, max_depth, scale_factor)


init_object = cmds.polyPlatonicSolid( r=2, l=2, st=0)
copy2face(object=init_object[0], depth=0, max_depth=3, scale_factor=0.33)


    


        
     

