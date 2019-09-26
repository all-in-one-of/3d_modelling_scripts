import maya.cmds as cmds
with open('C:\\Users\\Max\\PycharmProjects\\personal_projects\\cplusplus\\out.csv') as csv:
    csvstring = csv.read()

slices = csvstring.split('|')[:-1]

positions = []
for i in enumerate(slices):
    strokes = i[1].split('\n')[:-1]
    for j in enumerate(strokes):
        values = j[1].split(',')[:-1]       
        for k in enumerate(values):
            if k[1] == '1':
                positions.append((i[0],j[0],k[0]))
print(positions)
cmds.nParticle(p=positions)     
