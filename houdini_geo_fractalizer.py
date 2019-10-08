import hou
from random import uniform
from random import randint

def translate_obj(obj, p):
    obj.parm('tx').set(p[0])
    obj.parm('ty').set(p[1])
    obj.parm('tz').set(p[2])
    
    
def scale_obj(obj, scale, rand_scale):
    obj.parm('sizex').set(obj.parm('sizex').eval() * (scale[0] + uniform(-rand_scale[0], rand_scale[0])))
    obj.parm('sizey').set(obj.parm('sizey').eval() * (scale[1] + uniform(-rand_scale[1], rand_scale[1])))
    obj.parm('sizez').set(obj.parm('sizez').eval() * (scale[2] + uniform(-rand_scale[2], rand_scale[2])))
    
  
def rotate_obj(obj, rand_rot, rot):
    obj.parm('rx').set(rot[0] + uniform(-rand_rot[0], rand_rot[0]))
    obj.parm('ry').set(rot[1] + uniform(-rand_rot[1], rand_rot[1]))
    obj.parm('rz').set(rot[2] + uniform(-rand_rot[2], rand_rot[2]))

    
def instance_at_point(obj, p, scale, rotate, rand_scale, rand_rot):
    sub_obj=n.copyItems([obj])[0]

    translate_obj(sub_obj, p.attribValue('P'))
    scale_obj(sub_obj, rand_scale, scale)
    rotate_obj(sub_obj, rand_rot, rotate)
    
    return sub_obj
    
    
def recursive_instancer(obj, iterations, scale, rotate):
    if iterations > 0:
        points = obj.geometry().points()
        
        for p in points:
        
            sub_obj = instance_at_point(obj, p, scale, rotate, rand_scale, rand_rot)
            recursive_instancer(sub_obj, iterations - 1, scale, rotate)
            

    
n = hou.node('obj').createNode('geo')
box = n.createNode('box')

scale_factor = (0.5, 0.5, 0.5)
rot_factor = (0, 0, 0)
rand_scale = (0.5, 0.5, 0.5)
rand_rot = (45, 0, 0)
    
recursive_instancer(box, 2, scale_factor, rot_factor) 
