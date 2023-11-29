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

def Die():
    s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
        sheetSize=200.0)
    g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
    s.setPrimaryObject(option=STANDALONE)
    s.Spot(point=(0.0, 0.0))
    s.Spot(point=(80.0, 0.0))
    s.Spot(point=(0.0, 80.0))
    s.Spot(point=(80.0, 80.0))
    s.Line(point1=(0.0, 80.0), point2=(80.0, 80.0))
    s.HorizontalConstraint(entity=g[2], addUndoState=False)
    s.Line(point1=(80.0, 80.0), point2=(80.0, 0.0))
    s.VerticalConstraint(entity=g[3], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[2], entity2=g[3], addUndoState=False)
    s.Line(point1=(80.0, 0.0), point2=(0.0, 0.0))
    s.HorizontalConstraint(entity=g[4], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[3], entity2=g[4], addUndoState=False)
    s.Line(point1=(0.0, 0.0), point2=(0.0, 80.0))
    s.VerticalConstraint(entity=g[5], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[4], entity2=g[5], addUndoState=False)
    s.FilletByRadius(radius=10.0, curve1=g[2], nearPoint1=(74.4298248291016, 
        80.2981185913086), curve2=g[3], nearPoint2=(79.53955078125, 
        75.8002853393555))
    p = mdb.models['Model-1'].Part(name='die', dimensionality=TWO_D_PLANAR, 
        type=ANALYTIC_RIGID_SURFACE)
    p = mdb.models['Model-1'].parts['die']
    p.AnalyticRigidSurf2DPlanar(sketch=s)
    s.unsetPrimaryObject()
    p = mdb.models['Model-1'].parts['die']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    del mdb.models['Model-1'].sketches['__profile__']

dieog()
