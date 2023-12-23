def post():    
    o3 = session.openOdb(name='E:/temp/Job-2.odb')
    a = mdb.models['Model-1'].rootAssembly
    session.mdbData.summary()
    session.Path(name='Path-2', type=NODE_LIST, expression=(('BLANK-1', (1, 201, 
        )), ))
    pth = session.paths['Path-2']
    session.XYDataFromPath(name='Mises', path=pth, includeIntersections=False, 
        projectOntoMesh=False, pathStyle=UNIFORM_SPACING, numIntervals=100, 
        projectionTolerance=0, shape=UNDEFORMED, labelType=TRUE_DISTANCE, 
        removeDuplicateXYPairs=True, includeAllElements=False)


