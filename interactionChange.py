


def interactionChange():
    a = mdb.models['Model-1'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
        constraints=ON, connectors=ON, engineeringFeatures=ON)
    a = mdb.models['Model-1'].rootAssembly
    s1 = a.instances['Blank_Holder-1'].edges
    side2Edges1 = s1.getSequenceFromMask(mask=('[#1f ]', ), )
    region1=regionToolset.Region(side2Edges=side2Edges1)
    a = mdb.models['Model-1'].rootAssembly
    s1 = a.instances['Blank-1'].edges
    side1Edges1 = s1.getSequenceFromMask(mask=('[#1 ]', ), )
    region2=regionToolset.Region(side1Edges=side1Edges1)
    mdb.models['Model-1'].interactions['Blank_Holder'].setValues(main=region1, 
        secondary=region2, initialClearance=OMIT, adjustMethod=NONE, 
        sliding=FINITE, enforcement=SURFACE_TO_SURFACE, thickness=ON, 
        contactTracking=TWO_CONFIG, bondingSet=None)
    a = mdb.models['Model-1'].rootAssembly
    s1 = a.instances['Die-1'].edges
    side2Edges1 = s1.getSequenceFromMask(mask=('[#1f ]', ), )
    region1=regionToolset.Region(side2Edges=side2Edges1)
    a = mdb.models['Model-1'].rootAssembly
    s1 = a.instances['Blank-1'].edges
    side2Edges1 = s1.getSequenceFromMask(mask=('[#1 ]', ), )
    region2=regionToolset.Region(side2Edges=side2Edges1)
    mdb.models['Model-1'].interactions['Die_Blank'].setValues(main=region1, 
        secondary=region2, initialClearance=OMIT, adjustMethod=NONE, 
        sliding=FINITE, enforcement=SURFACE_TO_SURFACE, thickness=ON, 
        contactTracking=TWO_CONFIG, bondingSet=None)
    a = mdb.models['Model-1'].rootAssembly
    s1 = a.instances['Punch-1'].edges
    side2Edges1 = s1.getSequenceFromMask(mask=('[#7 ]', ), )
    region1=regionToolset.Region(side2Edges=side2Edges1)
    a = mdb.models['Model-1'].rootAssembly
    s1 = a.instances['Blank-1'].edges
    side1Edges1 = s1.getSequenceFromMask(mask=('[#1 ]', ), )
    region2=regionToolset.Region(side1Edges=side1Edges1)
    mdb.models['Model-1'].interactions['punch_Blank'].setValues(main=region1, 
        secondary=region2, initialClearance=OMIT, adjustMethod=NONE, 
        sliding=FINITE, enforcement=SURFACE_TO_SURFACE, thickness=ON, 
        contactTracking=TWO_CONFIG, bondingSet=None)


