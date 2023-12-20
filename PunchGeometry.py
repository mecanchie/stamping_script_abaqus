# -*- coding: mbcs -*-
# Do not delete the following import lines
from abaqus import *
from abaqusConstants import *
import __main__
import section
import regionToolset
import displayGroupMdbToolset as dgm
import part
import material
import assembly
import step
import interaction
import load
import mesh
import optimization
import job
import sketch
import visualization
import xyPlot
import displayGroupOdbToolset as dgo
import connectorBehavior

def PunchGeometry():
    
    s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
        sheetSize=100.0)
    g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
    s1.setPrimaryObject(option=STANDALONE)
    s1.Line(point1=(0.0, 0.0), point2=(0.0, 16.0))
    s1.VerticalConstraint(entity=g[2], addUndoState=False)
    s1.Line(point1=(0.0, 0.0), point2=(14.0, 0.0))
    s1.HorizontalConstraint(entity=g[3], addUndoState=False)
    s1.PerpendicularConstraint(entity1=g[2], entity2=g[3], addUndoState=False)
    s1.ObliqueDimension(vertex1=v[0], vertex2=v[2], textPoint=(3.34565353393555, 
        -5.09044933319092), value=30.0)
    s1.ObliqueDimension(vertex1=v[0], vertex2=v[1], textPoint=(-1.26729583740234, 
        7.67365837097168), value=80.0)
    s1.FilletByRadius(radius=5.0, curve1=g[3], nearPoint1=(3.24427032470703, 
        -0.0253257751464844), curve2=g[2], nearPoint2=(-0.152076721191406, 
        2.6085376739502))
    p = mdb.models['Model-1'].Part(name='Part-1', dimensionality=TWO_D_PLANAR, 
        type=DEFORMABLE_BODY)
    p = mdb.models['Model-1'].parts['Part-1']
    p.AnalyticRigidSurf2DPlanar(sketch=s1)
    s1.unsetPrimaryObject()
    p = mdb.models['Model-1'].parts['Part-1']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    del mdb.models['Model-1'].sketches['__profile__']

PunchGeometry()
