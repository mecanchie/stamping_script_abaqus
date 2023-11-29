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

def Blank():
    s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
        sheetSize=200.0)
    g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
    s1.setPrimaryObject(option=STANDALONE)
    s1.Line(point1=(0.0, 0.0), point2=(48.75, 0.0))
    s1.HorizontalConstraint(entity=g[2], addUndoState=False)
    s1.FixedConstraint(entity=v[0])
    s1.ObliqueDimension(vertex1=v[0], vertex2=v[1], textPoint=(22.2239456176758, 
        10.7854957580566), value=143.56)
    p = mdb.models['Model-1'].Part(name='Blank', dimensionality=TWO_D_PLANAR, 
        type=DEFORMABLE_BODY)
    p = mdb.models['Model-1'].parts['Blank']
    p.BaseWire(sketch=s1)
    s1.unsetPrimaryObject()
    p = mdb.models['Model-1'].parts['Blank']
    del mdb.models['Model-1'].sketches['__profile__']


