import hou


def translate_obj(obj, p):
    obj.parm('tx').set(p[0])
    obj.parm('ty').set(p[1])
    obj.parm('tz').set(p[2])
    
    
def scale_obj(obj, scale):
    obj.parm('sizex').set(obj.parm('sizex').eval() * scale[0])
    obj.parm('sizey').set(obj.parm('sizey').eval() * scale[1])
    obj.parm('sizez').set(obj.parm('sizez').eval() * scale[2])
    
    
def rotate_obj(obj, rot):
    obj.parm('rx').set(rot[0])
    obj.parm('ry').set(rot[1])
    obj.parm('rz').set(rot[2])

    
def recursive_instancer(obj, iterations, scale, rotate):
    if iterations > 0:
        points = obj.geometry().points()
        
        for p in points:
            sub_obj = n.copyItems([obj])[0]
                      
            translate_obj(sub_obj, p.attribValue('P'))  
            scale_obj(sub_obj, scale)
            rotate_obj(sub_obj, rotate)
                     
            recursive_instancer(sub_obj, iterations - 1, scale, rotate)
            

    
n = hou.node('obj').createNode('geo')
box = n.createNode('box')

scale_factor = (0.5, 0.5, 0.5)
rot_factor = (0, 0, 0)
    
recursive_instancer(box, 4, scale_factor, rot_factor) 
