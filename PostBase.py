


def post():
    session.viewports['Viewport: 1'].setValues(displayedObject=None)
    o3 = session.openOdb(name='E:/temp/Job-2.odb')
    session.viewports['Viewport: 1'].setValues(displayedObject=o3)
    session.viewports['Viewport: 1'].makeCurrent()
    a = mdb.models['Model-1'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    session.mdbData.summary()
    session.viewports['Viewport: 1'].setValues(
        displayedObject=session.odbs['E:/temp/Job-2.odb'])
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=OFF, 
        constraints=OFF, connectors=OFF, engineeringFeatures=OFF)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=498.125, 
        farPlane=721.267, width=39.916, height=16.979, viewOffsetX=42.6392, 
        viewOffsetY=0.984373)
    session.Path(name='Path-2', type=NODE_LIST, expression=(('BLANK-1', (1, 201, 
        )), ))
    xyp = session.xyPlots['XYPlot-1']
    chartName = xyp.charts.keys()[0]
    chart = xyp.charts[chartName]
    pth = session.paths['Path-2']
    xy1 = xyPlot.XYDataFromPath(path=pth, includeIntersections=False, 
        projectOntoMesh=False, pathStyle=UNIFORM_SPACING, numIntervals=100, 
        projectionTolerance=0, shape=UNDEFORMED, labelType=TRUE_DISTANCE, 
        removeDuplicateXYPairs=True, includeAllElements=False)
    c1 = session.Curve(xyData=xy1)
    chart.setValues(curvesToPlot=(c1, ), )
    session.charts[chartName].autoColor(lines=True, symbols=True)
    session.viewports['Viewport: 1'].setValues(displayedObject=xyp)
    odb = session.odbs['E:/temp/Job-2.odb']
    session.viewports['Viewport: 1'].setValues(displayedObject=odb)
    session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
        CONTOURS_ON_DEF, ))
    xyp = session.xyPlots['XYPlot-1']
    chartName = xyp.charts.keys()[0]
    chart = xyp.charts[chartName]
    pth = session.paths['Path-2']
    xy1 = xyPlot.XYDataFromPath(path=pth, includeIntersections=False, 
        projectOntoMesh=False, pathStyle=UNIFORM_SPACING, numIntervals=100, 
        projectionTolerance=0, shape=UNDEFORMED, labelType=TRUE_DISTANCE, 
        removeDuplicateXYPairs=True, includeAllElements=False)
    c1 = session.Curve(xyData=xy1)
    chart.setValues(curvesToPlot=(c1, ), )
    session.charts[chartName].autoColor(lines=True, symbols=True)
    session.viewports['Viewport: 1'].setValues(displayedObject=xyp)
    pth = session.paths['Path-2']
    session.XYDataFromPath(name='Mises', path=pth, includeIntersections=False, 
        projectOntoMesh=False, pathStyle=UNIFORM_SPACING, numIntervals=100, 
        projectionTolerance=0, shape=UNDEFORMED, labelType=TRUE_DISTANCE, 
        removeDuplicateXYPairs=True, includeAllElements=False)


