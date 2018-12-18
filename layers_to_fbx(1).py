import rhinoscriptsyntax as rs

export_path = "C:\\Users\\Adhok\\Documents\\Max\\Rhino\\test\\"

project_layers = rs.LayerNames()
for i in project_layers:
    layer_objects = rs.ObjectsByLayer(i)
    rs.Command('-sellayer '+rs.LayerName(i))
    rs.Command('-mesh -enter')
    rs.Command('selnone')
    
    rs.Command('SelMesh')
    rs.Command('-join -enter')
    rs.Command('selnone')
    
    rs.Command('SelMesh')
    rs.Command('-export "%s%s.fbx" -enter -enter' % (export_path, rs.LayerName(i)))
    rs.Command('delete')
    rs.Command('selnone')

