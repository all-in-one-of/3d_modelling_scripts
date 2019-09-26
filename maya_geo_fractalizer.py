import maya.cmds as cmds
from random import uniform
from random import randint


def instance_at_point(object, pos, rescale, rotation, rand_scale, rand_rot):
    new_obj=cmds.instance(object, lf=True)
    cmds.select(new_obj)
    cmds.move(pos[0], pos[1], pos[2])
    
    cmds.rotate(rotation[0] + uniform(-rand_rot[0], rand_rot[0]), \
                rotation[1] + uniform(-rand_rot[1], rand_rot[1]), \
                rotation[2] + uniform(-rand_rot[2], rand_rot[2]))
                
    cmds.scale(rescale[0] + uniform(-rand_scale[0], rand_scale[0]), \
               rescale[1] + uniform(-rand_scale[1], rand_scale[1]), \
               rescale[2] + uniform(-rand_scale[2], rand_scale[2]), r=True)
    
    return new_obj

# recursively copy geometry onto its own faces, changing scale with every step
def recursive_instancer(object, depth, max_depth, scale_factor, mode, rotation, rand_scale, rand_rot, mode_switching):   
    if mode_switching == True:
        modes = ['centroid', 'vertex']
        mode = modes[random.randint(0, len(modes) - 1)]
        
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
                new_obj = instance_at_point(object, face_center, scale_factor, [i*depth for i in rotation], rand_scale, rand_rot)   
                recursive_instancer(new_obj[0], depth+1, max_depth, scale_factor, mode, rotation, rand_scale, rand_rot, mode_switching)
 
                
        elif mode == 'vertex':
            vertices = cmds.ls(cmds.polyListComponentConversion(toVertex=True), flatten=True)
            for v in vertices:
                new_obj = instance_at_point(object, cmds.pointPosition(v), scale_factor, [i*depth for i in rotation], rand_scale, rand_rot)
                recursive_instancer(new_obj[0], depth+1, max_depth, scale_factor, mode, rotation, rand_scale, rand_rot, mode_switching)
                    

# feed selected object into recursive function
init_object = cmds.ls(sl=True, long=True)

if init_object:
    recursive_instancer(object=init_object[0], \
    depth=0, \
    max_depth=3, \
    scale_factor=[0.5, 0.5, 0.5], \
    mode = 'centroid', \
    rotation=[0, 0, 0], \
    rand_rot = [0, 0, 0], \
    rand_scale = [0, 0.166, 0], \
    mode_switching = True)
    
else:
    print('Error: No initial object selected')
