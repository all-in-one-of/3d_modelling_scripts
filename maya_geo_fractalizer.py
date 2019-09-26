import maya.cmds as cmds

def instance_at_point(object, pos, scale_factor):
    new_obj=cmds.instance(object, lf=True)
    cmds.select(new_obj)
    cmds.move(pos[0], pos[1], pos[2])
    cmds.scale(scale_factor, scale_factor, scale_factor, r=True)
    
    return new_obj

# recursively copy geometry onto its own faces, changing scale with every step
def recursive_instancer(object, depth, max_depth, scale_factor, mode):
    if depth < max_depth:        
        cmds.select(object)
        
        if mode == 'centroid':
            num_faces = cmds.polyEvaluate(f=True)
            
            for f in range(num_faces):           
                coords_sms = [0, 0, 0]
                face = cmds.select(object + '.f[%i]' % f)
                vertices = cmds.ls(cmds.polyListComponentConversion(toVertex=True), flatten=True)
                
                for v in vertices:
                    cmds.select(v)
                    pos = cmds.pointPosition()            
                    for i in range(len(coords_sms)):
                        coords_sms[i] += pos[i]   
                        
                face_center = [c/len(vertices) for c in coords_sms]
                new_obj = instance_at_point(object, face_center, scale_factor)   
                recursive_instancer(new_obj[0], depth+1, max_depth, scale_factor, mode=mode)
                
        elif mode == 'vertex':
            vertices = cmds.ls(cmds.polyListComponentConversion(toVertex=True), flatten=True)
            for v in vertices:
                new_obj = instance_at_point(object, cmds.pointPosition(v), scale_factor)
                recursive_instancer(new_obj[0], depth+1, max_depth, scale_factor, mode=mode)
                    

# feed selected object into recursive function
init_object = cmds.ls(sl=True, long=True)
if init_object:
    recursive_instancer(object=init_object[0], depth=0, max_depth=4, scale_factor=0.5, mode = 'vertex')
else:
    print('Error: No initial object selected')
