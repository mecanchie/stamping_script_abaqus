
def translate():
    a1 = mdb.models['Model-1'].rootAssembly
    e1 = a1.instances['Punch-1'].edges
    e2 = a1.instances['BlankHolder-1'].edges
    a1.EdgeToEdge(movableAxis=e1[2], fixedAxis=e2[1], flip=ON, clearance=0.0)
    a1 = mdb.models['Model-1'].rootAssembly
    e1 = a1.instances['BlankHolder-1'].edges
    e2 = a1.instances['Die-1'].edges
    a1.EdgeToEdge(movableAxis=e1[2], fixedAxis=e2[1], flip=OFF, clearance=0.0)
    a1 = mdb.models['Model-1'].rootAssembly
    a1.translate(instanceList=('Die-1', ), vector=(0.0, 1.2, 0.0))
    a1 = mdb.models['Model-1'].rootAssembly
    a1.translate(instanceList=('blank-1', ), vector=(0.0, 0.6, 0.0))


