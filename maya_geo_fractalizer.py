import maya.cmds as cmds

# recursively copy geometry onto its own faces, changing scale with every step
def copy2face(object, depth, max_depth, scale_factor):
    if depth < max_depth:        
        cmds.select(object)
        num_faces = cmds.polyEvaluate(f=True)
        
        # place instances of self on own faces
        for f in range(num_faces):           
            # calculate face centroid
            coords_sms = [0, 0, 0]
            face = cmds.select(object + '.f[%i]' % f)
            vertices = cmds.ls(cmds.polyListComponentConversion(toVertex=True), flatten=True)
            
            for v in vertices:
                cmds.select(v)
                pos = cmds.pointPosition()            
                for i in range(len(coords_sms)):
                    coords_sms[i] += pos[i]   
                    
            face_center = [c/len(vertices) for c in coords_sms]          
            
            new_obj=cmds.instance(object)
            cmds.select(new_obj)
            cmds.move(face_center[0], face_center[1], face_center[2])
            cmds.scale(scale_factor, scale_factor, scale_factor, r=True)

            copy2face(new_obj[0], depth+1, max_depth, scale_factor)

# feed selected object into recursive function
init_object = cmds.ls(sl=True, long=True)
copy2face(object=init_object[0], depth=0, max_depth=3, scale_factor=0.33)


    


        
     

