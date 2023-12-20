


def Section():
    mdb.models['Model-1'].RectangularProfile(name='Profile-1', a=300.0, b=0.8)
    mdb.models['Model-1'].BeamSection(name='Section-1', 
        integration=DURING_ANALYSIS, poissonRatio=0.0, profile='Profile-1', 
        material='Material_Blank', temperatureVar=LINEAR, 
        consistentMassMatrix=False)
    p1 = mdb.models['Model-1'].parts['Blank']
    session.viewports['Viewport: 1'].setValues(displayedObject=p1)
    p = mdb.models['Model-1'].parts['Blank']
    e = p.edges
    edges = e.getSequenceFromMask(mask=('[#1 ]', ), )
    region = regionToolset.Region(edges=edges)
    p = mdb.models['Model-1'].parts['Blank']
    p.SectionAssignment(region=region, sectionName='Section-1', offset=0.0, 
        offsetType=MIDDLE_SURFACE, offsetField='', 
        thicknessAssignment=FROM_SECTION)


