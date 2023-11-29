# -*- coding: mbcs -*-
# Do not delete the following import lines
from abaqus import *
from abaqusConstants import *
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
import __main__

blankHolderRadius = [5]
def Blank_Holder():
    s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
        sheetSize=1000.0)
    g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
    s1.setPrimaryObject(option=STANDALONE)
    s1.rectangle(point1=(0.0, 0.0), point2=(160.0, 140.0))
    s1.FixedConstraint(entity=v[0])
    s1.ObliqueDimension(vertex1=v[0], vertex2=v[1], textPoint=(-56.1858825683594, 
        51.9852905273438), value=50.0)
    s1.ObliqueDimension(vertex1=v[3], vertex2=v[0], textPoint=(83.5055847167969, 
        -24.1911773681641), value=65)
    s1.FilletByRadius(radius=blankHolderRadius[0], curve1=g[2], nearPoint1=(-1.54641723632812, 
        19.5588073730469), curve2=g[5], nearPoint2=(19.072265625, 
        0.514694213867188))
    p = mdb.models['Model-1'].Part(name='Blank_Holder', dimensionality=TWO_D_PLANAR, 
        type=ANALYTIC_RIGID_SURFACE)
    p = mdb.models['Model-1'].parts['Part-1']
    p.AnalyticRigidSurf2DPlanar(sketch=s1)
    s1.unsetPrimaryObject()
    p = mdb.models['Model-1'].parts['Part-1']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    del mdb.models['Model-1'].sketches['__profile__']


Blank_Holder()
